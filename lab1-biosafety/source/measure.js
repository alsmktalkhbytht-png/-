const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.resolve(process.argv[2]));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const r=await p.evaluate(()=>{const o={};document.querySelectorAll('[data-m]').forEach(e=>{const cs=getComputedStyle(e.firstElementChild||e);const r=e.getBoundingClientRect();o[e.dataset.m]=r.height*25.4/96;});return o;});
console.log(JSON.stringify(r));await b.close();})();
