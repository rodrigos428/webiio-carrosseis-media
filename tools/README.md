# Ferramentas para gerar os carrosséis

1. Guarda os .dc.html dos slides numa pasta, com nomes por ordem (01.dc.html, 02.dc.html...).
2. Corre `python3 render.py PASTA_HTML PASTA_BLOBS PASTA_SAIDA`. Cada linha "EM FALTA <id>" é um ficheiro que tens de buscar com read_asset do canvas e gravar em PASTA_BLOBS/<id> (imagens: copia o ficheiro guardado pela ferramenta; svg e css: grava o texto). Repete até não aparecer nenhum EM FALTA.
3. O render cria 01.png, 02.png... a 1080x1350. Confirma que não há EM FALTA na última corrida.
4. Copia para uma pasta nova AAAA-MM-DD-tema/ neste repositório, faz commit e push para main.
5. Link público de cada imagem: https://raw.githubusercontent.com/rodrigos428/webiio-carrosseis-media/main/AAAA-MM-DD-tema/01.png
