def dobra_valor(num) -> list:
    """Recebe um valor inicial e cria uma lista
    dobrando os respectivos valores."""
    lista_valores = []
    lista_valores.append(num)
    for n in lista_valores:
        lista_valores.append(n*2)
        if len(lista_valores) == 10:
            break
    return lista_valores

def imprime_lista(num) -> str:
    posicao = 0
    for n in dobra_valor(num):
        print(f'N[{posicao}] = {n}')
        posicao += 1

numero = int(input())
imprime_lista(numero)
