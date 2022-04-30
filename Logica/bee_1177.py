numero = int(input())
lista = []
cont = 0
while len(lista) < 1000:
    lista.append(numero-3)
    lista.append(numero-2)
    lista.append(numero-1)

for n in lista:
    print(f'N[{cont}] = {n}')
    cont += 1
