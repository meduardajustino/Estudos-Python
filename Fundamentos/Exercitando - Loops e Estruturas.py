# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
# quadrados dos elementos do vetor.


total = 0


def main():
    vetor = []
    for i in range(10):
        numero = int(input("Digite um número inteiro: "))
        vetor.append(numero)
    somaquad = sum(x ** 2 for x in vetor)
    print(f"A soma dos quadrados dos elementos do vetor é: {somaquad}")


main()


total = 0


def main():
    resposta = input("Digite 10 números separados por vírgulas: ")
    print(resposta)
    lista_numeros = resposta.split(",")

    soma = 0
    for numero in lista_numeros:
        quadrado = int(numero)**2
        print(quadrado)
        soma += quadrado  # soma = soma + quadrado

    print(soma)


main()
