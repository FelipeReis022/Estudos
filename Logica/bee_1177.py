numero = int(input())
lista = list(range(0, numero))
index = 0

for n in lista:
    lista.append(n)
    if len(lista) == 1000:
        break
for n in lista:
    print(f'N[{index}] = {n}')
    index += 1
