import sys

def getLetra(nota):
    if nota >= 8:
        return 'A'
    elif nota >= 6:
        return 'B'
    elif nota >= 4:
        return 'C'
    elif nota >= 2:
        return 'D'
    return 'E'

print("Quantas notas deseja computar?")

numeroDeNotas = int(input())

somaDasNotas = 0

for i in range(numeroDeNotas):
    print("Entre com a " + str(i+1) + "ª nota: ")
    somaDasNotas += float(input())

media = somaDasNotas / numeroDeNotas

print("A média das notas é: " + str(media))

notaEmLetra = getLetra(media)

print("A nota em letra correspondente é: " + notaEmLetra)