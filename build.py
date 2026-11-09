"""Builds the five static pages. Run: python3 build.py
Drone footage: drop .mp4 files into assets/drone/ (hero.mp4 is used on the home page,
any others fill the gallery) and re-run. Without footage, illustrated scenes are used."""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
DRONE = os.path.join(ROOT, "assets", "drone")
clips = sorted(f for f in (os.listdir(DRONE) if os.path.isdir(DRONE) else []) if f.lower().endswith((".mp4", ".webm")))
stills = sorted(f for f in (os.listdir(DRONE) if os.path.isdir(DRONE) else []) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")))

PAGES = [
    ("index.html", "Home"),
    ("explore.html", "Things to do"),
    ("wild-atlantic-way.html", "Wild Atlantic Way"),
    ("gallery.html", "Gallery"),
    ("local.html", "Local businesses"),
]

LOGO = """<svg viewBox="0 0 40 40" aria-hidden="true"><defs><clipPath id="lc"><circle cx="20" cy="20" r="18"/></clipPath></defs>
<circle cx="20" cy="20" r="19.5" fill="#2B1055"/><g clip-path="url(#lc)"><rect width="40" height="40" fill="#FFD23F"/><rect y="17" width="40" height="23" fill="#FF8A3D"/><rect y="24" width="40" height="16" fill="#FF2E88"/>
<rect y="15" width="40" height="2" fill="#2B1055"/><rect y="21" width="40" height="2.5" fill="#2B1055"/><rect y="27" width="40" height="3" fill="#2B1055"/><rect y="32" width="40" height="8" fill="#00C2C7"/></g></svg>"""

def scene(variant=0, label="Illustrated sunset over Tralee Bay"):
    skies = [
        ("#FFD23F", "#FF2E88", "#FF8A3D", "#5B2A86"),
        ("#BFEFFF", "#7FD3F0", "#3DA9E8", "#5B2A86"),
        ("#FFD9A0", "#FF8A5C", "#C9518F", "#1B2F66"),
        ("#E6FBF7", "#9BE8DC", "#00C2C7", "#0B6E8A"),
    ]
    a, b, c, d = skies[variant % len(skies)]
    gid = f"sky{variant}"
    sun_y = [430, 170, 470, 210][variant % 4]
    return f"""<svg class="scene" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{html.escape(label)}">
<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{d}"/><stop offset=".45" stop-color="{c}"/><stop offset=".75" stop-color="{b}"/><stop offset="1" stop-color="{a}"/></linearGradient>
<linearGradient id="sea{variant}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5B2A86"/><stop offset="1" stop-color="#2B1055"/></linearGradient></defs>
<rect width="1600" height="620" fill="url(#{gid})"/>
<g class="sun"><circle cx="1080" cy="{sun_y}" r="110" fill="#FFF3C4" opacity=".95"/></g>
<path d="M0 560 L180 500 L320 520 L470 430 L600 470 L760 400 L900 455 L1040 520 L1600 540 L1600 620 L0 620Z" fill="#1B2F66" opacity=".55"/>
<path d="M0 590 L240 560 L420 575 L620 540 L860 570 L1100 585 L1600 575 L1600 620 L0 620Z" fill="#2B1055" opacity=".7"/>
<rect y="600" width="1600" height="300" fill="url(#sea{variant})"/>
<g fill="#FFF3C4" opacity=".55"><rect x="1030" y="625" width="100" height="5" rx="2"/><rect x="1010" y="650" width="140" height="4" rx="2"/><rect x="1045" y="680" width="70" height="4" rx="2"/><rect x="990" y="715" width="180" height="3" rx="2"/></g>
<path d="M0 780 C260 740 520 800 800 770 S1300 730 1600 760 L1600 900 L0 900Z" fill="#FFD23F"/>
<path d="M0 820 C300 790 600 840 900 815 S1350 790 1600 810 L1600 900 L0 900Z" fill="#FFE39A"/>
<path d="M0 772 C260 732 520 792 800 762 S1300 722 1600 752" fill="none" stroke="#FFFFFF" stroke-width="6" opacity=".8"/>
</svg>"""

def head(title, desc, current):
    nav = "".join(
        f'<li><a href="{f}"{" aria-current=\"page\"" if f == current else ""}>{n}</a></li>' for f, n in PAGES
    )
    return f"""<!doctype html>
<html lang="en-IE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Righteous&family=Work+Sans:wght@400;500;600;700&family=Permanent+Marker&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<link rel="icon" href="data:image/svg+xml,{LOGO.replace('#','%23').replace(chr(10),'').replace('"',"'")}">
</head>
<body>
<header class="site-head"><div class="wrap">
<a class="brand" href="index.html">{LOGO}Discover Ballyheigue</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<ul class="nav" id="nav">{nav}</ul>
</div></header>
<main>"""

FOOT = """</main>
<footer class="site-foot"><div class="wrap">
<div class="cols">
<div><h2>Stay for sunset.</h2><p>Ballyheigue, Co. Kerry, on the Wild Atlantic Way. Follow <a href="https://www.instagram.com/discoverballyheigue/" rel="noopener">@discoverballyheigue</a> for hidden gems, local favourites and what's on in the village.</p></div>
<div><ul><li><a href="index.html">Home</a></li><li><a href="explore.html">Things to do</a></li><li><a href="wild-atlantic-way.html">Wild Atlantic Way</a></li></ul></div>
<div><ul><li><a href="gallery.html">Gallery</a></li><li><a href="local.html">Local businesses</a></li><li><a href="https://www.instagram.com/discoverballyheigue/" rel="noopener">Instagram</a></li></ul></div>
</div>
<p class="small">Sample site. Aerial footage by AOS Entertainment. Opening hours and details change, so check with each business before you travel.</p>
</div></footer>
<script>
const b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
b.addEventListener('click',()=>{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);b.textContent=o?'Close':'Menu'});
</script>
</body></html>"""

WAVE_DOWN = lambda top, bottom: f'<svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true" style="background:{bottom}"><path d="M0 0h1440v20c-120 30-240 30-360 10S840 0 720 20 480 50 360 30 120 0 0 20z" fill="{top}"/></svg>'

def hero(title, tag, variant=0, small=False, buttons="", img=None):
    media = ""
    if not small and "hero.mp4" in clips:
        media = '<video autoplay muted loop playsinline preload="auto" poster="assets/drone/hero.jpg" aria-label="Drone footage over Ballyheigue Beach and Black Rock"><source src="assets/drone/hero.mp4" type="video/mp4"></video>'
    elif img and os.path.exists(os.path.join(DRONE, img)):
        media = f'<img class="scene" src="assets/drone/{img}" alt="">'
    else:
        media = scene(variant)
    return f"""<section class="hero{' small' if small else ''}"><div class="hero-media">{media}</div>
<div class="vhs" aria-hidden="true"><span class="rec">&#9654; PLAY</span><span class="stamp">SP&nbsp;&nbsp;JUL 26 1994</span></div>
<div class="wrap"><h1 class="retro" data-text="{html.escape(html.unescape(title).replace(chr(173),''))}">{title}</h1><p class="tag">{tag}</p>{buttons}</div>
{'' if small else '<div class="sticker" aria-hidden="true"><span>Greetings from</span><strong>Kerry!</strong></div>'}</section>"""

def write(fname, body, title, desc):
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(head(title, desc, fname) + body + FOOT)

def maps(q):
    from urllib.parse import quote
    return "https://www.google.com/maps/search/?api=1&query=" + quote(q)

# ---------------- HOME ----------------
home = hero("Bally&shy;heigue",
    "Three kilometres of Blue Flag sand, Atlantic sunsets and a proper Kerry welcome.",
    0, buttons='<div class="btn-row"><a class="btn btn-coral" href="explore.html">See things to do</a><a class="btn btn-ghost" href="local.html">Find a pub or café</a></div>')
home += f"""
<section><div class="wrap split">
<div>
<h2>North Kerry's seaside village, right on the Wild Atlantic Way.</h2>
<p class="lede">Ballyheigue sits on the north-west edge of Tralee Bay, where a long golden beach runs south towards Banna Strand and the land rises north into Kerry Head.</p>
<p>Come for a swim, a surf or a long walk on the sand. Stay for a pint in the village, a round of golf beside a castle and a sunset that turns the whole bay gold, pink and amber. Don't rush through on the way to somewhere else. Give Ballyheigue a day or two.</p>
<div class="facts">
<div><strong>3 km</strong><span>Blue Flag beach</span></div>
<div><strong>25 min</strong><span>from Tralee</span></div>
<div><strong>1 h 20</strong><span>from Shannon Airport</span></div>
</div>
</div>
<div class="route" style="background:var(--ink);color:var(--sand)">
<h3 style="font-size:2rem">Named Ireland's No. 1 beach</h3>
<p style="color:#E7D8FF">Ballyheigue Beach topped the Irish list in the Condé Nast Traveller Readers' Choice Awards 2026. Locals weren't surprised.</p>
<a class="btn btn-coral" href="gallery.html">See it from the air</a>
</div>
</div></section>
{WAVE_DOWN('#FFF3D6', '#5B2A86')}
<section class="band-atlantic"><div class="wrap">
<h2>Plan your days</h2>
<p class="lede">Four ways into Ballyheigue, whatever the weather is doing.</p>
<div class="postcards">
<a class="postcard pc-coral" href="explore.html#beach"><span class="go" aria-hidden="true">&#8599;</span><h3>The beach</h3><p>Swimming, surfing, kayaking and the evening stroll to Black Rock.</p></a>
<a class="postcard pc-gold" href="explore.html#kerry-head"><span class="go" aria-hidden="true">&#8599;</span><h3>Kerry Head</h3><p>Cliffs, quiet roads and 2,000-year-old forts on the coastal loop.</p></a>
<a class="postcard pc-foam" href="wild-atlantic-way.html"><span class="go" aria-hidden="true">&#8599;</span><h3>The Wild Atlantic Way</h3><p>Banna, Fenit, Ballybunion and the Dingle Peninsula, all within reach.</p></a>
<a class="postcard pc-thrift" href="local.html"><span class="go" aria-hidden="true">&#8599;</span><h3>Eat, drink, stay</h3><p>Pubs with music, a seaside café, ice cream on the front and beds by the beach.</p></a>
</div>
</div></section>
<section><div class="wrap split">
<div>
<h2>Time it for sunset.</h2>
<p class="lede">The sun drops into the Atlantic behind Kerry Head and the wet sand mirrors the whole sky.</p>
<p>In midsummer it doesn't set until after 10pm, so there's time for dinner first. Bring a jacket: Atlantic weather turns quickly, even in July.</p>
<a class="btn btn-coral" href="gallery.html">Watch the drone footage</a>
</div>
<div class="frame"><video class="scene" src="assets/drone/07-sunset.mp4" poster="assets/drone/07-sunset.jpg" autoplay muted loop playsinline preload="metadata" aria-label="Drone footage of the sun setting behind Kerry Head"></video></div>
</div></section>"""
write("index.html", home, "Discover Ballyheigue | Blue Flag beach on the Wild Atlantic Way",
      "Plan a trip to Ballyheigue, Co. Kerry: a 3km Blue Flag beach, Atlantic sunsets, Kerry Head walks, golf, pubs and cafés on the Wild Atlantic Way.")

# ---------------- EXPLORE ----------------
gems = [
    ("beach", "Ballyheigue Beach", "Three kilometres of golden Blue Flag sand backed by dunes, looking out over Tralee Bay. Swim, surf, kayak or fish from the shore, and look out for lifeguards in the bathing season. There's parking beside the beach and a playground across the road.", ["Free", "Dog friendly", "Family friendly"]),
    ("black-rock", "The Black Rock", "The local landmark at the end of the classic beach walk, and one of the best spots to watch the Atlantic waves roll in.", ["Walk", "Waves"]),
    ("kerry-head-drive", "Kerry Head coastal drive", "A loop around the peninsula with ocean views at every bend, across to Banna Strand, Tralee Bay and the Dingle mountains. Drive it, cycle it or walk sections of it.", ["Drive", "Cycle"]),
    ("castle", "Ballyheigue Castle", "The striking ruin of the Crosbie family's mansion, standing above the village and the golf course. A fine backdrop for photos.", ["History", "Free"]),
    ("casement", "Roger Casement monument", "A monument overlooking the Atlantic, commemorating one of the significant figures of Irish history.", ["History"]),
    ("sauna", "Seaside sauna", "Warm up after a sea swim with a sauna session overlooking the beach. Heat, a cold plunge in the Atlantic, repeat.", ["Wellness", "Book ahead"]),
    ("golf", "Ballyheigue Castle Golf Club", "Nine holes laid out around the 18th-century castle, with views over the beach to the Brandon mountains. Visitors welcome.", ["Golf", "Visitors welcome"]),
    ("pubs", "The local pubs", "A warm welcome, a good pint and trad sessions in high season. After a day on the beach, there's nowhere better.", ["Live music", "Food"]),
    ("amusements", "Ballyheigue Amusements", "A nostalgic seaside favourite that's been part of summer holidays here for generations. A good one for rainy days.", ["Kids", "Rainy day"]),
    ("kerry-head", "Kerry Head walking trails", "Dramatic cliffs, quiet country lanes and the Cahercarbery forts, thought to be over 2,000 years old. Ballyheigue is also the finishing point of the 48km North Kerry Way from Tralee.", ["Walk", "Heritage"]),
]
items = "".join(
    f'<li class="gem" id="{i}"><div><h3>{t}</h3><p>{d}</p><div class="meta">{"".join(f"<span class=chip>{c}</span>" for c in chips)}</div></div></li>'
    for i, t, d, chips in gems)
explore = hero("Things to do", "Ten local favourites, picked by the people who live here.", 1, small=True, img="04-black-rock.jpg")
explore += f"""<section><div class="wrap">
<h2>Ten reasons to stay longer</h2>
<p class="lede">Whether you're here for an afternoon or a week, start with these. Have a favourite we've missed? Tell us on Instagram.</p>
<ol class="gems">{items}</ol>
</div></section>
{WAVE_DOWN('#FFF3D6', '#2B1055')}
<section class="band-ink"><div class="wrap split">
<div><h2>Rainy day?</h2><p class="lede">It's Kerry. Have a plan B.</p>
<p>Head for the amusements, warm up in the sauna, settle into a pub or drive 20 minutes to Tralee for the Kerry County Museum and the leisure centres. Banna Leisure Centre, a couple of miles down the road, has an indoor pool.</p></div>
<div><h2>What's on</h2><p class="lede">Summer is festival season.</p>
<p>July brings the Ballyheigue Summer Festival and Races. In late summer the village fills for the Pattern, a three-day festival with deep local roots. Follow <a href="https://www.instagram.com/discoverballyheigue/" rel="noopener" style="color:var(--gold)">@discoverballyheigue</a> for dates.</p>
<h2 style="margin-top:1.4em">Fishing</h2><p class="lede">Bass, flounder and turbot from the beach.</p>
<p>The rocks on Kerry Head give pollock, mackerel and wrasse, but take real care there. Sea angling charters run from Fenit Marina, 10km across the bay.</p></div>
</div></section>"""
write("explore.html", explore, "Things to do in Ballyheigue | Discover Ballyheigue",
      "Ten local favourites in Ballyheigue, Co. Kerry: the Blue Flag beach, Black Rock, Kerry Head, the castle, golf, sauna, pubs and more.")

# ---------------- WILD ATLANTIC WAY ----------------
stops = [
    ("", "Ballybunion", "About 35 km north", "Cliff walks, sea stacks, a surf school on the south beach and the famous links."),
    ("here", "Ballyheigue", "You are here", "Blue Flag beach, Kerry Head and the end of the North Kerry Way."),
    ("", "Banna Strand", "About 8 km south", "Ten kilometres of dunes and sand linking right back to Ballyheigue. Surf lessons in summer."),
    ("", "Ardfert Cathedral", "About 10 km", "Medieval cathedral ruins and one of Kerry's oldest Christian sites."),
    ("", "Fenit", "About 20 km by road", "Harbour village with a lighthouse, sailing, sea angling charters and a beach café."),
    ("", "Tralee", "25 minutes", "Kerry's county town: museum, the Rose of Tralee, shops, restaurants and the train."),
    ("", "The Dingle Peninsula", "About an hour", "Inch, Castlegregory, the Conor Pass and Dingle town. A perfect day trip west."),
]
st = "".join(f'<li class="{c}"><h3>{n}</h3><span class="dist">{d}</span><p>{t}</p></li>' for c, n, d, t in stops)
waw = hero("The Wild Atlantic Way", "Ballyheigue is your base for Kerry's longest stretch of Ireland's great coastal route.", 3, small=True, img="01-kerry-head.jpg")
waw += f"""<section><div class="wrap split" style="align-items:start">
<div>
<h2>Base yourself here, explore the coast.</h2>
<p class="lede">Kerry has the longest stretch of the Wild Atlantic Way, and Ballyheigue sits right in the middle of its quieter northern half.</p>
<p>Spend the morning on the beach, take the Kerry Head loop after lunch, and you're never more than an hour from Dingle, Killarney or the cliffs at Ballybunion. Come back to the village for dinner and sunset.</p>
<h3 style="margin-top:2em">The North Kerry Way</h3>
<p>A signposted 48km walking trail from Tralee to Ballyheigue, joining the Dingle Way at its start. Walk it over two days, or pick up any section. The final stretch loops around Kerry Head past Maulin Mountain (218m) and the Cahercarbery forts.</p>
<h3 style="margin-top:2em">Getting here</h3>
<p>Ballyheigue is on the R551, 25 minutes north-west of Tralee through Ardfert. Kerry Airport is about 40 minutes away, Shannon around 1 hour 20 minutes. Trains and buses run to Tralee.</p>
</div>
<div class="route"><h3 style="font-size:1.8rem">Along the coast</h3><p style="color:var(--muted)">Approximate distances from Ballyheigue.</p><ol class="stops">{st}</ol></div>
</div></section>
{WAVE_DOWN('#FFF3D6', '#FF2E88')}
<section style="background:var(--coral);color:var(--paper)"><div class="wrap">
<h2>Good to know</h2>
<div class="postcards" style="margin-top:24px">
<div class="postcard" style="background:rgba(255,255,255,.14);min-height:0"><h3>Pack layers</h3><p>Atlantic weather changes fast. A waterproof is never wasted.</p></div>
<div class="postcard" style="background:rgba(255,255,255,.14);min-height:0"><h3>Swim between the flags</h3><p>Lifeguards cover the beach in the bathing season. Check the notice board.</p></div>
<div class="postcard" style="background:rgba(255,255,255,.14);min-height:0"><h3>Book summer early</h3><p>July brings the Ballyheigue Summer Festival and Races, and beds go fast.</p></div>
</div></div></section>"""
write("wild-atlantic-way.html", waw, "Ballyheigue on the Wild Atlantic Way | Discover Ballyheigue",
      "Use Ballyheigue as your base for the Wild Atlantic Way in Kerry: Banna Strand, Fenit, Ballybunion, the Dingle Peninsula and the North Kerry Way.")

# ---------------- GALLERY ----------------
GALLERY = [
    ("hero", "wide", "Atlantic waves rolling in to the village"),
    ("02-village", "", "The village and beach from above"),
    ("01-kerry-head", "tall", "Across the bay to the Dingle mountains"),
    ("03-waves", "", "Swimmers off the main beach"),
    ("10-golf-village", "", "The golf course and castle grounds"),
    ("07-sunset", "wide", "Sunset behind Kerry Head"),
    ("09-shoreline", "", "A walk at the water's edge"),
    ("05-blaskets", "", "Low tide, looking west"),
    ("08-village-evening", "", "Evening over the village"),
]
tiles = []
for i, (f, cls, cap) in enumerate(GALLERY):
    if f + ".mp4" in clips:
        inner = f'<video src="assets/drone/{f}.mp4" poster="assets/drone/{f}.jpg" muted loop playsinline preload="none" aria-label="Drone footage: {cap}"></video>'
    else:
        inner = scene(i, cap)
    tiles.append(f'<figure class="tile {cls}" style="margin:0">{inner}<figcaption>{cap}</figcaption></figure>')
gal = hero("From the air", "Drone footage of Ballyheigue Beach, Kerry Head and Tralee Bay.", 2, small=True, img="06-long-beach.jpg")
gal += f"""<section><div class="wrap">
<h2>Ballyheigue, seen differently</h2>
<p class="lede">The beach, the dunes and the Atlantic from a few hundred feet up. Aerial footage by AOS Entertainment. Hover or tap a clip to play it.</p>
<div class="gallery">{''.join(tiles)}</div>
<h2 style="margin-top:96px">Summer 2026 in Ballyheigue</h2>
<p class="lede">Two short films from July and August, shot by DJ Alan O'Sullivan.</p>
<div class="yt-grid">
<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/ldTgTLGFTjw" title="Ballyheigue Co Kerry July and August 2026" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/Pi_L-OiIuXM" title="Ballyheigue Co Kerry July 2026" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
</div>
<p style="margin-top:32px">Share your own photos with <strong>#DiscoverBallyheigue</strong> or tag <a href="https://www.instagram.com/discoverballyheigue/" rel="noopener">@discoverballyheigue</a> on Instagram.</p>
</div></section>"""
gal += """<script>
document.querySelectorAll('.tile video').forEach(v=>{
  const play=()=>{v.play().catch(()=>{})},stop=()=>v.pause();
  v.parentElement.addEventListener('mouseenter',play);v.parentElement.addEventListener('mouseleave',stop);
  v.parentElement.addEventListener('click',()=>v.paused?play():stop());
});
if(!matchMedia('(prefers-reduced-motion: reduce)').matches){
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(matchMedia('(hover: none)').matches){e.isIntersecting?e.target.play().catch(()=>{}):e.target.pause()}}),{threshold:.6});
  document.querySelectorAll('.tile video').forEach(v=>io.observe(v));
}
</script>"""
write("gallery.html", gal, "Gallery and drone footage | Discover Ballyheigue",
      "Aerial drone footage and photos of Ballyheigue Beach, Kerry Head and Tralee Bay in Co. Kerry.")

# ---------------- LOCAL ----------------
groups = [
    ("drink", "Pubs and bars", "#FF2E88", [
        ("Flahive's", "The village", "Lively village pub, highly rated on Google and Tripadvisor for its atmosphere, music and friendly staff.", None, "Flahive's Ballyheigue"),
        ("O'Regan's Bar", "Main Street", "Long-established bar with a restaurant and function room. Great music nights and a sunny-day favourite after the beach.", None, "O'Regan's Bar Ballyheigue"),
        ("Kirby's Lounge", "The village", "Bar and restaurant known for good food, good beer and a friendly welcome.", None, "Kirby's Lounge Ballyheigue"),
        ("White Sands Hotel bar", "Main Street", "Hotel bar opposite the beach, with evening entertainment in summer.", "https://www.whitesands.ie", "White Sands Hotel Ballyheigue"),
    ]),
    ("eat", "Cafés and food", "#FFD23F", [
        ("Tides Café", "Main Street", "Seaside café for breakfast, brunch, lunch, speciality coffee and homemade treats. Dog friendly and top-rated on Tripadvisor.", None, "Tides Cafe Ballyheigue"),
        ("The Peachy Bean", "Main Street", "Coffee shop for an early cup and a bite before the beach.", None, "The Peachy Bean Ballyheigue"),
        ("The Krusty Krub", "Main Street", "Family-friendly spot for casual food, open late.", None, "The Krusty Krub Ballyheigue"),
        ("The Sea Shell", "Top of the Street", "Chipper for fish and chips to eat on the seafront.", None, "The Sea Shell Ballyheigue"),
        ("Kebab Cottage", "The village", "Takeaway with a wide menu when you fancy something different.", None, "Kebab Cottage Ballyheigue"),
        ("Tony's Ice Cream Van", "The seafront", "A familiar sight on the front. No trip to Ballyheigue is complete without a cone.", None, "Ballyheigue Beach"),
        ("Centra Ballyheigue", "Main Street", "Shop and deli for coffee, ice cream, hot food and beach supplies.", None, "Centra Ballyheigue"),
    ]),
    ("do", "Attractions and activities", "#00C2C7", [
        ("Ballyheigue Beach", "Buncurrig", "Blue Flag beach with parking, toilets, a playground and lifeguards in season. Walk the 5km out to Black Rock and back.", "https://www.discoverireland.ie/kerry/ballyheigue-beach", "Ballyheigue Beach"),
        ("Ballyheigue Castle Golf Club", "Castle grounds", "Nine holes around the castle ruins, with views over the beach. Visitors welcome.", "https://www.ballyheiguecastlegolfclub.com", "Ballyheigue Castle Golf Club"),
        ("Healing Heat Sauna", "Ballyheigue Beach", "Seaside sauna sessions overlooking the beach, ideal after a sea swim.", None, "Healing Heat Sauna Ballyheigue"),
        ("Ballyheigue Amusements", "The seafront", "Games and attractions for children and families. A rainy-day saviour.", None, "Ballyheigue Amusements"),
        ("Roger Casement statue", "Above the beach", "A small green with a big view over the Blue Flag beach. Bring a coffee.", None, "Roger Casement Statue Ballyheigue"),
        ("Glenderry Souterrains", "Near the village", "Ancient underground passages a few miles out, for anyone curious about early Irish life.", None, "Glenderry Souterrains"),
    ]),
    ("stay", "Places to stay", "#FF8A3D", [
        ("White Sands Hotel", "Main Street", "Family-run three-star hotel a minute's walk from the beach, with family rooms and a restaurant.", "https://www.whitesands.ie", "White Sands Hotel Ballyheigue"),
        ("O'Neill's B&B", "The village", "Highly rated B&B close to the beach and village.", None, "O'Neill's B&B Ballyheigue"),
        ("Bayview Glamping", "Ballyheigue", "Five-star-reviewed glamping with a view of the bay.", "https://bayviewglamping.com/", "Bayview Glamping Ballyheigue"),
        ("Casey's Caravan Park", "Ballyheigue", "Caravan park handy for the beach and village.", None, "Caseys Caravan Park Ballyheigue"),
        ("Kerry Holiday Village", "Ballyheigue Holiday Village", "Self-catering holiday homes for families and groups.", None, "Kerry Holiday Village Ballyheigue"),
    ]),
]
filters = '<button type="button" aria-pressed="true" data-f="all">Everything</button>' + "".join(
    f'<button type="button" aria-pressed="false" data-f="{k}">{t}</button>' for k, t, _, _ in groups)
gh = ""
for k, t, col, rows in groups:
    lis = ""
    for name, where, desc, url, q in rows:
        links = (f'<a class="pill primary" href="{url}" rel="noopener" target="_blank">Website</a>' if url else "") + \
                f'<a class="pill" href="{maps(q)}" rel="noopener" target="_blank">Directions</a>'
        lis += f'<div class="listing"><div><h4>{name}</h4><span class="where">{where}</span><p>{desc}</p></div><div class="links">{links}</div></div>'
    gh += f'<div class="dir-group" data-g="{k}"><h3><span class="dot" style="background:{col}"></span>{t}</h3>{lis}</div>'
local = hero("Local businesses", "Where to eat, drink, stay and play in Ballyheigue.", 0, small=True, img="02-village.jpg")
local += f"""<section><div class="wrap">
<h2>Support local</h2>
<p class="lede">Pubs, cafés, places to stay and things to do in and around the village. Tap Directions to open Google Maps.</p>
<div class="dir-filter" role="group" aria-label="Filter businesses">{filters}</div>
{gh}
<div class="route" style="margin-top:64px;background:var(--atlantic);color:var(--paper)">
<h3 style="font-size:1.8rem">Run a business in Ballyheigue?</h3>
<p style="color:#F1E6FF">Get your pub, café, shop, accommodation or activity listed here. Send us a message on Instagram with your details.</p>
<a class="btn btn-coral" href="https://www.instagram.com/discoverballyheigue/" rel="noopener" target="_blank">Message us on Instagram</a>
</div>
</div></section>
<script>
document.querySelectorAll('.dir-filter button').forEach(b=>b.addEventListener('click',()=>{{
  document.querySelectorAll('.dir-filter button').forEach(x=>x.setAttribute('aria-pressed',x===b));
  const f=b.dataset.f;document.querySelectorAll('.dir-group').forEach(g=>g.hidden=!(f==='all'||g.dataset.g===f));
}}));
</script>"""
write("local.html", local, "Local businesses: pubs, cafés and places to stay | Discover Ballyheigue",
      "Find pubs, cafés, places to stay and things to do in Ballyheigue, Co. Kerry, with links and directions.")
print("Built 5 pages. Clips:", clips, "Stills:", stills)
