"""Generate the fourteen static pages. Run: python3 scripts/build_pages.py."""
from pathlib import Path
from html import escape
from product_content import PRODUCTS

ROOT = Path(__file__).resolve().parents[1]
CONTACT_URL = 'https://wa.me/5521966045167'
EMAIL = 'developer@mocatecnologia.com'
COPY = {
'pt': {
 'lang':'pt-BR','name':'Moca Tecnologia','skip':'Ir para o conteúdo','menu':'Menu','nav':['Soluções','Produtos','Projetos','Sobre'], 'contact':'Vamos conversar','other':'EN',
 'eyebrow':'Engenharia de software · Moca Tecnologia','headline':'Software bem pensado.<br><em>Negócios em movimento.</em>',
 'intro':'Criamos software sob medida e desenvolvemos nossos próprios produtos digitais. Técnica e criatividade, do primeiro desenho à próxima versão.',
 'cta':'Conte seu projeto','explore':'Explore nossos produtos','bottom':['Software sob medida + produtos próprios','Da ideia à evolução'],
 'solutions':'Duas frentes.<br>A mesma atenção ao produto.','solutions_intro':'Construir boas soluções começa por entender o que realmente precisa funcionar.',
 'custom':'Software sob medida','custom_desc':'Sistemas, aplicações web e integrações construídos para os desafios da sua empresa. Da experiência de uso à estrutura que sustenta a operação.',
 'tags':['Aplicações web','APIs e integrações','Sistemas de negócio'],
 'own':'Produtos próprios','own_desc':'Também colocamos nossas ideias em prática. Desenvolvemos produtos digitais com o mesmo cuidado que dedicamos a cada projeto.',
 'product_heading':'Ideias nossas.<br>Possibilidades para você.','product_desc':'A Moca também é um espaço para criar e desenvolver produtos próprios. Quer conhecer essa frente de trabalho? Acompanhe nossos projetos e novidades.',
 'product_link':'Acompanhe a Moca','product_note':'Criação, desenvolvimento e evolução.','product_caption':'Produtos digitais · Moca',
 'projects':'Tecnologia em projetos reais.','project_intro':'Conheça um dos projetos com participação da Moca.','project_type':'Projeto em colaboração','tooda_desc':'Uma iniciativa voltada à proteção e ao auxílio na localização de pessoas vulneráveis nas praias do Rio de Janeiro. Conheça a contribuição técnica da Moca e a apresentação da solução.',
 'view_project':'Conheça o projeto','all_projects':'Todos os projetos','process_title':'Da primeira conversa<br>à evolução do produto.',
 'steps':[('Entender','Conhecer o contexto, as pessoas e o problema a resolver.'),('Desenhar','Definir a experiência, a arquitetura e as prioridades.'),('Construir','Transformar decisões em software, com testes e entregas incrementais.'),('Evoluir','Aprender com o uso e orientar os próximos passos.')],
 'about_title':'Engenharia com<br>espaço para criar.','about_desc':'Somos a Moca Tecnologia. Combinamos desenvolvimento de sistemas, aplicações web e experiências interativas. Acreditamos em tecnologia que aproxima pessoas e transforma ideias em soluções úteis.',
 'contact_title':'O próximo projeto<br>começa com uma conversa.','contact_desc':'Um sistema para sua empresa ou uma ideia de produto? Vamos entender o que você quer construir.','contact_fallback':'Encontre a Moca no GitHub','footer':'Software, produtos e novas possibilidades.','back':'Voltar para projetos',
 'case_title':'TOODA.<br>Tecnologia a serviço do cuidado.','case_intro':'Conheça a solução e a participação técnica da Moca no projeto TOODA — Safe Children.',
 'docs':[('A contribuição da Moca','Visão técnica do projeto, abordagem de desenvolvimento e tecnologias utilizadas.','Ver apresentação técnica'),('TOODA — Safe Children','Apresentação da solução para proteção e auxílio na localização de pessoas vulneráveis nas praias do Rio de Janeiro.','Ver apresentação da solução')],
 'meta':'Software sob medida e produtos digitais próprios. Conheça a Moca Tecnologia, nossos projetos e nossa forma de construir soluções.'
},
'en': {
 'lang':'en','name':'Moca Technology','skip':'Skip to content','menu':'Menu','nav':['Solutions','Products','Projects','About'],'contact':'Let’s talk','other':'PT',
 'eyebrow':'Software engineering · Moca Technology','headline':'Thoughtful software.<br><em>Business in motion.</em>',
 'intro':'We build custom software and develop our own digital products. Engineering and creativity, from the first sketch to the next release.',
 'cta':'Tell us your idea','explore':'Explore our products','bottom':['Custom software + our own products','From idea to evolution'],
 'solutions':'Two paths.<br>The same care for the product.','solutions_intro':'Building useful solutions starts with understanding what really needs to work.',
 'custom':'Custom software','custom_desc':'Systems, web applications and integrations built around your business challenges. From the user experience to the foundations that support your operations.',
 'tags':['Web applications','APIs & integrations','Business systems'],
 'own':'Our own products','own_desc':'We put our own ideas into practice, too. We develop digital products with the same care we bring to every project.',
 'product_heading':'Our ideas.<br>New possibilities for you.','product_desc':'Moca is also a place to create and develop our own products. Interested in this side of our work? Follow our projects and updates.',
 'product_link':'Follow Moca','product_note':'Creation, development and evolution.','product_caption':'Digital products · Moca',
 'projects':'Technology in real projects.','project_intro':'Explore a project with Moca’s participation.','project_type':'Collaborative project','tooda_desc':'An initiative focused on protecting and helping locate vulnerable people on Rio de Janeiro’s beaches. Explore Moca’s technical contribution and the solution presentation.',
 'view_project':'Explore the project','all_projects':'All projects','process_title':'From the first conversation<br>to the next iteration.',
 'steps':[('Understand','Explore the context, the people and the problem to solve.'),('Design','Define the experience, architecture and priorities.'),('Build','Turn decisions into software, with testing and incremental delivery.'),('Evolve','Learn from real usage and shape the next steps.')],
 'about_title':'Engineering with<br>room to create.','about_desc':'We are Moca Technology. We combine systems development, web applications and interactive experiences. We believe in technology that connects people and turns ideas into useful solutions.',
 'contact_title':'The next project starts<br>with a conversation.','contact_desc':'A system for your business or a new product idea? Let’s understand what you want to build.','contact_fallback':'Find Moca on GitHub','footer':'Software, products and new possibilities.','back':'Back to projects',
 'case_title':'TOODA.<br>Technology that cares.','case_intro':'Explore the solution and Moca’s technical participation in TOODA — Safe Children.',
 'docs':[('Moca’s contribution','A technical overview of the project, development approach and technologies.','View technical presentation'),('TOODA — Safe Children','An introduction to the solution for protecting and helping locate vulnerable people on Rio de Janeiro’s beaches.','View solution presentation')],
 'meta':'Custom software and our own digital products. Discover Moca Technology, our projects and how we build useful solutions.'
}}

