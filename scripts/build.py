#!/usr/bin/env python3
"""Render complete bilingual HTML. No packages, app checkout or network needed."""
import argparse, json, html, posixpath, urllib.parse
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

ROOT=Path(__file__).resolve().parents[1]
PAGES=['','features','stories','support','privacy']
BOOKS=['red','golden','pigs','duckling','goldilocks','lionMouse','redHen','billyGoats','elves','gingerbread']
COMPANIONS=['red-primary','golden-primary','golden-hare','pigs-primary','duckling-primary','goldilocks-primary','lionMouse-primary','lionMouse-mouse','redHen-primary','billyGoats-primary','elves-primary','elves-shoemaker','gingerbread-primary']
def e(value): return html.escape(str(value),quote=True)
def rel(source,target):
    value=posixpath.relpath(target or '.',source or '.')
    return value+'/' if not Path(target).suffix else value
def render(config):
    content=json.loads((ROOT/'content.json').read_text())
    details=json.loads((ROOT/'privacy-support.json').read_text())
    dimensions={a['filename']:(a['output']['width'],a['output']['height']) for a in json.loads((ROOT/'assets/asset-provenance.json').read_text())['assets']}
    def imgdim(filename):
        w,h=dimensions[filename]
        return f'width="{w}" height="{h}"'
    base=(config.get('base_url') or 'https://example.invalid/oonmoon/').rstrip('/')+'/'
    public=bool(config.get('public_indexing') and config.get('base_url'))
    def absolute(path): return base+path
    def screen(source,stem,alt,caption='',priority=False):
        return f'''<figure class="app-screen"><a href="{rel(source,'assets/'+stem+'-1600.jpg')}" aria-label="{e(alt)}"><img src="{rel(source,'assets/'+stem+'-800.jpg')}" srcset="{rel(source,'assets/'+stem+'-800.jpg')} 800w, {rel(source,'assets/'+stem+'-1600.jpg')} 1600w" sizes="(max-width: 800px) 90vw, 580px" width="1600" height="736" alt="{e(alt)}" {'fetchpriority="high"' if priority else 'loading="lazy"'} decoding="async"></a>{f'<figcaption>{e(caption)}</figcaption>' if caption else ''}</figure>'''
    def header(lang,page,source,gateway=False):
        d=content[lang]; alternate='th' if lang=='en' else 'en'
        nav=''.join(f'<a href="{rel(source,lang+"/"+p)}"'+(' aria-current="page"' if p==page and not gateway else '')+f'>{e(d["nav"][i])}</a>' for i,p in enumerate(PAGES))
        switch=''.join(f'<a href="{rel(source,l+"/"+page)}" lang="{l}" hreflang="{l}" data-language="{l}"'+(' aria-current="page"' if l==lang and not gateway else '')+f'>{label}</a>' for l,label in [('en','EN'),('th','ไทย')])
        return f'''<a class="skip" href="#main">{d['skip']}</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="{rel(source,lang)}"><img src="{rel(source,'assets/favicon.png')}" width="38" height="38" alt="">Oonmoon</a><nav class="nav" aria-label="{'Main navigation' if lang=='en' else 'เมนูหลัก'}">{nav}</nav><nav class="language-switch" aria-label="{'Language' if lang=='en' else 'ภาษา'}">{switch}</nav></div></header>'''
    def footer(lang,source):
        d=content[lang]
        links=''.join(f'<a href="{rel(source,lang+"/"+p)}">{d["nav"][PAGES.index(p)]}</a>' for p in ['stories','support','privacy'])
        return f'''<footer class="site-footer"><div class="wrap"><div class="footer-top"><div><a class="brand" href="{rel(source,lang)}">Oonmoon</a><p>{d['footer']}<br>{d['footerStatus']}</p></div><nav class="footer-links" aria-label="{'Footer navigation' if lang=='en' else 'เมนูท้ายหน้า'}">{links}<a href="mailto:pondd.me@gmail.com">pondd.me@gmail.com</a></nav></div><p class="credits">{d['credits']}</p>{f'<p class="preview-label">{d["previewNotice"]}</p>' if not public else ''}</div></footer>'''
    def head(lang,page,source,title,desc,gateway=False):
        canonical=absolute(source+'/') if source else base
        index='index,follow' if public else 'noindex,follow'
        en=absolute('en/'+(page+'/' if page else ''))
        th=absolute('th/'+(page+'/' if page else ''))
        fallback=base if not page else en
        return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="robots" content="{index}"><meta name="theme-color" content="#102c3d">
