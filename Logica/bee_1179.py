numero_testes = 15
par = []
impar = []
index_par = 0
index_impar = 0

while numero_testes > 0:
    numero = int(input())
    numero_testes -= 1

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

    if len(par) == 5:
        for num in par:
            print(f'par[{index_par}] = {num}')
            index_par += 1
        par.clear()

    if len(impar) == 5:
        for num in impar:
            print(f'impar[{index_impar}] = {num}')
            index_impar += 1
        impar.clear()

index_impar = 0
index_par = 0

for num in impar:
    print(f'impar[{index_impar}] = {num}')
    index_impar += 1

for num in par:
    print(f'par[{index_par}] = {num}')
    index_par += 1