def products(locale,base):
 i=0 if locale=='pt' else 1
 action='Conheça o produto' if i==0 else 'Explore the product'
 cards=[]
 for slug,p in PRODUCTS.items():
  url=f'{base}products/{slug}/'
  cards.append(f'<article class="product-card"><a class="product-image {slug}" href="{url}" aria-label="{action}: {p["name"]}"><img src="{p["image"]}" alt="{p["name"]}" loading="lazy" width="460" height="260"></a><p class="eyebrow">{p["tag"][i]}</p><h3>{p["name"]}</h3><p>{p["intro"][i]}</p><a class="text-link" href="{url}">{action}<span aria-hidden="true">↗</span></a></article>')
 return ''.join(cards)


def product_body(locale, base, slug, link):
 p=PRODUCTS[slug];i=0 if locale=='pt' else 1
 back='Todos os produtos' if i==0 else 'All products'
 actions=''.join(link(url,label[i],'button' if n==0 else 'text-link') for n,(label,url) in enumerate(p['links']))
 features=''.join(f'<article><span class="number">0{n+1} /</span><h3>{title[i]}</h3><p>{text[i]}</p></article>' for n,(title,text) in enumerate(p['features']))
 gallery=''.join(f'<a href="{url}" aria-label="{alt[i]}"><img src="{url}" alt="{alt[i]}" loading="lazy" width="1200" height="675"></a>' for url,alt in p['gallery'])
 media=''
 if gallery: media=f'<section class="section"><div class="wrap"><p class="eyebrow">{"Dentro do jogo" if i==0 else "Inside the game"}</p><h2>{"Imagens de Dungeon Fighters" if i==0 else "Dungeon Fighters screenshots"}</h2><div class="product-gallery">{gallery}</div></div></section>'
 if p.get('video'): media=f'<section class="section"><div class="wrap"><p class="eyebrow">{"Vídeo de apresentação" if i==0 else "Presentation video"}</p><h2>Paper Hero</h2><iframe class="product-video" src="{p["video"]}" title="Paper Hero — {"vídeo de apresentação" if i==0 else "presentation video"}" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe><a class="text-link" href="https://www.youtube.com/watch?v=pX-UymX0gXg">{"Assistir no YouTube" if i==0 else "Watch on YouTube"} ↗</a></div></section>'
 if slug=='tooda':
  news='https://www.tupi.fm/rio/carnaval-2026-tera-60-mil-pulseiras-para-criancas-no-rj/'
  instagram='https://www.instagram.com/p/DVJw0mWFM-b/'
  media=f'''<section class="section"><div class="wrap field-story"><div><p class="eyebrow">{"TOODA na prática · Carnaval 2026" if i==0 else "TOODA in action · Carnival 2026"}</p><h2>{"Uma parceria para ampliar o cuidado." if i==0 else "A partnership to extend care."}</h2><p class="lead">{"A FIA-RJ fez uma parceria com a TOODA para utilizar as pulseiras de identificação no Carnaval. O vídeo mostra a aplicação das pulseiras e orientações de uso da plataforma." if i==0 else "FIA-RJ partnered with TOODA to use identification wristbands during Carnival. The video shows the wristbands being used and explains how to use the platform."}</p><p class="product-note">{"Vídeo em português, com legendas na imagem. Crédito: FIA-RJ / @fiarjoficial." if i==0 else "Video in Portuguese, with on-screen Portuguese captions. Credit: FIA-RJ / @fiarjoficial."}</p>{link(instagram,"Ver publicação no Instagram" if i==0 else "View Instagram post")}<div class="press-reference"><p class="eyebrow">{"Cobertura da ação" if i==0 else "Coverage of the initiative"}</p><h3>{"Carnaval 2026 terá 60 mil pulseiras para crianças no RJ" if i==0 else "Rio Carnival 2026 plans 60,000 identification wristbands for children"}</h3><p>{"Em 11 de fevereiro de 2026, a Super Rádio Tupi noticiou a ação SOS Folia da FIA-RJ. A previsão de 60 mil pulseiras refere-se ao total da ação anunciado na reportagem." if i==0 else "On February 11, 2026, Super Rádio Tupi reported on FIA-RJ’s SOS Folia initiative. The planned 60,000 wristbands refer to the initiative’s total announced in that report."}</p>{link(news,"Ler matéria na Tupi" if i==0 else "Read the Tupi article")}</div></div><figure class="field-video"><video controls playsinline preload="none" poster="/assets/media/tooda-fia-poster.png" aria-label="{"FIA-RJ: uso das pulseiras no Carnaval" if i==0 else "FIA-RJ: using wristbands during Carnival"}"><source src="/assets/media/tooda-fia-carnaval-2026.mp4" type="video/mp4"><a href="/assets/media/tooda-fia-carnaval-2026.mp4">{"Abrir vídeo" if i==0 else "Open video"}</a></video><figcaption>{"Registro da FIA-RJ · Trecho de 1 minuto" if i==0 else "FIA-RJ footage · One-minute excerpt"}</figcaption></figure></div></section>'''
 related=''.join(f'<a class="related-product" href="{base}products/{key}/">{item["name"]}<span aria-hidden="true">↗</span></a>' for key,item in PRODUCTS.items() if key!=slug)
 return f'''<section class="page-hero"><div class="wrap"><a class="breadcrumb" href="{base}#products">← {back}</a><div class="product-detail-hero"><div><p class="eyebrow">{p['tag'][i]}</p><h1>{p['name']}</h1><p class="lead">{p['intro'][i]}</p><div class="actions">{actions}</div>{'<p class="product-note">'+p['note'][i]+'</p>' if p.get('note') else ''}</div><img class="detail-cover" src="{p['image']}" alt="{p['name']}" width="1200" height="675"></div></div></section><section class="section light"><div class="wrap"><div class="split"><h2>{p['heading'][i]}</h2><p class="detail-description">{p['body'][i]}</p></div>{'<div class="product-features">'+features+'</div>' if features else ''}</div></section>{media}<section class="section light"><div class="wrap"><h2>{"Explore outros produtos" if i==0 else "Explore more products"}</h2><div class="related-products">{related}</div></div></section>'''

