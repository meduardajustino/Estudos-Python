# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


def main():
    print("☠️🔪 Para iniciarmos o interrogatório é importante que responda apenas (sim) ou (não).")
telefonou = lower(prompt = "1.⚰️ Você telefonou para a vítima? ")
local = lower(prompt = "2.⚰️ Você esteve no local do crime? ")
moradia = lower(prompt = "3.⚰️ Você mora perto da vítima? ")
divida = lower(prompt = "4.⚰️ Você devia para a vítima? ")
trabalho = lower(prompt = "5.⚰️ Você trabalhava com a vítima? ")

  
respostas = (telefonou, local, moradia, divida, trabalho)
contagem = sum(respostas == "sim")

if (contagem == 5) {
  print("Assassino 💀")
} else if (contagem >= 3) {
  print("Cúmplice 🪦")
} else if (contagem == 2) {
  print("Suspeita ⛏️")
} else {
  print("Inocente 🌍♥️🫵")
}