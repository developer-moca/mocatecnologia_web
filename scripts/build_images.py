"""Build responsive, lossless WebP images. Requires ImageMagick with WebP support."""
import hashlib
import json
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.image-cache'
OUT = ROOT / 'assets' / 'optimized'
SOURCES = {
 'dungeon-cover': 'https://dungeonfighters.github.io/Web/assets/images/screenshot-0.png',
 **{f'dungeon-{i}': f'https://dungeonfighters.github.io/Web/assets/images/screenshot-{i}.png' for i in (1, 2, 3)},
 'tooda-cover': '/images/clients/moca-tooda-cover.png',
 'tooda-pitch': '/images/clients/tooda-pitch-cover.png',
 'tooda-poster': '/assets/media/tooda-fia-poster.png',
 'paper-hero': 'https://i.ytimg.com/vi/pX-UymX0gXg/hqdefault.jpg',
 'kalimour': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2402460/header.jpg?t=1707143301',
}


def run(*args):
 return subprocess.check_output(args, text=True).strip()


def build():
 CACHE.mkdir(exist_ok=True); OUT.mkdir(parents=True, exist_ok=True)
 manifest = {}
 for name, source in SOURCES.items():
  if source.startswith('https:'):
   original = CACHE / name
   if not original.exists():
    with urllib.request.urlopen(source, timeout=45) as response:
     original.write_bytes(response.read())
  else:
   original = ROOT / source.lstrip('/')
  width, height = map(int, run('magick', 'identify', '-format', '%w %h', str(original)).split())
  variants = []
  for size in sorted({min(width, n) for n in (480, 800, 1200, width)}):
   temp = CACHE / f'{name}-{size}.webp'
   args = ['magick', str(original)]
   if size < width:
    args += ['-resize', f'{size}x']
   args += ['-strip', '-define', 'webp:lossless=true', '-define', 'webp:method=6', str(temp)]
   run(*args)
   content = temp.read_bytes()
   filename = f'{name}-{size}-{hashlib.sha256(content).hexdigest()[:10]}.webp'
   (OUT / filename).write_bytes(content)
   variants.append({'width': size, 'url': '/assets/optimized/' + filename, 'bytes': len(content)})
  if len(variants) == 1 and variants[0]['bytes'] >= original.stat().st_size:
   (ROOT / variants[0]['url'].lstrip('/')).unlink()
   print(f'{name}: keeping the smaller original image')
   continue
  manifest[source] = {'width': width, 'height': height, 'original_bytes': original.stat().st_size, 'variants': variants}
  print(f'{name}: {original.stat().st_size:,} -> {variants[-1]["bytes"]:,} bytes at original resolution')
 (ROOT / 'scripts' / 'image_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')

if __name__ == '__main__':
 build()
