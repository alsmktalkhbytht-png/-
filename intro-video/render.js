// Render intro.html frame by frame: node render.js <outdir> [fps] [seconds]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const out = process.argv[2], fps = +(process.argv[3] || 30), secs = +(process.argv[4] || 10);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file://' + path.resolve(__dirname, 'intro.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const n = Math.round(fps * secs);
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => window.render(t), i / fps);
    await page.screenshot({ path: `${out}/f${String(i).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 95 });
  }
  await browser.close();
  console.log('frames', n);
})();
