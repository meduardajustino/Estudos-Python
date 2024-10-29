
def mostrarmenu():
    print("-"*38)
    print(" 🎫🧳 CALCULAR O PREÇO DA VIAGEM 🚍 ")
    print("-"*38)
    print("Bem-vinda a ON34bus, para calcularmos o preço total da sua viagem responda a pergunta seguinte 🚏")


def calcularvalor(km, valorfixo):
    if km < 50:
        print("Não é possível calcular o preço para viagens com menos de 50Km. \n🚧 Tente uma viagem mais longa. \n🚌 Estamos encerrando o atendimento. 🚌")
    elif 50<= km <= 200:
        print(f'Sua viagem com {km}km custará R${valorfixo + km*0.75} 💺.')
    elif 200 < km <= 500:
        print(f'Sua viagem com {km}km custará R${valorfixo + km*0.6} 💺.')
    else:
        print(f'Sua viagem com {km}km custará R${valorfixo + km*0.5} 💺.')

try: 
    mostrarmenu()

    km = float(input("Quandos quilometros tem sua viagem (escreva apenas o dado numérico)? "))
    valorfixo = 20

    calcularvalor(km, valorfixo)
    print("Obrigada pela consulta. Podemos agendar a sua viagem? 🎫🧳")
except:
    print("Digite apenas numeros inteiros ou decimais positivos. O sistema não ler caracteres. ⛔ \nTente novamente 🚌")