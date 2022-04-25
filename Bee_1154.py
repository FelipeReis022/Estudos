def calculo(num):
    resultado = sum(num) / len(num)
    return resultado

lista_idades = []

while True:

    idade = int(input())

    if idade > 0:
        lista_idades.append(idade)
    else:
        break

print("{:.2f}".format(calculo(lista_idades)))