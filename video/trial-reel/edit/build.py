#!/usr/bin/env python3
"""Builds the two Jew Jitsu Ashkelon trial-class promo cuts (A: action opening, B: direct-address opening).

Everything after the opening is cut from the same segment files, so the two versions differ only in the first 2.4 s.

Folders expected next to this script's parent: big/ (source clips downloaded from the Drive folder "מדיה לעריכה"),
fonts/ (Rubik.ttf, Assistant.ttf from Google Fonts), ov/ (caption PNGs from overlays.js, plus logo_tight.png).
Run overlays.js first, then: python3 build.py
"""
import subprocess, sys, json, os, re

S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIG, SEG, OV, OUT = (os.path.join(S, d) for d in ('big', 'seg', 'ov', 'out'))
FPS = 30
W, H = 1080, 1920
TARGET_RMS = -21.0   # per-segment mean level before the final loudness pass

def run(cmd, capture=False):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(' '.join(cmd) + '\n' + r.stderr[-3000:] + '\n')
        raise SystemExit(1)
    return r.stderr if capture else None

def mean_volume(src, ss, dur):
    err = run(['ffmpeg', '-nostdin', '-ss', f'{ss}', '-t', f'{dur}', '-i', src, '-vn', '-af', 'highpass=f=70,volumedetect', '-f', 'null', '-'], capture=True)
    m = re.search(r'mean_volume: (-?[\d.]+) dB', err); p = re.search(r'max_volume: (-?[\d.]+) dB', err)
    return float(m.group(1)), float(p.group(1))

# id, source file, in-point (s), frames, crop (w:h:x:y on the upright picture) or None,
# opts: zoom = slow push-in amount, sharp = extra sharpening for low-res sources, grade = False to leave graded footage alone,
#       audio = (file, in-point) to take the sound from another clip of the studio (used where the original track is music)
SEGMENTS = {
    # --- openings ---
    'A1':  dict(src='IMG_1398.MOV', ss=11.10, n=50, crop=None, grade=False, audio=('IMG_1496.MOV', 9.75)),
    'A2':  dict(src='IMG_1398.MOV', ss=21.55, n=22, crop=None, grade=False, audio=('IMG_1496.MOV', 9.75 + 50 / 30)),
    'B1':  dict(src='20260209_073931.mp4', ss=0.0, n=72, crop='1126:2002:560:950', zoom=0.07),
    # --- shared body ---
    'S1':  dict(src='IMG_1496.MOV', ss=6.35, n=36, crop='1300:2311:150:260'),
    'S2':  dict(src='IMG_0548.MOV', ss=1.27, n=32, crop='1512:2688:324:500'),
    'S3':  dict(src='IMG_0052.MOV', ss=6.60, n=36, crop='1512:2688:324:560'),
    'S4':  dict(src='netanel-video-16MB.mp4', ss=12.75, n=51, crop='540:960:108:320', sharp=True),
    'S5':  dict(src='VID-20260129-WA0042.mp4', ss=0.40, n=45, crop='440:782:0:0', sharp=True),
    'S6':  dict(src='IMG_1604.MOV', ss=5.80, n=78, crop='880:1564:447:520', zoom=0.06),
    'S7':  dict(src='IMG_0569.MOV', ss=3.30, n=22, crop='1400:2489:700:250'),
    'S8':  dict(src='IMG_0404.MOV', ss=1.30, n=60, crop=None),
    'S9':  dict(src='IMG_1398.MOV', ss=23.33, n=36, crop=None, grade=False, audio=('IMG_1507.MOV', 13.0)),
    'S11': dict(src='IMG_0569.MOV', ss=5.35, n=33, crop=None),
    'S10': dict(src='IMG_0051.MOV', ss=8.72, n=26, crop=None),
    # --- end card background (blurred wide shot of a class) ---
    'END': dict(src='IMG_1507.MOV', ss=12.7, n=108, crop=None, blur=True, audio=('IMG_1507.MOV', 15.0), gain_db=-7, fade_out=1.4),
}
ORDER_BODY = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S11', 'S10', 'END']
VERSIONS = {'A': ['A1', 'A2'] + ORDER_BODY, 'B': ['B1'] + ORDER_BODY}

