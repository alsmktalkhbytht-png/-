// usage: node render.js in.html out.pdf [shotsDir]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out, shots] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1.4 });
  await page.goto('file://' + path.resolve(inp));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  const report = await page.evaluate(() => {
    const mm = px => (px * 25.4 / 96).toFixed(1);
    return [...document.querySelectorAll('.page')].map((p, i) => {
      const body = p.querySelector('.body'), content = p.querySelector('.content'), notes = p.querySelector('.notes');
      const r = { i: i + 1 };
      if (body) {
        r.overflow = body.scrollHeight > body.clientHeight + 1 ? mm(body.scrollHeight - body.clientHeight) : 0;
        r.notesMM = notes ? mm(notes.getBoundingClientRect().height) : '-';
        const lines = p.querySelector('.notes-lines');
        r.lines = lines ? Math.floor(lines.getBoundingClientRect().height / (8.2 * 96 / 25.4)) : '-';
      }
      const fonts = new Set(); return r;
    });
  });
  console.table(report);
  const fontsOk = await page.evaluate(() => [...document.fonts].map(f => f.family + ' ' + f.weight + ' ' + f.status).join(' | '));
  console.log(fontsOk);
  if (shots) {
    const els = await page.$$('.page');
    for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: `${shots}/p${String(i + 1).padStart(2, '0')}.png` });
  }
  await page.pdf({ path: out, preferCSSPageSize: true, printBackground: true });
  await browser.close();
})();
