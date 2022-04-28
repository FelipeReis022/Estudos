def imprime(lista_valores):
    posicao = 0
    for n in lista:
        if n <= 10:
            print(f'A[{posicao}] = {n:.1f}')
        posicao += 1

lista = []

while len(lista) < 3:
    numero = float(input())
    lista.append(numero)

imprime(lista)