def build_segment(sid, s):
    out = os.path.join(SEG, sid + '.mp4')
    src = os.path.join(BIG, s['src'])
    dur = s['n'] / FPS
    vf = []
    if s.get('crop'):
        vf.append('crop=' + s['crop'])
    if s.get('zoom'):
        # scale up first so the push-in moves in sub-pixel steps of the final picture
        vf += [f'scale={W*2}:{H*2}:flags=lanczos', f'fps={FPS}',
               f"zoompan=z='1+{s['zoom']}*on/{s['n']}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}"]
    else:
        vf += [f'scale={W}:{H}:flags=lanczos', f'fps={FPS}']
    if s.get('sharp'):
        vf.append('hqdn3d=1.5:1.5:4:4,unsharp=5:5:0.7:5:5:0.0')
    if s.get('grade', True) and not s.get('blur'):
        vf.append('eq=contrast=1.06:saturation=1.14:brightness=0.005')
    if s.get('blur'):
        vf.append('boxblur=22:3,eq=brightness=-0.08:saturation=0.9')
    vf += ['setsar=1', 'format=yuv420p']

    asrc, ass = s.get('audio', (s['src'], s['ss']))
    asrc = os.path.join(BIG, asrc)
    mean, peak = mean_volume(asrc, ass, dur)
    gain = max(-14.0, min(16.0, TARGET_RMS - mean)) + s.get('gain_db', 0)
    gain = min(gain, -1.0 - peak) if peak + gain > -1.0 else gain   # never push a peak past -1 dBFS
    af = ['aresample=48000', 'aformat=channel_layouts=stereo', 'highpass=f=70', f'volume={gain:.1f}dB',
          'afade=t=in:st=0:d=0.02', f'afade=t=out:st={max(0, dur - (s.get("fade_out") or 0.025)):.3f}:d={s.get("fade_out") or 0.025}',
          f'apad=whole_dur={dur:.4f}', f'atrim=0:{dur:.4f}']
    cmd = ['ffmpeg', '-nostdin', '-v', 'error', '-y',
           '-ss', f'{s["ss"]}', '-i', src,
           '-ss', f'{ass}', '-i', asrc,
           '-map', '0:v:0', '-map', '1:a:0',
           '-vf', ','.join(vf), '-frames:v', str(s['n']),
           '-af', ','.join(af),
           '-c:v', 'libx264', '-preset', 'medium', '-crf', '12', '-g', '15', '-pix_fmt', 'yuv420p',
           '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', '-t', f'{dur:.4f}', '-f', 'matroska', out.replace('.mp4', '.mkv')]
    run(cmd)
    print(f'{sid:4s} {s["src"]:28s} in={s["ss"]:6.2f} frames={s["n"]:3d} ({dur:.2f}s) audio={os.path.basename(asrc)}@{ass:.2f} mean={mean:.1f} gain={gain:+.1f}dB')

def timeline(order):
    t = 0; tl = {}
    for sid in order:
        n = SEGMENTS[sid]['n']; tl[sid] = (t / FPS, (t + n) / FPS); t += n
    return tl, t / FPS

# caption overlays: (png, start, end, appear) — appear: 'pop' = fade+slide in, 'cut' = on from the first frame
def captions(v, tl):
    o = []
    open_end = tl['S1'][0]
    if v == 'A':
        o += [('hookA_1', 0.0, open_end, 'cut'), ('hookA_2', 0.10, open_end, 'pop')]
    else:
        o += [('hookB_1', 0.0, open_end, 'cut'), ('hookB_2', 0.10, open_end, 'pop')]
    o += [('cap_look', tl['S1'][0], tl['S1'][1], 'pop'),
          ('lab_muay', tl['S2'][0], tl['S2'][1], 'pop'),
          ('lab_box', tl['S3'][0], tl['S3'][1], 'pop'),
          ('lab_wres', tl['S4'][0], tl['S4'][1], 'pop'),
          ('lab_bjj', tl['S5'][0], tl['S5'][1], 'pop'),
          ('cap_learn', tl['S6'][0], tl['S6'][1], 'pop'),
          ('cap_drill', tl['S7'][0], tl['S8'][0] + 1.0, 'pop'),
          ('cap_group', tl['S8'][0] + 1.0, tl['S9'][1], 'pop'),
          ('cap_new', tl['S11'][0], tl['S10'][1], 'pop'),
          ('badge', 0.0, tl['END'][0], 'cut'),
          ('end', tl['END'][0], tl['END'][1], 'endcard')]
    return o

