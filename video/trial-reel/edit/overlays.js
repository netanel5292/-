// Renders the Hebrew (RTL) caption overlays as transparent 1080x1920 PNGs with Chromium.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const S = path.resolve(__dirname, '..');
const OUT = path.join(S, 'ov');
const logo = 'data:image/png;base64,' + fs.readFileSync('/home/user/-/brand/logo-lion-gloves.png').toString('base64');
const logoTight = 'data:image/png;base64,' + fs.readFileSync(path.join(S, 'ov', 'logo_tight.png')).toString('base64');
const font = f => 'data:font/ttf;base64,' + fs.readFileSync(path.join(S, 'fonts', f)).toString('base64');

const css = `
@font-face{font-family:"Rubik";src:url(${font('Rubik.ttf')});font-weight:300 900}
@font-face{font-family:"Assistant";src:url(${font('Assistant.ttf')});font-weight:200 800}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;background:transparent;overflow:hidden}
body{font-family:"Rubik",sans-serif;direction:rtl;color:#fff;position:relative}
/* text column: kept clear of the app UI (top bar, right-hand buttons, bottom caption area) */
.col{position:absolute;left:90px;width:840px;display:flex;flex-direction:column;align-items:center;text-align:center}
.pill{display:inline-block;background:#e8b92e;color:#141a2b;font-weight:900;border-radius:999px;line-height:1;white-space:nowrap}
.big{font-weight:900;line-height:1.08;letter-spacing:-1px;white-space:nowrap;
  text-shadow:0 0 18px rgba(0,0,0,.75),0 6px 0 rgba(0,0,0,.55),0 0 4px #000;-webkit-text-stroke:3px rgba(10,14,26,.9);paint-order:stroke fill}
.gold{color:#e8b92e}
.box{display:inline-block;background:rgba(20,26,43,.86);border-radius:28px;padding:22px 38px 26px;font-weight:800;font-size:62px;line-height:1.15;white-space:nowrap;
  box-shadow:0 10px 30px rgba(0,0,0,.35);border:3px solid rgba(232,185,46,.0)}
.label{display:inline-block;background:#e8b92e;color:#141a2b;font-weight:900;font-size:80px;line-height:1;border-radius:26px;padding:22px 42px 28px;white-space:nowrap;
  box-shadow:0 12px 34px rgba(0,0,0,.45)}
.badge{position:absolute;left:56px;top:240px;width:108px;height:108px;border-radius:50%;background:#fff;overflow:hidden;box-shadow:0 6px 18px rgba(0,0,0,.45);border:4px solid #141a2b}
.badge img{position:absolute;width:200px;left:-45px;top:-13px}
`;

const page = body => `<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><style>${css}</style></head><body>${body}</body></html>`;

// Hook block sits in the lower-middle: bottom edge ~y=1380, above the app caption area.
const hook = inner => `<div class="col" style="top:820px;height:480px;justify-content:flex-end">${inner}</div>`;
const lower = inner => `<div class="col" style="top:1080px;height:200px;justify-content:center">${inner}</div>`;
const upper = inner => `<div class="col" style="top:290px;height:150px;justify-content:center">${inner}</div>`;

