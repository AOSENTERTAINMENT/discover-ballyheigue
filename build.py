"""Discover Ballyheigue — modern chic edition. Run: python3 build.py
Drone clips and poster frames live in assets/drone/."""
import os, html
from urllib.parse import quote

ROOT = os.path.dirname(os.path.abspath(__file__))
D = "assets/drone"

PAGES = [("index.html", "Home"), ("explore.html", "Things to do"), ("wild-atlantic-way.html", "Wild Atlantic Way"),
         ("gallery.html", "Gallery"), ("local.html", "Local")]

def maps(q): return "https://www.google.com/maps/search/?api=1&query=" + quote(q)
def img(f, alt=""): return f'<img src="{D}/{f}.jpg" alt="{html.escape(alt)}" loading="lazy">'
def vid(f, label, auto=True):
    a = 'autoplay ' if auto else ''
    return f'<video src="{D}/{f}.mp4" poster="{D}/{f}.jpg" {a}muted loop playsinline preload="{"metadata" if auto else "none"}" aria-label="{html.escape(label)}"></video>'

def head(title, desc, current):
    nav = "".join(f'<li><a href="{f}"{" aria-current=page" if f == current else ""}>{n}</a></li>' for f, n in PAGES)
    return f"""<!doctype html>
<html lang="en-IE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{D}/hero.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@500;600;700&family=Hanken+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23142321'/%3E%3Cpath d='M5 19c4-3 7-3 11 0s7 3 11 0' fill='none' stroke='%23A9C5BC' stroke-width='2.5' stroke-linecap='round'/%3E%3C/svg%3E">
</head>
<body>
<header class="head" id="top">
<a class="mark" href="index.html">Ballyheigue<span>Co. Kerry</span></a>
<button class="menu" aria-expanded="false" aria-controls="nav">Menu</button>
<nav aria-label="Main"><ul id="nav">{nav}</ul></nav>
</header>
<main>"""

FOOT = """</main>
<footer class="foot">
<div class="foot-in">
<p class="foot-word" aria-hidden="true">Ballyheigue</p>
<div class="foot-cols">
<p>A seaside village on the Wild Atlantic Way, 25 minutes from Tralee. Follow <a href="https://www.instagram.com/discoverballyheigue/" rel="noopener">@discoverballyheigue</a> for what's on.</p>
<ul><li><a href="explore.html">Things to do</a></li><li><a href="wild-atlantic-way.html">Wild Atlantic Way</a></li><li><a href="gallery.html">Gallery</a></li><li><a href="local.html">Local businesses</a></li></ul>
</div>
<p class="fine">Sample site. Aerial footage by AOS Entertainment. Details change, so check with each business before you travel.</p>
</div>
</footer>
<script>
const h=document.querySelector('.head'),m=document.querySelector('.menu'),n=document.getElementById('nav');
const s=()=>h.classList.toggle('solid',scrollY>40);addEventListener('scroll',s,{passive:true});s();
m.addEventListener('click',()=>{const o=h.classList.toggle('open');m.setAttribute('aria-expanded',o);m.textContent=o?'Close':'Menu'});
</script>
</body></html>"""

def page_hero(title, intro, media, cls=""):
    return f"""<section class="phero {cls}"><div class="phero-media">{media}</div>
<div class="phero-text"><h1>{title}</h1><p>{intro}</p></div></section>"""

def write(fname, body, title, desc):
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(head(title, desc, fname) + body + FOOT)

