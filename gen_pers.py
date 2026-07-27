C="https://cdn.blossomflowerdelivery.com/wp-content/uploads"
logo=f"{C}/blososmlogo1.svg"
pays=["visa","mastercard","amex","discover","gpay","applepay","paypal"]
payimg="".join(f'<img src="{C}/{n}.png" alt="{n}">' for n in pays)

ROSE_REL=[("Unconditional Affections","64.99","69.99","15959/unconditional_affections-1-1-277x366.webp"),
 ("Scarlet Smooches","69.99","89.99","9251/scarlet_smooches-1-277x366.webp"),
 ("2 Dozen Roses","139.99","159.99","15704/2_dozen_roses-1-277x366.webp"),
 ("Garden Party","69.99","","15758/garden_party-1-1-277x366.webp"),
 ("3 Red Roses & Bear","59.99","79.99","15606/3-Red-Roses-and-bear-277x366.webp"),
 ("Brighten Up","69.99","89.99","15827/brighten_up-1-1-277x366.webp"),
 ("A Time for Remembrance","116.99","136.99","16096/a_time_for_remembrance_bouquet-1-1-277x366.webp"),
 ("Precious Pink","79.99","99.99","16333/precious_pink_nice-looking_bouquet-1-277x366.webp"),
 ("Luscious","114.99","","15724/luscious-1-277x366.webp"),
 ("Forever In Our Thoughts","69.95","","3250/forever_in_our_thoughts-1-1-277x366.webp"),
 ("Lemony Snicket","84.99","","16445/lemony_snicket-1-1-277x366.webp")]
CASKET_REL=[("Funeral Cover Casket - Medium","159.99","179.99","17141/funeral_cover_casket_-_medium-1-1-277x366.webp"),
 ("With Sympathy","333.99","353.99","17146/with_sympathy-1-1-277x366.webp"),
 ("Remembrance Casket Cover","349.00","","17160/remembrance_casket_cover-1-277x366.webp"),
 ("Eternal Rest Casket Spray","244.99","264.99","17149/eternal_rest_casket_spray-1-277x366.webp"),
 ("White Wonder Casket Cover","149.99","169.99","17136/white_wonder_casket_cover-1-1-277x366.webp"),
 ("Casket Spray","305.99","","17150/casket_spray-1-1-277x366.webp"),
 ("Radiant Remembrance Spray","109.99","129.99","17153/radiant_remembrance_spray-1-277x366.webp"),
 ("Elegant Remembrance","204.99","","17157/elegant_remembrance-1-1-277x366.webp")]

roses={"title":"Luxurious Roses","item":"15942","price":"79.99","old":"",
 "imgs":[f"{C}/v2/15942/luxurious_roses_charming_bouquet-{n}-1.webp" for n in [1,2,3,4]],
 "crumb":["Home","Flowers","Roses","Luxurious Roses"],
 "desc":"Welcome to our rose shop! Our beautiful flowers are a symbol of love and affection, and are sure to make your loved ones feel special. We offer a variety of colors and fragrances to choose from, so you can find the perfect bouquet for your special occasion.",
 "rel":ROSE_REL}
casket={"title":"Funeral Casket Cover","item":"17140","price":"159.99","old":"179.99",
 "imgs":[f"{C}/v2/17140/funeral_casket_cover-{n}.webp" for n in ["1-1","2-2","3-2","4-2"]],
 "crumb":["Home","Funeral Service","Casket Covers","Funeral Casket Cover"],
 "desc":"Looking to send flowers in memory of a loved one? Our funeral flowers assortment has the perfect mix of colors and styles to create a beautiful tribute that will comfort those close to you.",
 "rel":CASKET_REL}

def card(n,p,o,im):
    sale='<span class="sale">SALE</span>' if o else ''
    price=f'${p} <s>${o}</s>' if o else f'${p}'
    return f'<div class="card">{sale}<img loading="lazy" src="{C}/v2/{im}" alt="{n}"><div class="cn">{n}</div><div class="cst">&#9733;&#9733;&#9733;&#9733;&#9733;</div><div class="cp">{price}</div><button class="atc">ADD TO CART</button></div>'

