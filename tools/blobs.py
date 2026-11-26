"""Lista os ids /_blob/ usados pelas pranchas (e pelos CSS já descarregados) que ainda faltam em PASTA_BLOBS.
Uso: python3 blobs.py PASTA_HTML PASTA_BLOBS
Busca cada id em falta com a ferramenta read_asset do canvas e grava-o em PASTA_BLOBS/<id>
(imagens: copia o ficheiro que a ferramenta guardou; svg e css: grava o texto devolvido). Repete até não faltar nada."""
import os,re,sys
H,B=sys.argv[1:3]; os.makedirs(B,exist_ok=True)
ids=set()
for f in os.listdir(H):
    if f.endswith('.html'): ids|=set(re.findall(r'/_blob/([0-9a-f]{32})',open(os.path.join(H,f)).read()))
for f in os.listdir(B):
    try: ids|=set(re.findall(r'/_blob/([0-9a-f]{32})',open(os.path.join(B,f),errors='ignore').read()))
    except Exception: pass
falta=sorted(i for i in ids if not os.path.exists(os.path.join(B,i)))
print('\n'.join(falta) if falta else 'nada em falta')
