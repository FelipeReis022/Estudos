def verifica_numero(lista_inteiros):
    """Verifica se o valor é menor ou igual a zero,
    se for, muda o valor para 1."""
    for n in lista_inteiros:
        if n == 0 or n < 0:
            lista_inteiros[lista_inteiros.index(n)] = 1
    return lista_inteiros

def imprime_lista(lista_numeros) -> str:
    posicao = 0
    for n in verifica_numero(lista_numeros):
        print(f'X[{posicao}] = {n}')
        posicao += 1
    
numero_testes = 10
lista_inteiros = []

while numero_testes > 0:
    numero_testes -= 1
    numero = int(input())
    lista_inteiros.append(numero)

imprime_lista(lista_inteiros)