def page(mode, pr):
    imgs=pr["imgs"]; thumbs="".join(f'<img src="{u}" class="th" alt="view">' for u in imgs)
    rel="".join(card(*x) for x in pr["rel"]); rel2="".join(card(*x) for x in pr["rel"][::-1])
    collage="".join(f'<img loading="lazy" src="{C}/v2/{im}" alt="">' for _,_,_,im in pr["rel"])
    crumb=" &frasl; ".join(pr["crumb"][:-1])+f' &frasl; <b>{pr["crumb"][-1]}</b>'
    pricehtml=f'${pr["price"]}'+(f' <s>${pr["old"]}</s>' if pr["old"] else '')
    A=lambda t:f'<div class="anno">{t}</div>' if mode!="original" else ''
    if mode=="original":
        bg='#e9e9e9';btitle='Оригинал';btext='Точная копия текущей страницы blossomflowerdelivery.com — как есть, без изменений.';bul=''
        eyebrow_html='';subhead='';delivery=''
        counters='<div class="count"><b>&#128065; 36 people are viewing this product right now</b><b>&#128293; 6 items sold in last 24 hours</b><span class="usd">*ALL PRICES ARE LISTED IN USD ($)</span></div>'
        flash='<span class="flash">Flash Sale: <span>21h 26m 49s</span></span>' if pr["old"] else ''
        seo=f'<h2 class="center-h">Description</h2><p style="max-width:80ch;margin:0 auto;">{pr["desc"]}</p>'
        faq=''
    elif mode=="general":
        bg='#fff6fb';btitle='Пример: ОБЩИЙ запрос';btext='Персонализация под запрос «same-day rose delivery» + город. NEW — что добавлено/изменено.'
        bul='<li><b>Eyebrow + H1-подзаголовок</b> под тип запроса и город.</li><li><b>Строка доставки</b> с городом и cutoff.</li><li><b>SEO-блок</b> под розы/повод.</li><li><b>FAQ</b> + FAQPage JSON-LD.</li><li>Title/meta под ?type=&city=. Промо можно оставить.</li><li>Не трогать цену/товар/фото/кнопку.</li>'
        eyebrow_html=A('NEW — eyebrow под тип запроса')+'<span class="eyebrow">Fresh Roses · Same-Day Delivery</span>'
        subhead=A('NEW — H1-подзаголовок под тип запроса + город')+'<div class="subhead">Same-Day Rose Delivery in Houston, TX</div>'
        delivery=A('NEW — строка доставки под запрос')+'<div class="deliv">&#128205; Same-day rose delivery available across <b>Houston, TX</b> — order before the local cutoff and it arrives today.</div>'
        counters='<div class="count"><b>&#128065; 36 people are viewing this product right now</b><b>&#128293; 6 items sold in last 24 hours</b><span class="usd">*ALL PRICES ARE LISTED IN USD ($)</span></div>'
        flash='<span class="flash">Flash Sale: <span>21h 26m 49s</span></span>' if pr["old"] else ''
        seo='<h2 class="center-h">Description</h2>'+A('NEW — персонализированный SEO-блок под розы/same-day')+'<div class="pers"><p>Send fresh, hand-arranged roses anywhere in Houston with same-day delivery. Our network of local florists prepares each bouquet to order and delivers it the same day when placed before the local cutoff — perfect for birthdays, anniversaries and romantic moments.</p><p>Choose from classic red, pink and mixed rose bouquets. With more than 5,000 reviews on Google, Blossom is a trusted choice for rose delivery in Houston and nationwide.</p></div>'
        faq=A('NEW — FAQ под запрос + FAQPage JSON-LD')+'<div class="faq"><details open><summary>Can I get roses delivered today in Houston?</summary><p>Yes — order before the local cutoff time and same-day delivery is available for most Houston addresses.</p></details><details><summary>How late can I order for same-day rose delivery?</summary><p>Same-day cutoff varies by area; the available dates shown at checkout reflect the latest option for your ZIP.</p></details><details><summary>What rose colors can I choose?</summary><p>Red, pink, white and mixed seasonal roses are available depending on the arrangement.</p></details></div>'
    else:
        bg='#fff6fb';btitle='Пример: FUNERAL';btext='Персонализация под funeral/casket — сдержанный тон, доставка в funeral home. NEW — что добавлено/изменено.'
        bul='<li><b>Eyebrow + H1-подзаголовок</b> funeral + город.</li><li><b>Строка доставки</b> в funeral home к времени службы.</li><li><b>SEO-блок</b> уважительный.</li><li><b>FAQ</b> funeral + FAQPage JSON-LD.</li><li class="rm">Убрать: Flash Sale, «viewing», «sold in 24h».</li><li>Тон: без today/surprise/скидок.</li>'
        eyebrow_html=A('NEW — eyebrow под тип запроса')+'<span class="eyebrow">Funeral &amp; Sympathy · Casket Sprays</span>'
        subhead=A('NEW — H1-подзаголовок funeral + город')+'<div class="subhead">Funeral &amp; Sympathy Flowers in Houston, TX</div>'
        delivery=A('NEW — строка доставки под funeral')+'<div class="deliv">&#128205; Casket spray delivery to <b>funeral homes and residences in Houston, TX</b> — we coordinate timing around the service.</div>'
        counters='<div class="rmbox">Для funeral убрать: «36 people viewing», «6 sold in 24h», Flash Sale</div>'
        flash=''
        seo='<h2 class="center-h">Description</h2>'+A('NEW — персонализированный SEO-блок под funeral')+'<div class="pers"><p>A casket cover is one of the most meaningful tributes you can send. This full-length spray of fresh, seasonal blooms is prepared by our network of local florists and delivered with care to the funeral home or family residence in Houston, timed around the service.</p><p>Blossom coordinates funeral and sympathy deliveries across Houston — casket sprays, standing sprays, wreaths and sympathy arrangements. With more than 5,000 reviews on Google, families trust us to handle these orders thoughtfully.</p></div>'
        faq=A('NEW — funeral FAQ + FAQPage JSON-LD')+'<div class="faq"><details open><summary>Can you deliver a casket cover to a funeral home in Houston?</summary><p>Yes. Select "Funeral home" as the recipient location; we coordinate delivery timing with the funeral home around the service.</p></details><details><summary>Will the arrangement arrive before the service?</summary><p>We prioritize funeral deliveries and time them around the service.</p></details><details><summary>What message is appropriate on the card?</summary><p>Short, sincere messages work best — e.g. "With deepest sympathy" or "In loving memory."</p></details></div>'
    demoblock=f'<div class="demo" style="background:{bg}"><div class="in"><h3>&#127800; {btitle} — {pr["title"]}</h3><p>{btext}</p>'+(f'<ul>{bul}</ul>' if bul else '')+'</div></div>'
    nav=[('original','Оригинал'),('general','Общий запрос'),('funeral','Funeral')]
    switch="".join(f'<a href="{m}.html" class="sw {"on" if m==mode else ""}">{t}</a>' for m,t in nav)
    eyebrow_block=eyebrow_html if mode!='original' else ''
    return PAGE_TMPL(pr,mode,switch,demoblock,logo,thumbs,imgs,crumb,eyebrow_block,subhead,counters,pricehtml,flash,delivery,seo,faq,rel,rel2,collage,payimg)