const overlays = {
  // A: action opening
  hookA_1: hook(`<span class="pill" style="font-size:66px;padding:16px 38px 22px;margin-bottom:300px">אשקלון,</span>`),
  hookA_2: hook(`<div class="big" style="font-size:98px">תמיד רצית לנסות</div><div class="big gold" style="font-size:104px;margin-top:6px">אומנויות לחימה?</div><div style="height:22px"></div>`),
  // B: direct address opening
  hookB_1: hook(`<span class="pill" style="font-size:66px;padding:16px 38px 22px;margin-bottom:300px">אשקלון,</span>`),
  hookB_2: hook(`<div class="big" style="font-size:104px">רוצים להתחיל</div><div class="big gold" style="font-size:112px;margin-top:6px">להתאמן?</div><div style="height:14px"></div>`),
  cap_look: lower(`<span class="box">ככה נראה <span class="gold">אימון אצלנו</span></span>`),
  lab_muay: upper(`<span class="label">אגרוף תאילנדי</span>`),
  lab_box: upper(`<span class="label">אגרוף קלאסי</span>`),
  lab_wres: upper(`<span class="label">היאבקות</span>`),
  lab_bjj: upper(`<span class="label">ג׳יו-ג׳יטסו</span>`),
  cap_learn: lower(`<span class="box">קודם <span class="gold">לומדים</span> את התנועה</span>`),
  cap_drill: lower(`<span class="box">ואז <span class="gold">מתרגלים</span> עם פרטנר</span>`),
  cap_group: lower(`<span class="box">וכל זה <span class="gold">ביחד</span>, עם הקבוצה</span>`),
  cap_new: `<div class="col" style="top:1030px;height:270px;justify-content:center"><span class="box" style="text-align:center;white-space:normal;line-height:1.22">אף פעם לא התאמנתם?<br><span class="gold">בואו לנסות</span></span></div>`,
  badge: `<div class="badge"><img src="${logo}"></div>`,
  // End card: everything between y≈330 and y≈1330
  end: `
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,18,33,.90) 0%,rgba(20,26,43,.84) 45%,rgba(13,18,33,.93) 100%)"></div>
  <div style="position:absolute;left:0;right:0;top:330px;display:flex;justify-content:center">
    <div style="width:330px;height:300px;border-radius:44px;background:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 40px rgba(0,0,0,.5);border:6px solid #e8b92e">
      <img src="${logoTight}" style="width:296px;height:auto;display:block">
    </div>
  </div>
  <div class="col" style="top:690px">
    <div style="font-weight:900;font-size:112px;line-height:1.06;letter-spacing:-1px;white-space:nowrap">רוצים</div>
    <div style="font-weight:900;font-size:112px;line-height:1.06;letter-spacing:-1px;white-space:nowrap" class="gold">אימון ניסיון?</div>
    <div style="margin-top:46px;font-weight:800;font-size:68px;line-height:1.1;white-space:nowrap;display:flex;align-items:center;gap:20px">
      <span>שלחו לנו</span><span class="pill" style="font-size:72px;padding:16px 34px 24px;border-radius:24px">״ניסיון״</span><span>בהודעה</span>
    </div>
    <div style="width:560px;height:5px;border-radius:3px;background:rgba(232,185,46,.9);margin:54px 0 40px"></div>
    <div style="font-family:'Assistant',sans-serif;font-weight:800;font-size:62px;line-height:1.15;white-space:nowrap;display:flex;align-items:center;gap:16px">
      <svg width="46" height="58" viewBox="0 0 24 30" style="flex:none"><path fill="#e8b92e" d="M12 0C5.4 0 0 5.3 0 11.8 0 20.5 12 30 12 30s12-9.5 12-18.2C24 5.3 18.6 0 12 0zm0 16.6a4.9 4.9 0 1 1 0-9.8 4.9 4.9 0 0 1 0 9.8z"/></svg>
      <span>קניון לב אשקלון&nbsp;&nbsp;|&nbsp;&nbsp;קומה עליונה</span>
    </div>
  </div>`,
};

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const p = await ctx.newPage();
  const report = {};
  for (const [name, body] of Object.entries(overlays)) {
    await p.setContent(page(body), { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    // bounding box of everything visible, to verify nothing leaves the safe area
    report[name] = await p.evaluate(() => {
      let b = null;
      for (const el of document.querySelectorAll('body *')) {
        if (el.children.length && !['SPAN', 'DIV'].includes(el.tagName)) continue;
        const cs = getComputedStyle(el);
        if (el.classList.contains('col') || cs.position === 'absolute' && el.style.inset === '0px') continue;
        const r = el.getBoundingClientRect();
        if (!r.width || !r.height) continue;
        if (!el.textContent.trim() && el.tagName !== 'IMG' && el.tagName !== 'svg' && cs.backgroundColor === 'rgba(0, 0, 0, 0)') continue;
        b = b ? { l: Math.min(b.l, r.left), t: Math.min(b.t, r.top), r: Math.max(b.r, r.right), b: Math.max(b.b, r.bottom) } : { l: r.left, t: r.top, r: r.right, b: r.bottom };
      }
      const fonts = [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family);
      return { box: b && Object.fromEntries(Object.entries(b).map(([k, v]) => [k, Math.round(v)])), fonts };
    });
    await p.screenshot({ path: path.join(OUT, name + '.png'), omitBackground: true });
  }
  await browser.close();
  for (const [k, v] of Object.entries(report)) console.log(k.padEnd(10), JSON.stringify(v.box), v.fonts.join(','));
})();
