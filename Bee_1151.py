def fib(numero):
    
    a,b = 0,1

    for i in range(numero):
        if i == numero -1:
            print(a)
        else:
            print(a, end=" ")
        
        c = a +b
        a = b
        b = c

numero = int(input())
fib(numero)
