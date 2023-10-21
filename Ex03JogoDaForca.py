import random

def atualizarPalavraDisplay(palavraAtual, palavraDisplay, letra):
    count = 0;

    for i in range(len(palavraAtual)):
        if palavraAtual[i] == letra:
            palavraDisplay[i] = letra
            count = count + 1
    
    return count

def getPalavraAleatoria():
    rand = random.Random()
    index = rand.randint(0, len(stringPool) - 1)
    return stringPool[index]

def basicPrint(palavra_display, chances, letras_tentadas):
    print("Chances restantes:", chances)
    
    print("Tentativas erradas:", end=" ")
    for c in letras_tentadas:
        print(c, end="; ")
    print()
    
    print("Palavra:", end=" ")
    for i in range(len(palavra_display)):
        print(palavra_display[i], end=" ")
    print()


stringPool = ["computador", "monitor", "mouse", "pincel", "gaivota", "luz", "mar", "vidro", "carro", "moto", "navio", "barco", "remo", "metal", "ouro", "prata", "favela", "drama", "sucesso", "lama", "brasil", "marinha", "gente", "temor", "servil", "liberdade", "morte"]

palavraAtual = getPalavraAleatoria()

palavraDisplay = ['_'] * len(palavraAtual)

letrasTentadas = []

chances = 10

acertos = 0

while chances > 0 and acertos < len(palavraAtual):
    basicPrint(palavraDisplay, chances, letrasTentadas)

    print("Entre com a próxima letra: ")

    letra = input()[0]

    if letra in palavraAtual:
        print("Letra correta!")
        numeroDeLetras = atualizarPalavraDisplay(palavraAtual, palavraDisplay, letra)
        acertos += numeroDeLetras
    else:
        print("Letra errada!")
        letrasTentadas.append(letra)
        chances -= 1

    print()

if chances == 0:
    print("Você perdeu... Tente na próxima")
else:
    print(palavraAtual)

    print("Você ganhou! Parabéns!")