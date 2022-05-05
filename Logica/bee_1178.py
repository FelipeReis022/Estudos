def crialista(numero_inicial) -> list:
    """Cria lista com 100 valores, definidos pela metade do valor anterior"""
    lista_numeros = [numero_inicial]
    for n in lista_numeros:
        lista_numeros.append(n / 2)
        if len(lista_numeros) == 100:
            break
    return lista_numeros

def imprime(numero_inicial) -> str:
    """Imprime lista com seu index e respectivo valor, somente com 4 casas decimais"""
    contador = 0
    for n in crialista(numero_inicial):
        print(f'N[{contador}] = {n:.4f}')
        contador += 1


numero = float(input())
imprime(numero)
