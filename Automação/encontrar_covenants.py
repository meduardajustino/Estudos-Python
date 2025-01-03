# Bibliotecas utilizadas, importante instalar com pip install

import PyPDF2
from PyPDF2 import PdfReader
import re
import os
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor # permite executar várias tarefas simultaneamente em threads separada

pasta_mega = r"C:\Users\PPGCC\Downloads\Notas Explicativas"
contador_covenants = 0
diretorio = []

for caminho, subpastas, arquivos in os.walk(pasta_mega):
    for nome in arquivos:
        if nome.endswith('.pdf'):
            diretorio.append(os.path.join(caminho, nome))

# percorre as subpastas e arquivos na pasta Mega
for caminho, subpastas, arquivos in os.walk(pasta_mega):
    for nome in arquivos:
        print(caminho, nome)
        diretorio.append(os.path.join(caminho, nome)) #concatena e adiciona a lista

def processa_pdf(nota_explicativa):
    global contador_covenants
    try:
        with open(nota_explicativa, 'rb') as file:
                pdf = PdfReader(file) # percorre a lista de arquivos e analisa o conteúdo das notas explicativas
                for page in pdf.pages:
                    content = page.extract_text()
                    if content and any(term in content.lower() for term in ['covenants', 'covenant', "cláusulas restritivas"]):
                        contador_covenants += 1 
                        
                        # salva o arquivo na pasta de empresas com covenants (ano do documento)
                        nome_empresa = nota_explicativa.split("\\")[-2]  # nome da empresa está na subpasta
                        ano_documento = nota_explicativa.split("\\")[-1].split('_')[0]  # o ano é o no nome do arquivo
                        print(f'Nome da empresa: {nome_empresa} e ano do documento {ano_documento}')
                        
                        nova_pasta = os.path.join(r"C:\Users\PPGCC\Downloads\Empresas Com Covenants", nome_empresa, ano_documento)
                        print(f'Nova pasta: {nova_pasta}')
                        
                        os.makedirs(nova_pasta, exist_ok=True)  # cria a pasta, se não existir
                        
                        novo_caminho = os.path.join(nova_pasta, os.path.basename(nota_explicativa))
                        print(f'Novo caminho: {novo_caminho}')
                        
                        shutil.copy(nota_explicativa, novo_caminho)  # move o arquivo para a nova pasta
                        print(f"Arquivo {os.path.basename(nota_explicativa)} movido para {novo_caminho}")
                        
    except Exception as e:
        print(f"Erro ao processar o arquivo {nota_explicativa}: {e}")

# usando ThreadPoolExecutor para processar os PDFs em paralelo
with ThreadPoolExecutor() as executor:
    executor.map(processa_pdf, diretorio)

print(f"Total de notas explicativas com covenants: {contador_covenants}")
        
