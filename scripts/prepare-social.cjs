// Compose marketing metadata from approved assets. App pixels stay unchanged.
const sharp=require('/Applications/ChatGPT.app/Contents/Resources/cua_node/lib/node_modules/sharp');
const fs=require('fs'),path=require('path');
const ROOT=path.resolve(__dirname,'..'),assets=path.join(ROOT,'assets');
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
(async()=>{
 const background=await sharp(path.join(assets,'forest.jpg')).resize(1200,630,{fit:'cover'}).toBuffer();
 const names=['red','golden','pigs','duckling','goldilocks','lionMouse','redHen','billyGoats','elves','gingerbread'];
 for(const lang of ['en','th']){
  const layers=[];
  layers.push({input:Buffer.from('<svg width="1200" height="630"><defs><linearGradient id="g"><stop stop-color="#102c3d" stop-opacity=".7"/><stop offset="1" stop-color="#102c3d" stop-opacity="0"/></linearGradient></defs><rect width="1200" height="630" fill="url(#g)"/></svg>'),top:0,left:0});
  const lines=lang==='en'?['Little stories.','Big wonder.']:['นิทานเล็ก ๆ','มหัศจรรย์ยิ่งใหญ่'];
  const text=`<svg width="1200" height="630"><g font-family="Thonburi, sans-serif" fill="#fbf4e5"><text x="60" y="95" font-size="36" font-weight="700">Oonmoon</text><text x="60" y="195" font-size="${lang==='en'?58:49}" font-weight="700">${esc(lines[0])}</text><text x="60" y="265" font-size="${lang==='en'?58:49}" font-weight="700">${esc(lines[1])}</text><text x="60" y="326" font-size="22" fill="#f4cf87">${lang==='en'?'Thai &amp; English storytime':'อ่านและฟังนิทานภาษาไทยและอังกฤษ'}</text><text x="60" y="380" font-size="19">${lang==='en'?'Coming soon':'เร็ว ๆ นี้'}</text></g></svg>`;
  layers.push({input:Buffer.from(text),left:0,top:0});
  const native=await sharp(path.join(assets,'reader-'+lang+'-1600.jpg')).resize(545).png().toBuffer();
  const {width,height}=await sharp(native).metadata();
  // Subtle presentation clip, matching the website. No border or app-asset edit.
  const mask=Buffer.from(`<svg width="${width}" height="${height}"><rect width="${width}" height="${height}" rx="8" ry="8" fill="white"/></svg>`);
  const screen=await sharp(native).ensureAlpha().composite([{input:mask,blend:'dest-in'}]).png().toBuffer();
  layers.push({input:screen,top:220,left:605});
  for(let i=0;i<names.length;i++){layers.push({input:await sharp(path.join(assets,names[i]+'-primary.png')).resize(105,105,{fit:'inside'}).toBuffer(),left:45+i*111,top:510});}
  await sharp(background).composite(layers).jpeg({quality:88,mozjpeg:true}).toFile(path.join(assets,'social-'+lang+'.jpg'));
 }
})();
