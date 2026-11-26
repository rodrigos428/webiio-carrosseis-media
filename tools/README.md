# Ferramentas para gerar os carrosséis

1. Guarda os .dc.html dos slides numa pasta, com nomes por ordem (01.dc.html, 02.dc.html...).
2. `python3 blobs.py PASTA_HTML PASTA_BLOBS` e busca com read_asset cada id listado. Repete até dizer "nada em falta" (o CSS partilhado traz mais ids).
3. `python3 render.py PASTA_HTML PASTA_BLOBS PASTA_SAIDA` cria 01.png, 02.png... a 1080x1350.
4. Copia para uma pasta nova AAAA-MM-DD-tema/ neste repositório, faz commit e push para main.
5. Link público de cada imagem: https://raw.githubusercontent.com/rodrigos428/webiio-carrosseis-media/main/AAAA-MM-DD-tema/01.png
