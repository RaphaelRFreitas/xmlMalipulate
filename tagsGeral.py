import os
import pandas as pd

# Defina o caminho da pasta com os arquivos
caminho_principal = "C:/Users/raphael.r.freitas/OneDrive - Accenture/Desktop/Telas S11D"

# Crie uma lista para armazenar os DataFrames
lista_dataframes = []

for diretorio_atual, subdiretorios, arquivos in os.walk(caminho_principal):
    for arquivo in arquivos:
        # verificar se o arquivo é um XML
        if arquivo.endswith("Alltags_PI_Path.xlsx"):
            try:
                df = pd.read_excel(f'{diretorio_atual}\\{arquivo}')
            # Leia o arquivo em um DataFrame e adicione à lista
                lista_dataframes.append(df)
            except Exception as e:
                print(f"Erro {e} no arquivo {arquivo}")

# Concatene todos os DataFrames em um único DataFrame
resultado = pd.concat(lista_dataframes, ignore_index=True)

# Salve o DataFrame resultante em um arquivo .xlsx
resultado.to_excel("levantamentoGeraldeTags.xlsx", index=False)
