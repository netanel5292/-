#!/usr/bin/env python3
"""Voice-over cut of the trial-class reel.

Same picture edit as build.py (only the end card is 0.7 s longer). The owner's speech is lifted from IMG_0998.MOV,
trimmed to seven sentences, and laid over the reel; the studio sound stays underneath as a quiet bed.
On-screen captions follow the speech, so the video still reads with the sound off.
"""
import json, os, subprocess, sys
import build

S, SEG, OV, OUT, FPS = build.S, build.SEG, build.OV, build.OUT, build.FPS
VOICE = os.path.join(build.BIG, 'IMG_0998.MOV')

# (source in, source out, start on the reel) — cut points sit on the quietest 10 ms between sentences
VO = [
    (0.00, 3.08, 0.00),     # חיפשתם מקום ללמוד אומנויות לחימה? זה הבית.
    (3.14, 6.68, 3.14),     # בין אם זה אתם או החברים שלכם, בואו תראו מה אתם מקבלים פה בדיוק.
    (12.66, 15.95, 6.76),   # כבר בשנה הראשונה עברו במכון הזה מעל 600 מתאמנים.
    (23.04, 26.28, 10.13),  # אנחנו כמכון רוצים לתת את המעטפת הכי בטוחה לכל תלמיד
    (29.60, 33.45, 13.45),  # ובעיקר בעיקר לתת את הביטחון העצמי להגן על עצמו.
    (33.62, 36.30, 17.38),  # הזמן הכי נכון לקבוע אימון ניסיון זה עכשיו.
    (36.88, 37.85, 20.20),  # צרו איתנו קשר.
]
# caption chunks: (html, source in, source out, index of the VO sentence). <b> = gold emphasis.
CHUNKS = [
    ('<b>זה הבית.</b>', 2.20, 3.08, 0),
    ('בין אם זה אתם', 3.14, 3.90, 1), ('או החברים שלכם', 3.90, 4.87, 1), ('בואו תראו', 4.87, 5.40, 1),
    ('מה אתם <b>מקבלים פה</b>', 5.40, 6.20, 1), ('בדיוק', 6.20, 6.68, 1),
    ('כבר בשנה', 12.66, 13.20, 2), ('הראשונה עברו', 13.20, 13.83, 2), ('במכון הזה', 13.83, 14.45, 2),
    ('מעל <b>600</b> מתאמנים', 14.45, 15.95, 2),
    ('אנחנו כמכון', 23.04, 23.90, 3), ('רוצים לתת', 23.90, 24.50, 3), ('את המעטפת', 24.50, 25.08, 3),
    ('<b>הכי בטוחה</b>', 25.08, 25.60, 3), ('לכל תלמיד', 25.60, 26.28, 3),
    ('ובעיקר בעיקר', 29.60, 30.57, 4), ('לתת את', 30.57, 31.00, 4), ('<b>הביטחון העצמי</b>', 31.00, 32.25, 4),
    ('להגן על עצמו', 32.25, 33.45, 4),
]
HOOK_END = 2.20   # the opening question stays up until "זה הבית"
END_FRAMES = 129  # 4.3 s end card, so the last spoken line does not land on the final frame

def reel_time(src_t, i):
    a, _, at = VO[i]
    return at + (src_t - a)

