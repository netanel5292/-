// Caption overlays for the voice-over cut: the opening question and one PNG per spoken chunk (RTL Hebrew).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const S = path.resolve(__dirname, '..');
const OUT = path.join(S, 'ov');
const font = f => 'data:font/ttf;base64,' + fs.readFileSync(path.join(S, 'fonts', f)).toString('base64');
const chunks = JSON.parse(fs.readFileSync(path.join(OUT, 'vo_chunks.json'), 'utf8'));

const css = `
@font-face{font-family:"Rubik";src:url(${font('Rubik.ttf')});font-weight:300 900}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;background:transparent;overflow:hidden}
body{font-family:"Rubik",sans-serif;direction:rtl;color:#fff;position:relative}
.col{position:absolute;left:90px;width:840px;display:flex;flex-direction:column;align-items:center;text-align:center}
.pill{display:inline-block;background:#e8b92e;color:#141a2b;font-weight:900;border-radius:999px;line-height:1;white-space:nowrap}
.big{font-weight:900;line-height:1.08;letter-spacing:-1px;white-space:nowrap;
  text-shadow:0 0 18px rgba(0,0,0,.75),0 6px 0 rgba(0,0,0,.55),0 0 4px #000;-webkit-text-stroke:3px rgba(10,14,26,.9);paint-order:stroke fill}
.gold,b{color:#e8b92e;font-weight:900}
/* spoken captions: one short chunk at a time, same band as the sentence captions of the silent cut */
.say{font-weight:900;font-size:92px;line-height:1.1;letter-spacing:-1px;text-wrap:balance;max-width:840px;
  text-shadow:0 0 20px rgba(0,0,0,.8),0 6px 0 rgba(0,0,0,.6),0 0 4px #000;-webkit-text-stroke:3.5px rgba(10,14,26,.92);paint-order:stroke fill}
`;
const page = body => `<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><style>${css}</style></head><body>${body}</body></html>`;
const hook = inner => `<div class="col" style="top:820px;height:480px;justify-content:flex-end">${inner}</div>`;
const say = inner => `<div class="col" style="top:1060px;height:240px;justify-content:center"><div class="say">${inner}</div></div>`;

const overlays = {
  vo_hook_1: hook(`<span class="pill" style="font-size:66px;padding:16px 38px 22px;margin-bottom:300px">אשקלון,</span>`),
  vo_hook_2: hook(`<div class="big" style="font-size:86px">חיפשתם מקום ללמוד</div><div class="big gold" style="font-size:104px;margin-top:6px">אומנויות לחימה?</div><div style="height:22px"></div>`),
};
for (const c of chunks) overlays[c.name] = say(c.html);

(async () => {
  const browser = await chromium.launch();
  const p = await (await browser.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 })).newPage();
  for (const [name, body] of Object.entries(overlays)) {
    await p.setContent(page(body), { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    const box = await p.evaluate(() => {
      const el = document.querySelector('.say') || document.querySelector('.col');
      const range = document.createRange(); range.selectNodeContents(el);
      const r = range.getBoundingClientRect();
      return [Math.round(r.left), Math.round(r.top), Math.round(r.right), Math.round(r.bottom)];
    });
    await p.screenshot({ path: path.join(OUT, name + '.png'), omitBackground: true });
    console.log(name.padEnd(10), box.join(','));
  }
  await browser.close();
})();
