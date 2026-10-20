"""Use generated lossless WebP variants without changing page layouts."""
import json
import re
from pathlib import Path

IMAGES = json.loads((Path(__file__).parent / 'image_manifest.json').read_text())


def optimize_images(html):
 def replace(match):
  tag = match.group(0)
  source = re.search(r'\bsrc="([^"]+)"', tag)
  if not source or source[1] not in IMAGES:
   return tag
  image = IMAGES[source[1]]
  variants = image['variants']
  default = next((v for v in variants if v['width'] >= 800), variants[-1])
  tag = tag.replace(source[0], f'src="{default["url"]}"')
  tag = re.sub(r'\s(?:width|height)="[^"]*"', '', tag)
  srcset = ', '.join(f'{v["url"]} {v["width"]}w' for v in variants)
  sizes = '(max-width: 760px) calc(100vw - 40px), (max-width: 1296px) 50vw, 600px'
  return tag[:-1] + f' width="{image["width"]}" height="{image["height"]}" srcset="{srcset}" sizes="{sizes}" decoding="async">'
 html = re.sub(r'<img\b[^>]*>', replace, html)
 poster = '/assets/media/tooda-fia-poster.png'
 return html.replace(f'poster="{poster}"', f'poster="{IMAGES[poster]["variants"][-1]["url"]}"')
