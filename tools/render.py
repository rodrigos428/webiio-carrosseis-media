"""Renderiza pranchas .dc.html do canvas Webiio em PNG 1080x1350.
Uso: python3 render.py PASTA_HTML PASTA_BLOBS PASTA_SAIDA
  PASTA_HTML: ficheiros .dc.html (um por slide, por ordem do nome)
  PASTA_BLOBS: ficheiros com o nome igual ao id do /_blob/<id> (imagens, svg, css)
Antes: python3 blobs.py PASTA_HTML PASTA_BLOBS  (lista os ids que faltam buscar com read_asset)
"""
import asyncio,os,sys,subprocess
from playwright.async_api import async_playwright
H,B,O=[os.path.abspath(a) for a in sys.argv[1:4]]
T=os.path.dirname(os.path.abspath(__file__))
F=os.path.join(T,'node_modules/@fontsource/outfit/files/')
if not os.path.isdir(F): subprocess.run(['npm','i','--prefix',T,'@fontsource/outfit'],check=True,capture_output=True)
FONTCSS=''.join(f"@font-face{{font-family:'Outfit';font-weight:{w};src:url(https://fonts.local/{w}.woff2) format('woff2')}}" for w in (300,400,500,700))
def ctype(p):
    h=open(p,'rb').read(64).lstrip()
    if h.startswith(b'\x89PNG'): return 'image/png'
    if h.startswith(b'\xff\xd8'): return 'image/jpeg'
    if h.startswith(b'RIFF'): return 'image/webp'
    if h.startswith(b'<svg') or h.startswith(b'<?xml'): return 'image/svg+xml'
    return 'text/css'
async def route(r):
    u=r.request.url
    if '/_blob/' in u:
        i=u.split('/_blob/')[1].split('?')[0]; p=os.path.join(B,i)
        if os.path.exists(p): return await r.fulfill(path=p,content_type=ctype(p))
        print('EM FALTA',i); return await r.abort()
    if 'fonts.googleapis.com' in u: return await r.fulfill(body=FONTCSS,content_type='text/css')
    if 'fonts.local' in u:
        w=u.rsplit('/',1)[1].split('.')[0]; w='500' if w=='700' else w
        return await r.fulfill(path=F+f'outfit-latin-{w}-normal.woff2',content_type='font/woff2')
    if u.startswith('https://page.local/') and u.endswith('.html'):
        return await r.fulfill(path=os.path.join(H,u.rsplit('/',1)[1]),content_type='text/html')
    return await r.abort()
async def main():
    os.makedirs(O,exist_ok=True)
    files=sorted(f for f in os.listdir(H) if f.endswith('.html'))
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        await pg.route('**/*',route)
        for n,f in enumerate(files,1):
            await pg.goto('https://page.local/'+f); await pg.wait_for_timeout(700)
            await pg.evaluate('document.fonts.ready')
            el=await pg.query_selector('.s')
            await el.screenshot(path=os.path.join(O,f'{n:02d}.png'))
            print('ok',f,'->',f'{n:02d}.png')
        await b.close()
asyncio.run(main())
