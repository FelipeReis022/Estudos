def retorna_soma(num1, num2) -> str:
    if (num1 % 2) == 0:
        numeros_impares = list(range(num1 + 1, num2*num1, 2))
    else:
        numeros_impares = list(range(num1, num1*num2, 2))
    return print(sum(numeros_impares[:numero2]))

numero_teste = int(input())

while numero_teste > 0:
    numero_teste -= 1
    numero1, numero2 = map(int, input().split())

    retorna_soma(numero1, numero2)