def PAGE_TMPL(pr,mode,switch,demoblock,logo,thumbs,imgs,crumb,eyebrow_block,subhead,counters,pricehtml,flash,delivery,seo,faq,rel,rel2,collage,payimg):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{pr['title']} — Blossom ({mode})</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='14' font-size='14'>&#127800;</text></svg>">
<style>
:root{{--pink:#E5167F;--pink-d:#c00e6b;--ink:#2b2b2b;--muted:#8a8a8a;--line:#eaeaea;--soft:#f7f7f7;}}
*{{box-sizing:border-box;margin:0;padding:0;}} body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:#fff;line-height:1.5;font-size:14px;}}
img{{max-width:100%;display:block;}} s{{color:#b3b3b3;font-weight:400;}}
.switch{{position:sticky;top:0;z-index:50;background:#1f1f1f;display:flex;gap:6px;justify-content:center;padding:8px;}}
.sw{{color:#ccc;text-decoration:none;font-size:12px;font-weight:700;padding:6px 16px;border-radius:20px;}} .sw.on{{background:var(--pink);color:#fff;}}
.demo{{border-bottom:2px solid var(--pink);}} .demo .in{{max-width:1180px;margin:0 auto;padding:14px 20px;}}
.demo h3{{font-size:15px;color:var(--pink-d);margin-bottom:6px;}} .demo p{{font-size:12.5px;color:#555;margin-bottom:6px;}}
.demo ul{{padding-left:18px;font-size:12.5px;color:#444;column-count:2;column-gap:34px;}} .demo li{{margin:3px 0;break-inside:avoid;}} .demo .rm{{color:#c0142f;}}
.badge{{display:inline-block;font-size:9px;font-weight:700;color:#fff;background:#0a8f43;padding:2px 6px;border-radius:3px;vertical-align:middle;margin-left:6px;}}
.anno{{font-size:11.5px;color:#0a7a3a;background:#eefaf2;border-left:3px solid #0a8f43;padding:5px 9px;margin:6px 0;border-radius:0 4px 4px 0;}}
.rmbox{{font-size:11.5px;color:#c0142f;background:#fdeef2;border-left:3px solid var(--pink);padding:5px 9px;margin:6px 0;border-radius:0 4px 4px 0;}}
.util{{border-bottom:1px solid var(--line);font-size:12px;color:var(--muted);}} .util .in{{max-width:1180px;margin:0 auto;display:flex;justify-content:space-between;padding:8px 20px;}} .util .r{{display:flex;gap:20px;}}
.head{{max-width:1180px;margin:0 auto;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:24px;padding:16px 20px;}}
.search{{display:flex;max-width:340px;border:1px solid #ddd;border-radius:4px;overflow:hidden;}} .search input{{border:0;padding:9px 12px;flex:1;font-size:13px;outline:none;}} .search button{{border:0;background:var(--pink);color:#fff;padding:0 15px;font-size:15px;}}
.logo{{height:58px;margin:0 auto;}} .contact{{font-size:12px;color:var(--muted);text-align:right;}}
.nav{{background:var(--soft);border-top:1px solid var(--line);border-bottom:3px solid var(--pink);}} .nav .in{{max-width:1180px;margin:0 auto;display:flex;justify-content:center;gap:30px;padding:13px;font-size:13px;font-weight:700;}}
.crumb{{max-width:1180px;margin:0 auto;font-size:12px;color:var(--muted);padding:14px 20px;}} .crumb b{{color:var(--ink);font-weight:500;}}
.prod{{max-width:1180px;margin:0 auto;display:grid;grid-template-columns:460px 1fr;gap:40px;padding:4px 20px 26px;}}
@media(max-width:820px){{.prod{{grid-template-columns:1fr;}}.head{{grid-template-columns:1fr;}}.demo ul{{column-count:1;}}}}
.gal>img{{border:1px solid var(--line);border-radius:4px;}} .dlf{{text-align:center;color:#0a8f43;font-size:13px;margin:8px 0;}}
.thwrap{{display:flex;align-items:center;gap:8px;justify-content:center;}} .thwrap .arr{{color:#bbb;font-size:20px;cursor:pointer;}}
.th{{width:80px;height:80px;object-fit:cover;border:1px solid var(--line);border-radius:4px;cursor:pointer;}}
.eyebrow{{display:inline-block;font-size:12px;font-weight:600;color:var(--pink-d);background:#fce8f2;padding:5px 12px;border-radius:20px;}}
.subhead{{font-size:14px;color:var(--pink-d);font-weight:600;margin:8px 0 0;}}
h1.p{{font-size:30px;font-weight:800;margin:8px 0 3px;text-transform:uppercase;}} .item{{font-size:12px;color:var(--muted);}}
.stars{{color:#f5a623;font-size:15px;margin:8px 0;}} .stars small{{color:#555;margin-left:6px;font-size:12px;}}
.count{{font-size:12.5px;color:#444;margin:4px 0;display:flex;flex-direction:column;gap:3px;}} .count b{{font-weight:400;}} .usd{{color:var(--muted);font-size:11px;}}
.priceline{{display:flex;align-items:center;gap:14px;margin:10px 0;}} .price{{font-size:26px;font-weight:800;}} .flash{{color:var(--pink);font-size:13px;font-weight:700;}} .flash span{{font-weight:800;}}
.deliv{{background:#f4fbf6;border-left:3px solid #0a8f43;padding:11px 14px;margin:6px 0;font-size:14px;color:#14503a;border-radius:0 4px 4px 0;}}
.hr{{border-top:1px solid var(--line);margin:12px 0;}}
.field{{margin:12px 0;display:grid;grid-template-columns:210px 1fr;align-items:center;gap:12px;max-width:560px;}} .field label{{font-size:12px;font-weight:600;}} .field label b{{color:var(--pink);}} .field select,.field input{{padding:10px;border:1px solid #c9c9c9;border-radius:4px;font-size:13px;width:100%;}}
.cta{{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;max-width:560px;background:var(--pink);color:#fff;border:0;padding:15px;font-size:15px;font-weight:700;border-radius:4px;margin-top:14px;cursor:pointer;}} .cta:hover{{background:var(--pink-d);}}
.disc{{border:1px solid var(--line);border-radius:4px;padding:12px 14px;margin-top:14px;font-size:13px;color:#555;max-width:560px;}}
.center-h{{text-align:center;font-size:24px;font-weight:400;color:#444;margin:16px 0 14px;}}
.sec{{max-width:1180px;margin:0 auto;padding:14px 20px;}} .pers{{border:1px dashed #0a8f43;border-radius:8px;padding:16px 18px;background:#f7fcf9;max-width:900px;margin:0 auto;}} .pers p{{margin-bottom:8px;}}
.rowhd{{max-width:1180px;margin:24px auto 10px;padding:0 20px;display:flex;justify-content:space-between;align-items:center;}} .rowhd h2{{font-size:15px;font-weight:800;letter-spacing:.04em;}}
.viewall{{border:1px solid var(--line);background:#fafafa;font-size:11px;font-weight:700;padding:7px 14px;border-radius:3px;color:#555;}}
.carou{{max-width:1180px;margin:0 auto;padding:0 20px;display:flex;align-items:center;gap:8px;}} .carou .nav-a{{flex:0 0 30px;height:30px;border-radius:50%;border:1px solid var(--line);background:#fff;color:#999;display:flex;align-items:center;justify-content:center;cursor:pointer;}}
.row{{display:flex;gap:16px;overflow-x:auto;padding:6px 0 12px;flex:1;}} .card{{flex:0 0 200px;border:1px solid var(--line);border-radius:8px;padding:12px;text-align:center;position:relative;}}
.card img{{border-radius:5px;height:230px;object-fit:cover;width:100%;}} .sale{{position:absolute;top:6px;right:6px;background:#f5a623;color:#fff;font-size:9px;font-weight:700;padding:2px 7px;border-radius:3px;}}
.card .cn{{font-size:13px;font-weight:600;margin:9px 0 5px;min-height:34px;}} .card .cst{{color:#f5a623;font-size:12px;}} .card .cp{{font-size:15px;font-weight:800;margin:4px 0 8px;}}
.atc{{width:100%;background:var(--pink);border:0;color:#fff;font-size:11px;font-weight:700;padding:9px;border-radius:4px;}}
.faq details{{border-bottom:1px solid var(--line);padding:12px 0;}} .faq summary{{font-size:14px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;}} .faq summary::after{{content:"+";color:var(--pink);font-weight:700;}} .faq details[open] summary::after{{content:"\\2013";}} .faq details p{{margin-top:8px;font-size:13px;color:#555;}}
.collage{{max-width:1180px;margin:24px auto;padding:0 20px;display:grid;grid-template-columns:repeat(6,1fr);gap:8px;}} .collage img{{height:150px;width:100%;object-fit:cover;border-radius:3px;}}
@media(max-width:820px){{.collage{{grid-template-columns:repeat(3,1fr);}}.field{{grid-template-columns:1fr;}}}}
.foot{{background:#f4f4f4;border-top:1px solid var(--line);margin-top:20px;}} .foot .in{{max-width:1180px;margin:0 auto;padding:34px 20px;}} .fcols{{display:flex;flex-wrap:wrap;gap:60px;}} .foot h4{{font-size:12px;letter-spacing:.09em;margin-bottom:12px;}} .foot a{{color:#666;display:block;text-decoration:none;margin:5px 0;font-size:13px;}}
.pays{{display:flex;align-items:center;gap:30px;flex-wrap:wrap;margin-top:26px;padding-top:20px;border-top:1px solid #e0e0e0;}} .pays .grp{{display:flex;align-items:center;gap:10px;}} .pays .lbl{{font-size:11px;font-weight:700;color:#777;}} .pays img{{height:22px;}} .logo2{{height:52px;margin-bottom:16px;}}
.cpr{{text-align:center;font-size:12px;color:#888;padding:16px;border-top:1px solid #e0e0e0;}}
</style></head><body>
<div class="switch">{switch}</div>
{demoblock}
<div class="util"><div class="in"><span>Blossom Flower Delivery</span><div class="r"><span>Shop</span><span>My Orders</span><span>Call Us : (877) 861-7986</span><span>PIN: B7602</span></div></div></div>
<div class="head"><div class="search"><input placeholder="Search entire store here..."><button>&#9906;</button></div><img class="logo" src="{logo}" alt="the Blossom"><div class="contact">Call Us : (877) 861-7986<br>service@blossomflowerdelivery.com</div></div>
<div class="nav"><div class="in"><span>BIRTHDAY</span><span>OCCASIONS</span><span>FLOWERS</span><span>ROSES</span><span>FUNERAL &amp; SYMPATHY</span><span>PLANTS</span></div></div>
<div class="crumb">{crumb}</div>
<div class="prod">
  <div class="gal"><img id="main" src="{imgs[0]}" alt="{pr['title']}"><div class="dlf">Delivered by a local florist</div><div class="thwrap"><span class="arr">&#8249;</span>{thumbs}<span class="arr">&#8250;</span></div></div>
  <div class="buy">
    {eyebrow_block}
    {subhead}
    <h1 class="p">{pr['title']}</h1>
    <div class="item">Item #: {pr['item']}</div>
    <div class="stars">&#9733;&#9733;&#9733;&#9733;&#189;<small>(13 customer reviews)</small></div>
    {counters}
    <div class="priceline"><span class="price">{pricehtml}</span>{flash}</div>
    {delivery}
    <div class="hr"></div>
    <div class="field"><label>SELECT RECIPIENTS LOCATION <b>*</b></label><select><option>- Select Location Type -</option><option>Funeral home</option><option>Residence</option><option>Church</option><option>Hospital</option><option>Business</option></select></div>
    <div class="field"><label>ZIP/ POSTAL CODE <b>*</b></label><input></div>
    <div class="field"><label>PICK A DELIVERY DATE <b>*</b></label><input></div>
    <button class="cta">&#128722; CONTINUE TO SECURE CHECKOUT</button>
    <div class="disc">The <b>bouquet</b> you receive will have the same flowers and style as pictured, but since every arrangement is handmade, yours may look a <b>little different</b>.</div>
  </div>
</div>
<div class="sec">{seo}{faq}</div>
<div class="rowhd"><h2>CUSTOMERS ALSO CHOOSE</h2><span class="viewall">VIEW ALL</span></div>
<div class="carou"><span class="nav-a">&#8249;</span><div class="row">{rel}</div><span class="nav-a">&#8250;</span></div>
<div class="rowhd"><h2>PEOPLE ALSO BOUGHT</h2><span class="viewall">VIEW ALL</span></div>
<div class="carou"><span class="nav-a">&#8249;</span><div class="row">{rel2}</div><span class="nav-a">&#8250;</span></div>
<div class="collage">{collage}</div>
<div class="foot"><div class="in"><img class="logo2" src="{logo}" alt="the Blossom">
  <div class="fcols"><div><h4>COMPANY</h4><a>About Us</a></div><div><h4>ACCOUNT</h4><a>Manage Your Account</a></div><div><h4>HELP</h4><a>Customer Service</a><a>Delivery Policy</a><a>Refund Policy</a></div><div><h4>SITEMAP</h4><a>States</a><a>Cities</a></div><div><h4>CONTACT</h4><a>(877) 861-7986</a><a>service@blossomflowerdelivery.com</a></div></div>
  <div class="pays"><div class="grp"><span class="lbl">OUR PARTNERS</span><img src="{C}/fedex.png" alt="FedEx"><img src="{C}/ups.png" alt="UPS"></div><div class="grp"><span class="lbl">OUR PAYMENT METHODS</span>{payimg}</div></div>
</div><div class="cpr">Terms &amp; Conditions · Contact Us · Privacy Policy · ©2026 Blossom Flower Delivery · <b>Demo — not the live site</b></div></div>
<script>
document.querySelectorAll('.th').forEach(t=>t.addEventListener('click',()=>{{document.getElementById('main').src=t.src;}}));
document.querySelectorAll('.carou').forEach(c=>{{const r=c.querySelector('.row');c.querySelectorAll('.nav-a').forEach((a,i)=>a.addEventListener('click',()=>r.scrollBy({{left:i?420:-420,behavior:'smooth'}})));}});
</script></body></html>"""

open("pers-demo/original.html","w").write(page("original",roses))
open("pers-demo/general.html","w").write(page("general",roses))
open("pers-demo/funeral.html","w").write(page("funeral",casket))
print("regenerated 3 pages with REAL related products")
