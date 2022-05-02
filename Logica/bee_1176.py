
def listafibonacci(numero_valores):
    """"""
    a, b = 0, 1
    fibonacci = []
    for i in range(numero_valores + 1):
        if i == numero_valores -1:
            fibonacci.append(a)
        else:
            fibonacci.append(a)
        c = a + b
        a = b
        b = c
    return fibonacci

def imprimevalor(numero):
        objeto = listafibonacci(numero)
        if numero == 2:
            print(f'Fib(2) = 1')
        else:
            print(f'Fib({objeto.index(objeto[numero])}) = {objeto[numero]}')

numero_testes = int(input())

while numero_testes > 0:

    numero_testes -= 1
    numero = int(input())
    imprimevalor(numero)
