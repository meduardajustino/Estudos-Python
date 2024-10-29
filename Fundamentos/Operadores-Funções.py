Print("Calculadora 🧮🔢📱")
import math
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

somar = x+y
subtrair = x-y
multiplicar = x*y
dividir = x/y
potencia = x**y
raizx = round(math.sqrt(x), 4)
raizy = round(math.sqrt(y),4)

#imprimir resultados
print("A soma de", x, "e", y, "é: ", somar)
somarimpar = somar%2
print("O resultado da soma", somar, "é impar?", bool(somarimpar))

print("A subtração de", x, "e", y, "é: ", subtrair)
subtraimpar = subtrair%2
print("O resultado da subtração", subtrair, "é impar?", bool(subtraimpar))

print("A multiplicação", x, "e", y, "é: ", multiplicar)
multimpar = multiplicar%2
print("O resultado da multiplicação", multiplicar, "é impar?", bool(multimpar))

print("A divisão de", x, "e", y, "é: ", dividir)
dividirimpar = dividir%2
print("O resultado da divisão", dividir, "é impar?", bool(dividirimpar))

print(x, "elevado a", y ,"é: ", potencia)
potenciaimpar = potencia%2
print("O resultado da potência", potencia, "é impar?", bool(potenciaimpar))

print("A raiz quadrade de", x, "é: ", raizx)
raizximpar = raizx%2
print("O resultado da raiz quadrada de", raizx, "é impar?", bool(raizximpar))

print("A raiz quadrade de", y, "é: ", raizy)
raizyimpar = raizy%2
print("O resultado da raiz quadrada de", raizy, "é impar?", bool(raizyimpar))