<link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="en" href="{en}"><link rel="alternate" hreflang="th" href="{th}"><link rel="alternate" hreflang="x-default" href="{fallback}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Oonmoon"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="{'th_TH' if lang=='th' else 'en_US'}"><meta property="og:locale:alternate" content="{'en_US' if lang=='th' else 'th_TH'}"><meta property="og:image" content="{absolute('assets/social-'+lang+'.jpg')}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{e(content[lang]['tagline'])}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{absolute('assets/social-'+lang+'.jpg')}"><meta name="twitter:image:alt" content="{e(content[lang]['tagline'])}">
<link rel="icon" href="{rel(source,'assets/favicon.png')}" type="image/png"><link rel="stylesheet" href="{rel(source,'assets/site.css')}"><script src="{rel(source,'assets/site.js')}" defer></script></head><body>'''
    def panorama(lang,source):
        alt="Moonlit paper forest with a crescent moon and glowing campfire" if lang=="en" else "ป่ากระดาษใต้แสงจันทร์ พร้อมพระจันทร์เสี้ยวและกองไฟ"
        return f'<figure class="panorama"><img src="{rel(source,"assets/forest-small.jpg")}" width="1000" height="435" alt="{alt}" loading="lazy" decoding="async"></figure>'
    def camp(lang,source):
        d=content[lang]
        figures=''.join(f'<img src="{rel(source,"assets/"+stem+".png")}" {imgdim(stem+".png")} alt="{e(d["campAlt"]+" "+d["storyTitles"][BOOKS.index(stem.split("-")[0])])}" decoding="async" loading="lazy">' for stem in COMPANIONS)
        return f'<figure class="camp"><div class="companions">{figures}</div><figcaption><strong>{d["campTitle"]}</strong> {d["campText"]}</figcaption></figure>'
    def cards(lang,limit=6,level=3):
        d=content[lang]
        return '<div class="feature-grid">'+''.join(f'<article class="feature-card"><span class="number">0{i+1}</span><h{level}>{e(h)}</h{level}><p>{e(t)}</p></article>' for i,(h,t) in enumerate(d['featureCards'][:limit]))+'</div>'
    def duo(lang):
        d=content[lang]
        return f'<section class="forest-section"><div class="wrap"><div class="duo-note"><h2>{d["duoHeading"]}</h2><p>{d["duoText"]}</p></div></div></section>'
    for lang,d in content.items():
        for i,page in enumerate(PAGES):
            source=lang+('/'+page if page else '')
            prefix=f'<main id="main">'
            if not page:
                body=f'''<section class="scene"><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow">{d['eyebrow']}</p><span class="status">{d['status']}</span><h1>{d['hero'][0]}<br>{d['hero'][1]}</h1><p class="intro">{d['intro']}</p><div class="actions"><a class="button" href="{rel(source,lang+'/stories')}">{d['explore']} →</a><a class="text-link" href="{rel(source,lang+'/features')}">{d['featuresLink']}</a></div></div><div class="hero-screen">{screen(source,'reader-'+lang,d['readerAlt'],d['screenCaption'],True)}</div></div>{panorama(lang,source)}{camp(lang,source)}</section>
