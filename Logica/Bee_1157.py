def calculo(num):
    """Calcula os divisores do numero"""

    lista_testes = list(range(1, num + 1))
    divisores = [n for n in lista_testes if (num % n) == 0]
    for x in divisores:
        print(x)

numero = int(input())
calculo(numero)
