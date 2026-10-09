// node render.js measure in.html            -> JSON {data-m: height in mm}
// node render.js pdf in.html out.pdf [dir]  -> PDF (+ one PNG per page in dir), prints overflow report
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [mode, inp, out, shots] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1.4 });
  await page.goto('file://' + path.resolve(inp));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  if (mode === 'measure') {
    const r = await page.evaluate(() => {
      const o = {};
      document.querySelectorAll('[data-m]').forEach(e => { o[e.dataset.m] = e.getBoundingClientRect().height * 25.4 / 96; });
      return o;
    });
    console.log(JSON.stringify(r));
  } else {
    const report = await page.evaluate(() => [...document.querySelectorAll('.page')].map((p, i) => {
      const b = p.querySelector('.body');
      const over = b ? (b.scrollHeight - b.clientHeight) * 25.4 / 96 : 0;
      return over > 0.5 ? `page ${i} overflows by ${over.toFixed(1)}mm` : null;
    }).filter(Boolean));
    const bad = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'error').map(f => f.family));
    console.log(report.length ? report.join('\n') : 'no overflow');
    if (bad.length) console.log('FONT LOAD ERRORS: ' + bad.join(', '));
    if (shots) {
      const els = await page.$$('.page');
      for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: `${shots}/p${String(i).padStart(2, '0')}.png` });
    }
    await page.pdf({ path: out, preferCSSPageSize: true, printBackground: true });
  }
  await browser.close();
})();
