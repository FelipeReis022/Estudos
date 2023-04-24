while True:
    numero = int(input())
    number = []

    if numero == 0:
        break

    for n in range(1, numero + 1):
        n = str(n)
        number.append(n)
    print(" ".join(number))

