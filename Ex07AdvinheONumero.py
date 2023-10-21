import random

def getRandomNumber(max):
    return random.randint(0, max)

print("Selecione o número máximo para advinhar: ")

max = int(input())

numero = abs(getRandomNumber(max))

print("Advinhe o número: ")

numeroAdvinhado = int(input())

while numero != numeroAdvinhado:
    if numero > numeroAdvinhado:
        print("O número correto é maior")
    else:
        print("O número correto é menor")

    print("Tente novamente: ")

    numeroAdvinhado = int(input())

print("Parabéns, você acertou!")