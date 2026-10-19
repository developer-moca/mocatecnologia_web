"""Generate social cards from the site's vector logo; requires librsvg and ImageMagick."""
from pathlib import Path
import subprocess
ROOT = Path(__file__).resolve().parents[1]
mark = (ROOT/'assets/moca-mark.svg').read_text().split('>',1)[1].rsplit('</svg>',1)[0]
for locale,descriptor,tagline in [('pt','tecnologia','Software sob medida. Produtos próprios.'),('en','technology','Custom software. Our own products.')]:
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#202B3D"/>
<path d="M80 80h1040M80 550h1040" stroke="#455063" stroke-width="1"/>
<g fill="none" transform="translate(230 160) scale(1.05)">{mark}</g>
<g fill="#F5F3ED" font-family="Arial,Helvetica,sans-serif">
<text x="520" y="290" font-size="112" font-weight="bold" letter-spacing="-5">moca</text>
<text x="527" y="335" font-size="24" letter-spacing="7">{descriptor}</text>
<text x="600" y="457" text-anchor="middle" font-size="29">{tagline}</text>
<text x="600" y="511" text-anchor="middle" font-size="19" fill="#C3A36B" letter-spacing="2">mocatecnologia.com</text>
</g></svg>'''
 path=ROOT/f'assets/share-{locale}-v1.svg';path.write_text(svg)
 png=subprocess.run(['rsvg-convert',str(path)],check=True,capture_output=True).stdout
 subprocess.run(['magick','png:-','-strip','-quality','90',str(path.with_suffix('.jpg'))],input=png,check=True)
