// usage: node render4.js in.html out.pdf [shotsDir]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out, shots] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1.6 });
  await page.goto('file://' + path.resolve(inp));
  await page.waitForFunction(() => window.__done === true, null, { timeout: 60000 });
  console.log((await page.evaluate(() => window.__log)).join('\n'));
  console.log(await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight).filter((v, i, a) => a.indexOf(v) === i).join(' | ')));
  await page.evaluate(() => document.getElementById('flow').remove());
  if (shots) {
    const els = await page.$$('.page');
    for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: `${shots}/p${String(i + 1).padStart(2, '0')}.png` });
  }
  await page.pdf({ path: out, preferCSSPageSize: true, printBackground: true });
  await browser.close();
})();