# ---------------- HOME ----------------
home = f"""
<section class="hero">
<div class="hero-media"><video autoplay muted loop playsinline preload="auto" poster="{D}/hero.jpg" aria-label="Drone footage over Ballyheigue Beach"><source src="{D}/hero.mp4" type="video/mp4"></video></div>
<p class="coords">52.39&deg; N, 9.83&deg; W</p>
<div class="hero-foot">
<h1>Ballyheigue</h1>
<div class="hero-side"><p>Three kilometres of Blue Flag sand, Atlantic sunsets and a proper Kerry welcome.</p><a class="link" href="explore.html">Start exploring</a></div>
</div>
</section>

<section class="intro grid">
<h2 class="c-statement">North Kerry's seaside village, on the edge of the Wild Atlantic Way.</h2>
<div class="c-copy">
<p class="lede">Ballyheigue sits on the north-west edge of Tralee Bay, where a long golden beach runs south towards Banna Strand and the land rises north into Kerry Head.</p>
<p>Come for a swim, a surf or a long walk on the sand. Stay for a pint in the village, a round of golf beside a castle and a sunset that turns the whole bay gold. Don't rush through on the way somewhere else. Give it a day or two.</p>
<dl class="facts"><div><dt>Blue Flag beach</dt><dd>3 km</dd></div><div><dt>From Tralee</dt><dd>25 min</dd></div><div><dt>From Shannon Airport</dt><dd>1 h 20</dd></div></dl>
</div>
</section>

<section class="plan">
<div class="sec-head"><h2>Plan your days</h2><p>Four ways into Ballyheigue, whatever the weather is doing.</p></div>
<div class="rail">
<a class="card" href="explore.html#beach">{img("09-shoreline")}<h3>The beach</h3><p>Swimming, surfing and the evening walk out to Black Rock.</p></a>
<a class="card" href="explore.html#kerry-head">{img("01-kerry-head")}<h3>Kerry Head</h3><p>Cliffs, quiet roads and 2,000-year-old forts on the coastal loop.</p></a>
<a class="card" href="wild-atlantic-way.html">{img("05-blaskets")}<h3>The Wild Atlantic Way</h3><p>Banna, Fenit, Ballybunion and Dingle, all within reach.</p></a>
<a class="card" href="local.html">{img("08-village-evening")}<h3>Eat, drink, stay</h3><p>Village pubs with music, a seaside café and beds by the beach.</p></a>
</div>
</section>

<section class="award">
<p class="award-big">Named Ireland's best beach.</p>
<p>Ballyheigue Beach topped the Irish list in the Condé Nast Traveller Readers' Choice Awards 2026.</p>
<a class="link" href="gallery.html">See it from the air</a>
</section>

<section class="fullband">
{vid("07-sunset", "Drone footage of the sun setting behind Kerry Head")}
<div class="fullband-text"><h2>Stay for sunset.</h2><p>The sun drops into the Atlantic behind Kerry Head. In midsummer it doesn't set until after 10pm, so there's time for dinner first.</p></div>
</section>"""
write("index.html", home, "Discover Ballyheigue | Blue Flag beach on the Wild Atlantic Way",
      "Plan a trip to Ballyheigue, Co. Kerry: a 3km Blue Flag beach, Atlantic sunsets, Kerry Head walks, golf, pubs and cafés on the Wild Atlantic Way.")

# ---------------- EXPLORE ----------------
gems = [
    ("beach", "Ballyheigue Beach", "hero", "Three kilometres of golden Blue Flag sand backed by dunes, looking out over Tralee Bay. Swim, surf, kayak or fish from the shore, with lifeguards in the bathing season, parking beside the beach and a playground across the road.", "Free, dog friendly, family friendly"),
    ("black-rock", "The Black Rock", "04-black-rock", "The local landmark at the end of the classic beach walk, about 5km there and back, and one of the best places to watch the Atlantic roll in.", "Walk"),
    ("kerry-head-drive", "Kerry Head coastal drive", "01-kerry-head", "A loop around the peninsula with ocean views at every bend, across to Banna Strand, Tralee Bay and the Dingle mountains. Drive it, cycle it or walk sections of it.", "Drive or cycle"),
    ("castle", "Ballyheigue Castle", "10-golf-village", "The striking ruin of the Crosbie family's mansion, standing above the village and the golf course.", "History, free"),
    ("casement", "Roger Casement monument", "06-long-beach", "A small green with a big view over the beach, commemorating one of the significant figures of Irish history. Bring a coffee.", "History, free"),
    ("sauna", "Seaside sauna", "03-waves", "Warm up after a sea swim with a sauna session overlooking the beach. Heat, a cold plunge in the Atlantic, repeat.", "Wellness, book ahead"),
    ("golf", "Ballyheigue Castle Golf Club", "02-village", "Nine holes around the 18th-century castle, with views over the beach to the Brandon mountains. Visitors welcome.", "Golf"),
    ("pubs", "The local pubs", "08-village-evening", "A warm welcome, a good pint and music nights in high season. After a day on the beach, there's nowhere better.", "Live music, food"),
    ("amusements", "Ballyheigue Amusements", "09-shoreline", "A nostalgic seaside favourite on the front that's been part of summer holidays here for generations.", "Kids, rainy days"),
    ("kerry-head", "Kerry Head walking trails", "07-sunset", "Cliffs, quiet country lanes and the Cahercarbery forts, thought to be over 2,000 years old. Ballyheigue is also the end of the 48km North Kerry Way from Tralee.", "Walk, heritage"),
]
rows = "".join(
    f'<li class="gem" id="{i}"><figure>{img(f, t)}</figure><div class="gem-text"><span class="gem-n">{n:02d}</span><h3>{t}</h3><p>{d}</p><p class="tagline">{tags}</p></div></li>'
    for n, (i, t, f, d, tags) in enumerate(gems, 1))