def page(locale, kind, slug=None):
 c=COPY[locale]; base='/pt/' if locale=='pt' else '/'; other='/' if locale=='pt' else '/pt/'
 suffix=f'products/{slug}/' if kind=='product' else {'home':'','projects':'projects/','case':'projects/tooda.html'}[kind]
 def link(url,text,cls='text-link'):return f'<a class="{cls}" href="{url}">{text}<span aria-hidden="true">↗</span></a>'
 brand=f'<a class="brand" href="{base}" aria-label="{c["name"]}"><img src="/assets/moca-mark.svg" alt="" width="52" height="50"><span class="brand-name">moca<small>{"tecnologia" if locale=="pt" else "technology"}</small></span></a>'
 nav=''.join(f'<a href="{base}#{anchor}">{label}</a>' for anchor,label in zip(['solutions','products','projects','about'],c['nav']))
 header=f'<a class="skip" href="#main">{c["skip"]}</a><header class="header"><div class="wrap header-inner">{brand}<button class="menu-button" type="button" aria-controls="navigation" aria-expanded="false">{c["menu"]}</button><nav class="nav" id="navigation" aria-label="{"Principal" if locale=="pt" else "Main"}">{nav}<a class="lang" href="{other}{suffix}" lang="{"en" if locale=="pt" else "pt-BR"}" aria-label="{"English" if locale=="pt" else "Português"}">{c["other"]}</a>{link(base+"#contact",c['contact'],'button outline')}</nav></div></header>'
 contact=f'<section class="contact" id="contact"><div class="wrap contact-inner"><div><p class="eyebrow">{c["contact"]}</p><h2>{c["contact_title"]}</h2><p>{c["contact_desc"]}</p></div><div class="contact-actions">{link(CONTACT_URL,'WhatsApp','button')}{link('mailto:'+EMAIL,EMAIL)}<span>+55 (21) 96604-5167</span></div></div></section>'
 footer=f'<footer class="footer"><div class="wrap footer-inner"><span>© Moca · {c["footer"]}</span><div class="footer-links"><a href="https://github.com/developer-moca">GitHub ↗</a><a href="{other}{suffix}">{"English" if locale=="pt" else "Português"}</a></div></div></footer>'
 def project():return f'<div class="project"><a class="project-visual" href="{base}projects/tooda.html"><img src="/images/clients/moca-tooda-cover.png" alt="TOODA — Safe Children" width="1000" height="600" loading="lazy"></a><div><p class="eyebrow">{c["project_type"]}</p><h3>TOODA — Safe Children</h3><p>{c["tooda_desc"]}</p>{link(base+"projects/tooda.html",c["view_project"])}</div></div>'
 if kind=='home':
  body=f'''<section class="hero"><div class="wrap"><div class="hero-grid"><div><p class="eyebrow">{c['eyebrow']}</p><h1>{c['headline']}</h1><p class="lead">{c['intro']}</p><div class="actions">{link('#contact',c['cta'],'button')}{link('#products',c['explore'])}</div></div><div class="brand-drawing" aria-hidden="true"><img src="/assets/moca-mark.svg" alt="" width="360" height="330"><span class="drawing-note">MOCA / {"NOVOS HORIZONTES" if locale=='pt' else "NEW HORIZONS"}</span></div></div><div class="hero-bottom"><span>{c['bottom'][0]}</span><span>{c['bottom'][1]} ↘</span></div></div></section>
<section class="section light" id="solutions"><div class="wrap"><div class="section-heading"><h2>{c['solutions']}</h2><p class="section-intro">{c['solutions_intro']}</p></div><div class="split"><article class="service"><span class="number">01 /</span><h3>{c['custom']}</h3><p>{c['custom_desc']}</p><div class="tags">{''.join('<span>'+t+'</span>' for t in c['tags'])}</div></article><article class="service"><span class="number">02 /</span><h3>{c['own']}</h3><p>{c['own_desc']}</p>{link('#products',c['explore'])}</article></div></div></section>
<section class="section" id="products"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">{c['own']}</p><h2>{c['product_heading']}</h2></div><p class="lead">{"Soluções e jogos que dão forma às nossas ideias. Conheça o que estamos construindo." if locale=='pt' else "Solutions and games that bring our ideas to life. Explore what we are building."}</p></div><div class="products-grid">{products(locale,base)}</div></div></section>
<section class="section light" id="projects"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">{c['nav'][2]}</p><h2>{c['projects']}</h2></div>{link(base+'projects/',c['all_projects'])}</div>{project()}</div></section>
<section class="section light" id="about"><div class="wrap"><h2>{c['process_title']}</h2><div class="process">{''.join(f'<article><span class="number">0{i+1} /</span><h3>{title}</h3><p>{desc}</p></article>' for i,(title,desc) in enumerate(c['steps']))}</div><div class="about"><h2>{c['about_title']}</h2><p>{c['about_desc']}</p></div></div></section>'''
 elif kind=='product':
  body=product_body(locale,base,slug,link)
 elif kind=='projects':
  body=f'<section class="page-hero"><div class="wrap"><p class="eyebrow">{c["nav"][2]}</p><h1>{c["projects"]}</h1><p class="lead">{c["project_intro"]}</p></div></section><section class="section light"><div class="wrap">{project()}</div></section>'
 else:
  docs=''
  for (title,desc,action),img,pdf in zip(c['docs'],['moca-tooda-cover.png','tooda-pitch-cover.png'],['moca-tooda-project.pdf','tooda-pitch.pdf']):
   docs+=f'<article class="document"><img src="/images/clients/{img}" alt="{escape(title)}" loading="lazy"><h2>{title}</h2><p>{desc}</p>{link("/files/"+pdf,action+" (PDF)")}</article>'
  body=f'<section class="page-hero"><div class="wrap"><a class="breadcrumb" href="{base}projects/">← {c["back"]}</a><p class="eyebrow">{c["project_type"]}</p><h1>{c["case_title"]}</h1><p class="lead">{c["case_intro"]}</p></div></section><section class="section light"><div class="wrap document-grid">{docs}</div></section>'
 title=PRODUCTS[slug]['name']+' — '+c['name'] if kind=='product' else c['name'] if kind=='home' else (c['nav'][2] if kind=='projects' else 'TOODA')+' — '+c['name']
 url=f'https://www.mocatecnologia.com{base}{suffix}'
 image=f'https://www.mocatecnologia.com/assets/share-{locale}-v1.jpg'
 social_title = ('Moca Tecnologia | Software sob medida e produtos digitais' if locale=='pt' else 'Moca Technology | Custom software and digital products') if kind=='home' else title
 description = PRODUCTS[slug]['intro'][0 if locale=='pt' else 1] if kind=='product' else c['meta'] if kind=='home' else (c['project_intro'] if kind=='projects' else c['case_intro'])
 image_alt = 'Moca Tecnologia — montanha e sol em dourado sobre azul-marinho' if locale=='pt' else 'Moca Technology — gold mountain and sun on navy'
 social=f'''<link rel="canonical" href="{url}">
<meta property="og:title" content="{escape(social_title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{c['name']}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{'pt_BR' if locale=='pt' else 'en_US'}">
<meta property="og:locale:alternate" content="{'en_US' if locale=='pt' else 'pt_BR'}">
<meta property="og:image" content="{image}">
<meta property="og:image:secure_url" content="{image}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{image_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(social_title)}">
<meta name="twitter:description" content="{escape(description)}">
<meta name="twitter:image" content="{image}">
<meta name="twitter:image:alt" content="{image_alt}">'''
 return f'''<!doctype html>
<html lang="{c['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title><meta name="description" content="{escape(description)}"><meta name="theme-color" content="#202b3d">{social}<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg"><link rel="alternate" hreflang="{c['lang']}" href="https://www.mocatecnologia.com{base}{suffix}"><link rel="alternate" hreflang="{COPY['en' if locale=='pt' else 'pt']['lang']}" href="https://www.mocatecnologia.com{other}{suffix}"><link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script></head><body>{header}<main id="main">{body}{contact}</main>{footer}</body></html>'''

if __name__=='__main__':
 for locale in COPY:
  base=ROOT/'pt' if locale=='pt' else ROOT
  for kind,path in [('home','index.html'),('projects','projects/index.html'),('case','projects/tooda.html')]:
   dest=base/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page(locale,kind))
  for slug in PRODUCTS:
   dest=base/'products'/slug/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page(locale,'product',slug))
 print('Generated 14 pages.')
