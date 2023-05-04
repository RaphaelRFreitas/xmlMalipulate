import xml.etree.ElementTree as ET
import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont

def criaImagem(largura, altura, tags, locations, diretorio_atual):
    # cria a imagem
    img = Image.new('RGB', (largura, altura), color = (255, 255, 255))

    # adiciona o texto
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 50)  # define a fonte e tamanho do texto
    for i in range(len(tags)):
        draw.text((int(locations[i][0]), int(locations[i][1])), tags[i], fill=(0, 0, 0), font=font)

    # salva a imagem
    img.save(f'{diretorio_atual}\\imagemAll.png')

def criaPDF(largura, altura, tags, locations, diretorio_atual):
    pass

# definir o caminho da pasta principal
caminho_principal = "C:/Users/raphael.r.freitas/OneDrive - Accenture/Desktop/Telas S11D"
for diretorio_atual, subdiretorios, arquivos in os.walk(caminho_principal):
    for arquivo in arquivos:
        # verificar se o arquivo é um XML
        if arquivo.endswith(".xml"):
            try:
                caminho_xml = os.path.join(diretorio_atual, arquivo)
                tags = [] # lista para armazenar as tags
                xmlread = ET.parse(caminho_xml) # ler o arquivo xml
                root = xmlread.getroot() # pegar o elemento raiz do xml

                # Olhar cada tag em qualquer nível do xml
                for level in root.iter():
                    for datasource in level.findall('Datasource'):
                        tags.append(datasource.get('tag').strip()) # pegar o valor do atributo tag em cada tag datasource

                tags = list(set(tags)) # remover tags duplicadas
                tags = [tag for tag in tags if tag != ''] # remover tags vazias
                print(f"Arquivo {arquivo} lido com sucesso! Com {len(tags)} tags")


                #criar data frame com tags
                df = pd.DataFrame(tags, columns=['Tags'])
                writer = pd.ExcelWriter(f'{diretorio_atual}\\Alltags.xlsx', engine='xlsxwriter')
                df.to_excel(writer, sheet_name='Tags', index=False)
                writer._save() # salvar o arquivo xlsx no mesmo diretório do xml
                print(f"Arquivo {arquivo} salvo com sucesso!")
            except:
                print(f"Erro ao abrir o arquivo {arquivo}") # caso ocorra algum erro, imprimir o nome do arquivo