explore = page_hero("Things to do", "Ten local favourites, picked by the people who live here.", img("04-black-rock"))
explore += f"""<section class="wrap-narrow"><ol class="gems">{rows}</ol></section>
<section class="three">
<div><h3>Rainy day</h3><p>Head for the amusements, warm up in the sauna or settle into a pub. Tralee's Kerry County Museum is 25 minutes away, and Banna Leisure Centre down the road has an indoor pool.</p></div>
<div><h3>What's on</h3><p>July brings the Ballyheigue Summer Festival and Races. In late summer the village fills for the Pattern, a three-day festival with deep local roots.</p></div>
<div><h3>Fishing</h3><p>Bass, flounder and turbot from the beach; pollock and mackerel off the Kerry Head rocks, with real care. Sea angling charters run from Fenit.</p></div>
</section>"""
write("explore.html", explore, "Things to do in Ballyheigue | Discover Ballyheigue",
      "Ten local favourites in Ballyheigue, Co. Kerry: the Blue Flag beach, Black Rock, Kerry Head, the castle, golf, sauna, pubs and more.")

# ---------------- WILD ATLANTIC WAY ----------------
stops = [
    ("Ballybunion", "35 km north", "Cliff walks, sea stacks, a surf school and the famous links.", False),
    ("Ballyheigue", "You are here", "Blue Flag beach, Kerry Head and the end of the North Kerry Way.", True),
    ("Banna Strand", "8 km south", "Ten kilometres of dunes linking back to Ballyheigue. Surf lessons in summer.", False),
    ("Ardfert Cathedral", "10 km", "Medieval cathedral ruins and one of Kerry's oldest Christian sites.", False),
    ("Fenit", "20 km", "Harbour village with a lighthouse, sailing and sea angling charters.", False),
    ("Tralee", "25 min", "Kerry's county town, with the museum, shops, restaurants and the train.", False),
    ("The Dingle Peninsula", "About an hour", "Inch, Castlegregory, the Conor Pass and Dingle town.", False),
]
st = "".join(f'<li{" class=here" if h else ""}><h3>{n}</h3><p>{t}</p><span>{d}</span></li>' for n, d, t, h in stops)
waw = page_hero("The Wild Atlantic Way", "Your base for the quieter northern stretch of Ireland's great coastal route.", img("01-kerry-head"))
waw += f"""<section class="split-sticky">
<div class="sticky">
<h2>Base yourself here, explore the coast.</h2>
<p class="lede">Kerry has the longest stretch of the Wild Atlantic Way. Ballyheigue sits in the middle of its quieter north.</p>
<p>Spend the morning on the beach, take the Kerry Head loop after lunch, and you're never more than an hour from Dingle or the cliffs at Ballybunion.</p>
<h3>The North Kerry Way</h3>
<p>A signposted 48km trail from Tralee to Ballyheigue. Walk it over two days, or pick up any section. The final stretch loops Kerry Head past Maulin Mountain and the Cahercarbery forts.</p>
<h3>Getting here</h3>
<p>On the R551, 25 minutes north-west of Tralee through Ardfert. Kerry Airport is about 40 minutes away, Shannon around 1 hour 20.</p>
</div>
<ol class="stops">{st}</ol>
</section>
<section class="three">
<div><h3>Pack layers</h3><p>Atlantic weather changes fast. A waterproof is never wasted, even in July.</p></div>
<div><h3>Swim between the flags</h3><p>Lifeguards cover the beach in the bathing season. Check the notice board on arrival.</p></div>
<div><h3>Book summer early</h3><p>Festival weeks fill the village, and the best beds go first.</p></div>
</section>"""
write("wild-atlantic-way.html", waw, "Ballyheigue on the Wild Atlantic Way | Discover Ballyheigue",
      "Use Ballyheigue as your base for the Wild Atlantic Way in Kerry: Banna Strand, Fenit, Ballybunion, the Dingle Peninsula and the North Kerry Way.")

