def soma_divisores(num) -> int:
    """Calcula os divisores do numero e retorna a soma deles"""

    lista_testes = list(range(1, num))
    divisores = [n for n in lista_testes if (num % n) == 0]
    soma_divisores = sum(divisores)
    return soma_divisores

def impressao_teste(numero) -> str:
    """Verifica se a soma dos divisores é igual ao numero,
    se for retorna que é um número perfeito, se não,
    não é perfeito.
    """
    if soma_divisores(numero) == numero:
        return f'{numero} eh perfeito'
    else:
        return f'{numero} nao eh perfeito'

numero_testes = int(input())

while numero_testes > 0:
    numero_testes -= 1
    numero = int(input())
    # objeto = soma_divisores(numero)
    print(impressao_teste(numero))