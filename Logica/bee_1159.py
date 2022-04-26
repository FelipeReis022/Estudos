def soma_pares(numero: int) -> str:
    """Soma os numeros pares no intervalo determinado"""
    soma = 0
    intervalo = 5

    if numero != 0:
        while intervalo > 0:
            if numero % 2 == 0:
                soma = soma + numero
                numero = numero + 1
                intervalo -= 1
            else:
                numero = numero + 1
        return print(soma)

while True:
    numero_inicial = int(input())
    if numero_inicial != 0:
        soma_pares(numero_inicial)
    elif numero_inicial == 0:
        break