def assemble(v):
    order = VERSIONS[v]
    tl, total = timeline(order)
    lst = os.path.join(SEG, f'list_{v}.txt')
    with open(lst, 'w') as f:
        for sid in order:
            f.write(f"file '{os.path.join(SEG, sid + '.mkv')}'\n")
    base = os.path.join(SEG, f'base_{v}.mkv')
    run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', base])

    caps = captions(v, tl)
    inputs = ['-i', base]
    for name, *_ in caps:
        inputs += ['-loop', '1', '-framerate', str(FPS), '-t', f'{total:.4f}', '-i', os.path.join(OV, name + '.png')]
    fc = []; last = '0:v'
    for i, (name, st, en, mode) in enumerate(caps, start=1):
        lab = f'c{i}'
        if mode == 'pop':
            fc.append(f"[{i}:v]format=rgba,fade=t=in:st={st:.4f}:d=0.13:alpha=1[{lab}]")
            y = f"'if(lt(t-{st:.4f},0.16),26*pow(1-(t-{st:.4f})/0.16,2),0)'"
        elif mode == 'endcard':
            fc.append(f"[{i}:v]format=rgba,fade=t=in:st={st:.4f}:d=0.2:alpha=1[{lab}]")
            y = '0'
        else:
            fc.append(f"[{i}:v]format=rgba[{lab}]"); y = '0'
        nxt = f'v{i}'
        fc.append(f"[{last}][{lab}]overlay=x=0:y={y}:enable='between(t,{st:.4f},{en - 0.0005:.4f})':format=auto[{nxt}]")
        last = nxt
    # a real kick impact from the studio's own footage lands as the end card comes in
    hit_at = tl['END'][0]
    fc.append(f"[{last}]format=yuv420p[vout]")
    fc.append(f"[0:a]alimiter=limit=0.84:attack=3:release=60,loudnorm=I=-15:TP=-1.5:LRA=11[aout]")
    final = os.path.join(OUT, f'JewJitsu_trial_{v}.mp4')
    cmd = ['ffmpeg', '-nostdin', '-v', 'error', '-y'] + inputs + [
        '-filter_complex', ';'.join(fc), '-map', '[vout]', '-map', '[aout]',
        '-c:v', 'libx264', '-profile:v', 'high', '-level', '4.2', '-preset', 'slow', '-crf', '17', '-maxrate', '14M', '-bufsize', '28M',
        '-pix_fmt', 'yuv420p', '-r', str(FPS), '-g', str(FPS * 2),
        '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
        '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
        '-movflags', '+faststart', '-t', f'{total:.4f}', final]
    run(cmd)
    json.dump({'total': total, 'timeline': tl, 'captions': caps}, open(os.path.join(OUT, f'timeline_{v}.json'), 'w'), ensure_ascii=False, indent=1)
    print(f'version {v}: {total:.2f}s -> {final}')
    for sid in order:
        print(f'   {tl[sid][0]:6.2f}-{tl[sid][1]:6.2f}  {sid:4s} {SEGMENTS[sid]["src"]} @ {SEGMENTS[sid]["ss"]:.2f}-{SEGMENTS[sid]["ss"] + SEGMENTS[sid]["n"] / FPS:.2f}')

if __name__ == '__main__':
    os.makedirs(SEG, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    only = sys.argv[1:]
    if not only or 'seg' in only:
        for sid, s in SEGMENTS.items():
            build_segment(sid, s)
    if not only or 'asm' in only:
        for v in VERSIONS:
            assemble(v)
