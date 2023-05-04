import pandas as pd
import os


caminho_principal = "C:/Users/raphael.r.freitas/OneDrive - Accenture/Desktop/Telas S11D"
arquivo2 = pd.read_excel('S11D_AF_DadosOp.xlsx')
for diretorio_atual, subdiretorios, arquivos in os.walk(caminho_principal):
    for arquivo in arquivos:
        # verificar se o arquivo é um XML
        if arquivo.endswith("Alltags.xlsx"):
            try:
                arquivo1 = pd.read_excel(f'{diretorio_atual}\\{arquivo}')
                resultado = pd.merge(arquivo1, arquivo2[['TagIP21', 'TagPI', 'Path']], left_on='Tags', right_on='TagIP21',
                                     how='left')

                resultado_final = resultado[['Tags', 'TagPI', 'Path']]

                writer = pd.ExcelWriter(f'{diretorio_atual}\\Alltags_PI_Path.xlsx', engine='xlsxwriter')
                resultado_final.to_excel(writer, sheet_name='Tags', index=False)
                writer._save()  # salvar o arquivo xlsx no mesmo diretório do xml

                print(f"Arquivo {arquivo} salvo com sucesso!")
            except Exception as e:
                print(f"Erro {e} no arquivo {arquivo}")  # caso ocorra algum erro, imprimir o nome do arquivo