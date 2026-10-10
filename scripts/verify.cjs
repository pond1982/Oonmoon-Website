// Development-only verification. No dependency is served to visitors.
const fs=require('fs'), path=require('path'), assert=require('assert');
const {chromium}=require('/Applications/ChatGPT.app/Contents/Resources/cua_node/lib/node_modules/playwright');
const ROOT=path.resolve(__dirname,'..'), OUT=path.join(ROOT,'verification');fs.mkdirSync(OUT,{recursive:true});
const BASE=process.env.OONMOON_TEST_URL||'http://127.0.0.1:8080/';
const routes=['','en/','th/',...['features','stories','support','privacy'].flatMap(p=>['en/'+p+'/','th/'+p+'/'])];
const report={started:new Date().toISOString(),base:BASE,checks:[],errors:[]};
function ok(name,detail){report.checks.push({name,status:'PASS',detail});}
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',args:['--no-first-run','--no-default-browser-check']});
 try {
  const context=await browser.newContext({viewport:{width:1440,height:900},locale:'en-US'});
  const page=await context.newPage();const bad=[];page.on('pageerror',error=>bad.push(String(error)));page.on('response',r=>{if(r.status()>=400)bad.push(r.status()+' '+r.url());});
  for(const route of routes){
   await page.goto(BASE+route);await page.waitForLoadState('networkidle');
   const data=await page.evaluate(()=>({lang:document.documentElement.lang,h1:document.querySelectorAll('h1').length,title:document.title,description:document.querySelector('meta[name=description]')?.content,canonical:document.querySelector('link[rel=canonical]')?.href,alternates:[...document.querySelectorAll('link[hreflang]')].map(x=>({lang:x.hreflang,url:x.href})),mainText:document.querySelector('main')?.innerText.length,missingAlt:[...document.images].filter(x=>!x.hasAttribute('alt')).length,broken:[...document.images].filter(x=>x.complete&&!x.naturalWidth).map(x=>x.src),scripts:[...document.scripts].map(x=>x.src),bodyWidth:document.body.scrollWidth,viewport:innerWidth}));
   assert.equal(data.h1,1,route+' h1');assert.ok(data.description&&data.title,route+' metadata');assert.equal(data.missingAlt,0);assert.equal(data.broken.length,0);assert.ok(data.mainText>200);assert.equal(data.bodyWidth<=data.viewport,true,route+' overflow');assert.deepEqual(data.alternates.map(x=>x.lang),['en','th','x-default']);assert.equal(data.lang,route.startsWith('th/')?'th':'en');ok('Static page '+(route||'/'),data);
   const links=await page.locator('a[href]').evaluateAll(nodes=>nodes.map(n=>n.href));
   for(const link of new Set(links)){if(link.startsWith(BASE)){const result=await context.request.get(link);assert.ok(result.ok(),route+' broken link '+link);}}ok('Internal links '+(route||'/'),'all internal targets return 200');
  }
  for(const viewport of [{width:320,height:568},{width:390,height:844},{width:768,height:1024},{width:1024,height:768},{width:1440,height:900}]){
   await page.setViewportSize(viewport);
   for(const route of routes){await page.goto(BASE+route);await page.waitForLoadState('networkidle');const overflow=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,body:document.body.scrollWidth,offenders:[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>innerWidth+1&&getComputedStyle(e).position!=='absolute').slice(0,8).map(e=>e.tagName+'.'+e.className)}));assert.ok(overflow.scroll<=overflow.width&&overflow.body<=overflow.width,JSON.stringify({route,viewport,overflow}));}
   ok('Responsive '+viewport.width+'×'+viewport.height,'11 routes: no horizontal overflow');
  }
  for(const [name,locale,stored,want] of [['Thai first visit','th-TH',null,'th'],['English first visit','en-US',null,'en'],['Unsupported fallback','fr-FR',null,'en'],['Manual override','th-TH','en','en']]){
   const ctx=await browser.newContext({locale});if(stored)await ctx.addInitScript(value=>localStorage.setItem('oonmoon-language',value),stored);const p=await ctx.newPage();await p.goto(BASE);assert.equal(await p.locator('[data-continue]').getAttribute('data-language'),want);assert.equal(p.url(),BASE);ok(name,{suggested:want,noRedirect:true});await ctx.close();
  }
  const override=await browser.newContext({locale:'th-TH'});const p=await override.newPage();await p.goto(BASE+'th/features/');await p.locator('.language-switch [data-language=en]').click();assert.equal(p.url(),BASE+'en/features/');assert.equal(await p.evaluate(()=>localStorage.getItem('oonmoon-language')),'en');await p.goto(BASE);assert.equal(await p.locator('[data-continue]').getAttribute('data-language'),'en');await p.goto(BASE+'th/privacy/');assert.equal(p.url(),BASE+'th/privacy/');ok('Manual switch and remembered choice','same counterpart page; stored en wins at neutral root; direct th remains th');await override.close();
  const nojs=await browser.newContext({javaScriptEnabled:false});const nj=await nojs.newPage();for(const route of routes){await nj.goto(BASE+route);assert.ok((await nj.locator('main').innerText()).length>200);assert.equal(await nj.locator('.language-switch a').count(),2);}ok('JavaScript disabled','11 routes contain static main content and 2 language links');await nojs.close();
  const blocked=await browser.newContext({locale:'th-TH'});await blocked.addInitScript(()=>{Object.defineProperty(window,'localStorage',{get(){throw new Error('storage blocked')}})});const bp=await blocked.newPage();await bp.goto(BASE);assert.equal(await bp.locator('[data-continue]').getAttribute('data-language'),'th');await bp.locator('[data-language=en]').first().click();assert.ok(bp.url().endsWith('/en/'));ok('Blocked preference storage','browser suggestion and static language links work');await blocked.close();
  await page.emulateMedia({reducedMotion:'reduce'});await page.goto(BASE+'en/');assert.equal(await page.evaluate(()=>getComputedStyle(document.documentElement).scrollBehavior),'auto');ok('Reduced motion','smooth scrolling disabled');
  await page.keyboard.press('Tab');assert.equal(await page.evaluate(()=>document.activeElement.className),'skip');await page.keyboard.press('Enter');assert.ok(page.url().endsWith('#main'));ok('Keyboard skip navigation','first Tab reveals skip link, Enter reaches main');
  await page.goto(BASE+'en/support/');await page.locator('summary').first().focus();await page.keyboard.press('Enter');assert.equal(await page.locator('details').first().getAttribute('open'),'');ok('Keyboard support disclosure','native details opened with Enter');
  for(const [name,viewport,route] of [['desktop',{width:1440,height:1000},'en/'],['mobile',{width:390,height:844},'th/'],['tablet',{width:768,height:1024},'en/']]){await page.setViewportSize(viewport);await page.goto(BASE+route);await page.waitForLoadState('networkidle');await page.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=500){scrollTo(0,y);await new Promise(r=>setTimeout(r,50));}scrollTo(0,0)});await page.waitForTimeout(150);await page.screenshot({path:path.join(OUT,'Oonmoon-'+name+'-preview.png'),fullPage:true});ok('Preview '+name,viewport);}
  assert.equal(bad.length,0,JSON.stringify(bad));ok('Browser console and responses','no page errors or failed responses');
  await context.close();
 }catch(error){report.errors.push(String(error.stack||error));process.exitCode=1;}
 finally{await browser.close();report.finished=new Date().toISOString();fs.writeFileSync(path.join(OUT,'browser-checks.json'),JSON.stringify(report,null,2));console.log(JSON.stringify({checks:report.checks.length,errors:report.errors,report:path.join(OUT,'browser-checks.json')},null,2));}
})();
