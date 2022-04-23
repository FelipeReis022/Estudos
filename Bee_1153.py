class Fatorial:

    def __init__(self, numero):
        numero = int(numero)
        self.resultado = 1
        if numero >= 0:
            self.numero = int(numero)
        else:
            raise ValueError("O numero deve ser maior que zero!!")
    
    def calculo(self):
        if self.numero == 0:
            self.resultado = 1
            return self.resultado
        else:
            lista = list(range(1, self.numero + 1))
            for n in lista:
                self.resultado = n * self.resultado    
            return self.resultado

    def __str__(self):
        return str(self.calculo())

numero = int(input())
numero_fatorial = Fatorial(numero)
print(numero_fatorial)

