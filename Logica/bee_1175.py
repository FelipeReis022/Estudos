def inverte_lista(lista) -> list:
    """Inverte ordem da lista"""
    lista_reversa = list(reversed(lista))
    return lista_reversa

def imprime(lista) -> str:
    index = 0
    for num in inverte_lista(lista):
        print(f'N[{index}] = {num}')
        index += 1

lista_numeros = []

while len(lista_numeros) < 5:
    numero = int(input())
    lista_numeros.append(numero)

imprime(lista_numeros)
