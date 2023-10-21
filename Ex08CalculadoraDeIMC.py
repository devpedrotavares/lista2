print("-------------------- Calculadora de IMC --------------------")

print("Entre com o seu peso: ")

peso = float(input())

print("Entre com a sua altura: ")

altura = float(input())

imc = peso / (altura * altura)

print("O seu IMC é: " + str(imc))