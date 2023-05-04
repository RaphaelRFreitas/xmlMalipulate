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
                locations = [] # lista para armazenar as posições
                xmlread = ET.parse(caminho_xml) # ler o arquivo xml
                root = xmlread.getroot() # pegar o elemento raiz do xml
                largura = int(root.get('width')) # pegar o valor do atributo width do elemento raiz
                altura = int(root.get('height')) # pegar o valor do atributo height do elemento raiz

                for level in root.iter("DataField"):
                    for datasource in level.findall('Datasource'):
                        tags.append(datasource.get('tag').strip()) # pegar o valor do atributo tag em cada tag datasource
                    for datasource in level.findall('Location'):
                        locations.append((datasource.get('left'), datasource.get('top'))) # pegar o valor dos atributos left e top em cada tag location
                print(f"Arquivo {arquivo} lido com sucesso! Com {len(tags)} tags")

                criaImagem(largura, altura, tags, locations, diretorio_atual) # chamar a função para criar a imagem
                print(f"Imagem criada em {diretorio_atual}")
                #criar data frame com tags, top e left
                df = pd.DataFrame(tags, columns=['Tags'])
                df['Top'] = [int(i[1]) for i in locations]
                df['Left'] = [int(i[0]) for i in locations]
                writer = pd.ExcelWriter(f'{diretorio_atual}\\tags.xlsx', engine='xlsxwriter')
                df.to_excel(writer, sheet_name='Tags', index=False)
                writer._save() # salvar o arquivo xlsx no mesmo diretório do xml
            except:
                print(f"Erro ao abrir o arquivo {arquivo}") # caso ocorra algum erro, imprimir o nome do arquivo