<section class="paper"><div class="wrap"><div class="section-heading"><h2>{d['featureHeading']}</h2><p>{d['featureIntro']}</p></div>{cards(lang,3)}</div></section>
<section class="forest-section"><div class="wrap split"><div><h2>{d['libraryHeading']}</h2><p>{d['libraryIntro']}</p><div class="actions"><a class="button" href="{rel(source,lang+'/stories')}">{d['explore']} →</a></div></div>{screen(source,'shelf-en',d['shelfAlt'])}</div></section>{duo(lang)}'''
            else:
                key={'features':'feature','stories':'library','support':'support','privacy':'privacy'}[page]
                body=f'<section class="page-heading"><div class="wrap"><p class="eyebrow">Oonmoon · {d["status"]}</p><h1>{d[key+"Heading"]}</h1><p>{d[key+"Intro"]}</p></div></section>'
                if page=='features':
                    body+=f'<section class="paper"><div class="wrap">{cards(lang,level=2)}<div class="split" style="margin-top:60px">{screen(source,"dressing-girl-en",d["dressingAlt"])}{screen(source,"reader-"+lang,d["readerAlt"])}</div></div></section>'+duo(lang)
                elif page=='stories':
                    stories=''.join(f'''<article class="story-card"><img class="story-art" src="{rel(source,'assets/'+b+'-primary.png')}" {imgdim(b+'-primary.png')} alt="{e(d['campAlt']+' '+d['storyTitles'][j])}" loading="lazy" decoding="async"><span class="access {'full' if j>2 else ''}">{d['included'] if j<3 else d['fullLibrary']}</span><h2>{e(d['storyTitles'][j])}</h2><p>{e(d['storyNotes'][j])}</p></article>''' for j,b in enumerate(BOOKS))
                    body+=f'<section class="paper"><div class="wrap"><div class="story-grid">{stories}</div><p class="library-note">{d["libraryNote"]}</p></div></section>'
                elif page=='support':
                    faq=''.join(f'<details><summary>{e(row["question"])}</summary><p>{e(row["answer"])}</p></details>' for row in details[lang]['support'])
                    body+=f'<section class="paper"><div class="wrap reading-width"><p class="contact"><a href="mailto:pondd.me@gmail.com" aria-label="{d["emailLabel"]}">pondd.me@gmail.com</a></p><p class="contact-note">{d["emailNote"]}</p><div class="faq">{faq}</div></div></section>'
                elif page=='privacy':
                    sections=''.join(f'<section class="policy-section"><h2>{e(row["heading"])}</h2><p>{e(row["text"])}</p></section>' for row in details[lang]['privacy'])
                    heading="Platform privacy notices" if lang=="en" else "ข้อมูลความเป็นส่วนตัวของผู้ให้บริการ"
                    labels=["Apple Privacy Policy","App Store &amp; Privacy","GitHub Privacy Statement"] if lang=="en" else ["นโยบายความเป็นส่วนตัวของ Apple","App Store และความเป็นส่วนตัว","ประกาศความเป็นส่วนตัวของ GitHub"]
                    notices=f'<section class="policy-section"><h2>{heading}</h2><p><a href="https://www.apple.com/legal/privacy/en-ww/">{labels[0]}</a> · <a href="https://www.apple.com/legal/privacy/data/en/app-store/">{labels[1]}</a> · <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">{labels[2]}</a></p></section>'
                    body+=f'<section class="paper"><div class="wrap reading-width"><aside class="draft-note"><strong>{d["privacySummary"]}</strong><p>{d["privacySummaryText"]}</p></aside>{sections}{notices}</div></section>'
            directory=ROOT/source;directory.mkdir(parents=True,exist_ok=True)
            (directory/'index.html').write_text(head(lang,page,source,d['titles'][i],d['descriptions'][i])+header(lang,page,source)+prefix+body+'</main>'+footer(lang,source)+'</body></html>',encoding='utf-8')
    d=content['en'];source=''
    gateway=f'''<main id="main"><section class="scene gateway-scene"><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow">Read together · <span lang="th">อ่านด้วยกัน</span></p><span class="status">Coming soon · <span lang="th">เร็ว ๆ นี้</span></span><h1>Little stories.<br>Big wonder.</h1><p class="intro">Ten familiar tales, Thai and English narration, and a little world to explore together.</p><p class="gateway-intro-th" lang="th">นิทานคุ้นเคยสิบเรื่อง พร้อมเสียงบรรยายภาษาไทยและอังกฤษ และโลกเล็ก ๆ ให้สำรวจด้วยกัน</p><div class="gateway-card" data-language-gateway><h2>Choose your language · <span lang="th">เลือกภาษา</span></h2><div class="gateway-languages"><a href="en/" lang="en" hreflang="en" data-language="en" class="is-preferred">English</a><a href="th/" lang="th" hreflang="th" data-language="th">ไทย</a></div><a class="button" href="en/" data-continue>Continue in English →</a><p class="note" data-preference-note>English is the fallback. You can change language on every page.</p></div></div><div class="hero-screen">{screen(source,'reader-en',d['readerAlt'],d['screenCaption'],True)}</div></div>{panorama('en',source)}{camp('en',source)}</section></main>'''
    (ROOT/'index.html').write_text(head('en','','','Oonmoon — Thai & English storytime','Choose English or Thai and discover Oonmoon’s ten classic stories, recorded narration and character choices. Coming soon.',True)+header('en','','',True)+gateway+footer('en','')+'</body></html>')
    urls=['']+[l+'/'+(p+'/' if p else '') for l in ['en','th'] for p in PAGES]
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{xml_escape(absolute(u))}</loc></url>\n' for u in urls)+'</urlset>\n'
    (ROOT/'sitemap.xml').write_text(sitemap)
    (ROOT/'robots.txt').write_text('User-agent: *\n'+('Allow: /\nSitemap: '+absolute('sitemap.xml')+'\n' if public else 'Disallow: /\n# Local preview. Set the real base URL and enable public indexing before deployment.\n'))
    (ROOT/'.nojekyll').touch()
    print(json.dumps({'html_pages':len(urls),'base_url':base,'public_indexing':public,'privacy_owner_approved':config.get('privacy_owner_approved',False)}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--base-url');parser.add_argument('--public',action='store_true');parser.add_argument('--preview',action='store_true');args=parser.parse_args()
    config=json.loads((ROOT/'site.config.json').read_text())
    if args.base_url:
        parts=urllib.parse.urlsplit(args.base_url)
        if parts.scheme!='https' or not parts.hostname or parts.query or parts.fragment or parts.username: parser.error('Use an absolute HTTPS base URL, with the project subpath and without query, fragment or credentials.')
        config['base_url']=args.base_url.rstrip('/')+'/'
    if args.public:
        if not config.get('base_url') or '.invalid' in config['base_url']: parser.error('Configure the actual HTTPS site URL first.')
        config['public_indexing']=True
    if args.preview: config['public_indexing']=False
    (ROOT/'site.config.json').write_text(json.dumps(config,indent=2,ensure_ascii=False)+'\n')
    render(config)
