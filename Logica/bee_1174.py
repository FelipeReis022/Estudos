def imprime_menor(lista_valores) -> str:
    """Retorna em forma de str somente os valores
    menores ou iguais a 10 dentro da lista, com sua
    posição."""
    posicao = 0
    for valor in lista_numeros:
        if valor <= 10:
            print(f'A[{posicao}] = {valor:.1f}')
        posicao += 1

lista_numeros = []

while len(lista_numeros) < 100:
    numero = float(input())
    lista_numeros.append(numero)

imprime_menor(lista_numeros)
