import math

class ConversorBinario:

    def __init__(self, decimal):
        decimal = int(decimal)
        if self.validadecimal(decimal):
            self.decimal = int(decimal)
        else:
            raise ValueError("O numero deve ser maior que zero!!")

        self.binario = []

    def validadecimal(self, decimal):

        if decimal < 0:
            return False
        else:
            return True

    def calculos(self):

        while self.decimal > 0:

            resto_divisao = math.floor(self.decimal) % 2
            self.binario.append(resto_divisao)
            self.decimal = math.floor(self.decimal / 2)

            if self.decimal == 2:
                self.binario.append(0)
                self.binario.append(1)
                break

        self.binario = [str(numero) for numero in reversed(self.binario)]
        binario_desconpactado = ' '.join(self.binario)

        return binario_desconpactado

    def contadordeum(self):
        binario_descompactado = self.calculos()
        contador = [n for n in binario_descompactado if n == '1']
        return len(contador)
        

    def __str__(self):
        
        return str(self.contadordeum())

numero = int(input())
objeto = ConversorBinario(numero)
print(objeto)
