taxasDeCambio = {
    "dolar": 1.0,
    "euro": 1.06,
    "yen": 0.0067,
    "real": 0.2,
    "yuan": 0.14
}

print("-------------------- Conversor de moedas --------------------")

print("Opções disponíveis: ")

for moeda in taxasDeCambio.keys():
    print(moeda + "; ")

print()

moedaOrigem = ""

while moedaOrigem not in taxasDeCambio:
    print("Entre com a moeda de origem: ")

    moedaOrigem = input()

    if moedaOrigem not in taxasDeCambio:
        print("Opção inválida, tente novamente...")

moedaDestino = ""

while moedaDestino not in taxasDeCambio:
    print("Entre com a moeda de destino: ")

    moedaDestino = input()

    if moedaDestino not in taxasDeCambio:
        print("Opção inválida, tente novamente...")

valor = 0.0

print("Entre com o valor: ")

valor = float(input())

valorEmDolar = valor * taxasDeCambio[moedaOrigem]

valorConvertido = valorEmDolar / taxasDeCambio[moedaDestino]

print("%f em %s é equivalente a %f em %s" % (valor, moedaOrigem, valorConvertido, moedaDestino))