# ---------------- GALLERY ----------------
GALLERY = [
    ("hero", "Atlantic waves rolling in to the village"), ("01-kerry-head", "Across the bay to the Dingle mountains"),
    ("02-village", "The village and beach from above"), ("07-sunset", "Sunset behind Kerry Head"),
    ("09-shoreline", "A walk at the water's edge"), ("03-waves", "Swimmers off the main beach"),
    ("10-golf-village", "The golf course and castle grounds"), ("05-blaskets", "Low tide, looking west"),
    ("08-village-evening", "Evening over the village"), ("04-black-rock", "Black Rock and the long strand"),
]
tiles = "".join(f'<figure class="shot">{vid(f, cap, auto=False)}<figcaption>{cap}</figcaption></figure>' for f, cap in GALLERY)
gal = page_hero("From the air", "Drone footage of Ballyheigue Beach, Kerry Head and Tralee Bay, by AOS Entertainment.", img("06-long-beach"))
gal += f"""<section class="wrap-wide">
<p class="hint">Hover or tap a clip to play it.</p>
<div class="masonry">{tiles}</div>
</section>
<section class="wrap-wide films">
<div class="sec-head"><h2>Summer 2026</h2><p>Two short films from July and August, shot by DJ Alan O'Sullivan.</p></div>
<div class="yt-grid">
<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/ldTgTLGFTjw" title="Ballyheigue Co Kerry July and August 2026" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/Pi_L-OiIuXM" title="Ballyheigue Co Kerry July 2026" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
</div>
<p class="hint">Share yours with #DiscoverBallyheigue or tag <a href="https://www.instagram.com/discoverballyheigue/" rel="noopener">@discoverballyheigue</a>.</p>
</section>
<script>
document.querySelectorAll('.shot').forEach(f=>{{const v=f.querySelector('video');const p=()=>v.play().catch(()=>{{}}),s=()=>v.pause();
f.addEventListener('mouseenter',p);f.addEventListener('mouseleave',s);f.addEventListener('click',()=>v.paused?p():s());}});
if(matchMedia('(hover: none)').matches&&!matchMedia('(prefers-reduced-motion: reduce)').matches){{
const io=new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting?e.target.play().catch(()=>{{}}):e.target.pause()),{{threshold:.6}});
document.querySelectorAll('.shot video').forEach(v=>io.observe(v));}}
</script>"""
write("gallery.html", gal, "Gallery and drone footage | Discover Ballyheigue",
      "Aerial drone footage of Ballyheigue Beach, Kerry Head and Tralee Bay in Co. Kerry.")

