def verifica_numero(num) -> int:
    """Verifica se o número é primo ou não"""
    divisores = list(range(1, numero + 1))
    cont = 0
    for n in divisores:
        if num % n == 0:
            cont += 1
    return cont

def imprime_resultado(num) -> str:
    """Verifica o contador de divisores e retorna uma str"""
    if num == 1:
        return f'{num} nao eh primo'
    elif verifica_numero(num) > 2:
        return f'{num} nao eh primo'
    else:
        return f'{num} eh primo'

numero_teste = int(input())

while numero_teste > 0:
    numero_teste -= 1
    numero = int(input())
    print(imprime_resultado(numero))
