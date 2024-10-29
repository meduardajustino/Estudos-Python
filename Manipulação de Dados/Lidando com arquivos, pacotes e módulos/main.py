#https://docs.python.org/3/library/functions.html#open
import csv

data =[['Data', 'Acessos']] 
with open('abril-2024-tratado.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile) 

    for linha in leitor: 
        if linha != ['Data', 'Acessos']: #faço uma regra para excluir o cabeçalho da minha matriz (lista de listas)
            data.append(linha) #insiro minha linha (lista) na minha variavel global data que já possui o cabeçalho

with open('maio-2024-tratado.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)

    for linha in leitor:
        if linha != ['Data', 'Acessos']:
            data.append(linha)


#aqui eu crio um novo csv e escrevo os dados da variavel data nele
with open('abril-maio-2024.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerows(data) #aqui os dados estão sendo escritos!!!