# ---------------- LOCAL ----------------
groups = [
    ("drink", "Pubs and bars", [
        ("Flahive's", "The village", "Lively village pub, highly rated for its atmosphere, music and friendly staff.", None, "Flahive's Ballyheigue"),
        ("O'Regan's Bar", "Main Street", "Long-established bar with a restaurant and function room. Great music nights.", None, "O'Regan's Bar Ballyheigue"),
        ("Kirby's Lounge", "The village", "Bar and restaurant known for good food, good beer and a friendly welcome.", None, "Kirby's Lounge Ballyheigue"),
        ("White Sands Hotel bar", "Main Street", "Hotel bar opposite the beach, with evening entertainment in summer.", "https://www.whitesands.ie", "White Sands Hotel Ballyheigue"),
    ]),
    ("eat", "Cafés and food", [
        ("Tides Café", "Main Street", "Breakfast, brunch, lunch, speciality coffee and homemade treats. Dog friendly.", None, "Tides Cafe Ballyheigue"),
        ("The Peachy Bean", "Main Street", "Coffee shop for an early cup and a bite before the beach.", None, "The Peachy Bean Ballyheigue"),
        ("The Krusty Krub", "Main Street", "Family-friendly spot for casual food, open late.", None, "The Krusty Krub Ballyheigue"),
        ("The Sea Shell", "Top of the Street", "Fish and chips to eat on the seafront.", None, "The Sea Shell Ballyheigue"),
        ("Kebab Cottage", "The village", "Takeaway with a wide menu.", None, "Kebab Cottage Ballyheigue"),
        ("Tony's Ice Cream Van", "The seafront", "No trip to Ballyheigue is complete without a cone.", None, "Ballyheigue Beach"),
        ("Centra Ballyheigue", "Main Street", "Coffee, deli, ice cream and beach supplies.", None, "Centra Ballyheigue"),
    ]),
    ("do", "Things to do", [
        ("Ballyheigue Beach", "Buncurrig", "Blue Flag beach with parking, toilets, a playground and summer lifeguards.", "https://www.discoverireland.ie/kerry/ballyheigue-beach", "Ballyheigue Beach"),
        ("Ballyheigue Castle Golf Club", "Castle grounds", "Nine holes around the castle ruins. Visitors welcome.", "https://www.ballyheiguecastlegolfclub.com", "Ballyheigue Castle Golf Club"),
        ("Healing Heat Sauna", "Ballyheigue Beach", "Seaside sauna sessions, ideal after a sea swim.", None, "Healing Heat Sauna Ballyheigue"),
        ("Ballyheigue Amusements", "The seafront", "Games and attractions for families. A rainy-day saviour.", None, "Ballyheigue Amusements"),
        ("Roger Casement statue", "Above the beach", "A small green with a big view over the bay.", None, "Roger Casement Statue Ballyheigue"),
        ("Glenderry Souterrains", "Near the village", "Ancient underground passages, a few miles out.", None, "Glenderry Souterrains"),
    ]),
    ("stay", "Places to stay", [
        ("White Sands Hotel", "Main Street", "Family-run three-star hotel a minute from the beach, with a restaurant.", "https://www.whitesands.ie", "White Sands Hotel Ballyheigue"),
        ("O'Neill's B&B", "The village", "Highly rated B&B close to the beach and village.", None, "O'Neill's B&B Ballyheigue"),
        ("Bayview Glamping", "Ballyheigue", "Glamping with a view of the bay.", "https://bayviewglamping.com/", "Bayview Glamping Ballyheigue"),
        ("Casey's Caravan Park", "Ballyheigue", "Caravan park handy for the beach and village.", None, "Caseys Caravan Park Ballyheigue"),
        ("Kerry Holiday Village", "Ballyheigue", "Self-catering holiday homes for families and groups.", None, "Kerry Holiday Village Ballyheigue"),
    ]),
]
side = "".join(f'<li><a href="#{k}">{t}<span>{len(r)}</span></a></li>' for k, t, r in groups)
body = ""
for k, t, rows_ in groups:
    lis = "".join(
        f'<li><div class="biz"><h3>{n}</h3><span>{w}</span></div><p>{d}</p><div class="biz-links">'
        + (f'<a href="{u}" rel="noopener" target="_blank">Website</a>' if u else "")
        + f'<a href="{maps(q)}" rel="noopener" target="_blank">Directions</a></div></li>'
        for n, w, d, u, q in rows_)
    body += f'<section class="dir" id="{k}"><h2>{t}</h2><ul>{lis}</ul></section>'
local = page_hero("Local businesses", "Where to eat, drink, stay and play in Ballyheigue.", img("02-village"))
local += f"""<div class="directory">
<aside class="side"><nav aria-label="Categories"><ul>{side}</ul></nav>
<div class="getlisted"><h3>Run a business here?</h3><p>Send us your details on Instagram to get listed.</p><a class="link" href="https://www.instagram.com/discoverballyheigue/" rel="noopener" target="_blank">Message us</a></div></aside>
<div class="dir-main">{body}</div>
</div>"""
write("local.html", local, "Local businesses: pubs, cafés and places to stay | Discover Ballyheigue",
      "Find pubs, cafés, places to stay and things to do in Ballyheigue, Co. Kerry, with links and directions.")
print("Built 5 pages")