def main():
    # longer end card
    end = dict(build.SEGMENTS['END']); end['n'] = END_FRAMES
    build.SEGMENTS['ENDV'] = end
    build.build_segment('ENDV', end)
    os.rename(os.path.join(SEG, 'ENDV.mkv'), os.path.join(SEG, 'ENDV.mkv'))

    chunks = [dict(name=f'vo_{k:02d}', html=h, st=round(reel_time(a, i), 3), en=round(reel_time(b, i), 3)) for k, (h, a, b, i) in enumerate(CHUNKS)]
    json.dump(chunks, open(os.path.join(OV, 'vo_chunks.json'), 'w'), ensure_ascii=False, indent=1)
    subprocess.run(['node', os.path.join(S, 'scripts', 'vo_overlays.js')], check=True)

    for v, opening in (('A', ['A1', 'A2']), ('B', ['B1'])):
        order = opening + ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S11', 'S10', 'ENDV']
        tl, total = build.timeline(order)
        lst = os.path.join(SEG, f'list_vo_{v}.txt')
        with open(lst, 'w') as f:
            for sid in order:
                f.write(f"file '{os.path.join(SEG, sid + '.mkv')}'\n")
        base = os.path.join(SEG, f'base_vo_{v}.mkv')
        build.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', base])

        caps = [('vo_hook_1', 0.0, HOOK_END, 'cut'), ('vo_hook_2', 0.0, HOOK_END, 'cut')]
        caps += [(c['name'], c['st'], c['en'], 'pop') for c in chunks]
        caps += [('lab_muay', *tl['S2'], 'pop'), ('lab_box', *tl['S3'], 'pop'), ('lab_wres', *tl['S4'], 'pop'), ('lab_bjj', *tl['S5'], 'pop'),
                 ('badge', 0.0, tl['ENDV'][0], 'cut'), ('end', *tl['ENDV'], 'endcard')]
        inputs = ['-i', base, '-i', VOICE]
        for name, *_ in caps:
            inputs += ['-loop', '1', '-framerate', str(FPS), '-t', f'{total:.4f}', '-i', os.path.join(OV, name + '.png')]
        fc = []; last = '0:v'
        for i, (name, st, en, mode) in enumerate(caps, start=2):
            lab = f'c{i}'
            if mode == 'pop':
                fc.append(f"[{i}:v]format=rgba,fade=t=in:st={st:.4f}:d=0.08:alpha=1[{lab}]")
                y = f"'if(lt(t-{st:.4f},0.1),18*pow(1-(t-{st:.4f})/0.1,2),0)'"
            elif mode == 'endcard':
                fc.append(f"[{i}:v]format=rgba,fade=t=in:st={st:.4f}:d=0.2:alpha=1[{lab}]"); y = '0'
            else:
                fc.append(f"[{i}:v]format=rgba[{lab}]"); y = '0'
            fc.append(f"[{last}][{lab}]overlay=x=0:y={y}:enable='between(t,{st:.4f},{en - 0.0005:.4f})':format=auto[v{i}]")
            last = f'v{i}'
        fc.append(f"[{last}]format=yuv420p[vout]")
        # voice: seven trimmed sentences placed on the reel
        vlabs = []
        for k, (a, b, at) in enumerate(VO):
            d = b - a
            fc.append(f"[1:a]atrim=start={a}:end={b},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,"
                      f"afade=t=in:st=0:d=0.012,afade=t=out:st={d - 0.035:.3f}:d=0.035,adelay={int(at * 1000)}:all=1[vo{k}]")
            vlabs.append(f'[vo{k}]')
        fc.append(''.join(vlabs) + f"amix=inputs={len(VO)}:normalize=0:dropout_transition=0,highpass=f=85,"
                  "agate=threshold=0.05:ratio=1.6:range=0.45:attack=8:release=180:knee=4,"
                  "acompressor=threshold=-20dB:ratio=3:attack=6:release=90:makeup=1.5,equalizer=f=3200:t=q:w=1.2:g=2,volume=-2.5dB,"
                  f"apad=whole_dur={total:.4f},asplit=2[voice][key]")
        # studio sound as a bed: lowered, and ducked a little further whenever he speaks
        fc.append("[0:a]volume=-9dB[bed0];[bed0][key]sidechaincompress=threshold=0.02:ratio=5:attack=12:release=260[bed]")
        fc.append("[bed][voice]amix=inputs=2:normalize=0:dropout_transition=0,alimiter=limit=0.89:attack=3:release=60,loudnorm=I=-14:TP=-1.5:LRA=9[aout]")
        final = os.path.join(OUT, f'JewJitsu_trial_{v}_voice.mp4')
        build.run(['ffmpeg', '-nostdin', '-v', 'error', '-y'] + inputs + [
            '-filter_complex', ';'.join(fc), '-map', '[vout]', '-map', '[aout]',
            '-c:v', 'libx264', '-profile:v', 'high', '-level', '4.2', '-preset', 'slow', '-crf', '17', '-maxrate', '14M', '-bufsize', '28M',
            '-pix_fmt', 'yuv420p', '-r', str(FPS), '-g', str(FPS * 2),
            '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
            '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', '-t', f'{total:.4f}', final])
        print(f'version {v} voice: {total:.2f}s -> {final}')

if __name__ == '__main__':
    main()
