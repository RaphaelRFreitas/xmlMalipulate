import xml.etree.ElementTree as ET
import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont


def criaImagem(largura, altura, tags, locations):
    # cria a imagem
    img = Image.new('RGB', (largura, altura), color = (255, 255, 255))

    # adiciona o texto
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 50)  # define a fonte e tamanho do texto
    for i in range(len(tags)):
        draw.text((int(locations[i][0]), int(locations[i][1])), tags[i], fill=(0, 0, 0), font=font)

    # salva a imagem
    img.save(f'imagemTags.png')

tags = []
locations = []
xmlreed = ET.parse('Mina - Sistemas.xml')
root = xmlreed.getroot()
largura = int(root.get('width')) # pegar o valor do atributo width do elemento raiz
altura = int(root.get('height')) # pegar o valor do atributo height do elemento raiz
for datafield in root.iter():
    for datasource in datafield.findall('Datasource'):
        tags.append(datasource.get('tag').strip()) # pegar o valor do atributo tag em cada tag datasource
    for datasource in datafield.findall('Location'):
        locations.append((datasource.get('left'), datasource.get('top'))) # pegar o valor dos atributos left e top em cada tag location

#criaImagem(largura, altura, tags, locations) # chamar a função para criar a imagem
#criar data frame com tags, top e left
df = pd.DataFrame(tags, columns=['Tags'])
#df['Top'] = [int(i[1]) for i in locations]
#df['Left'] = [int(i[0]) for i in locations]
writer = pd.ExcelWriter(f'Alltags.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Tags', index=False)
writer._save() # salvar o arquivo xlsx no mesmo diretório do xml