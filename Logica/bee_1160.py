import math

class Populacao():
    """ Recebe 2 quantidades populacionais
     e suas respectivas taxas de crescimento
    """

    def __init__(self, populacao_1, populacao_2, taxa_crescimento_1, taxa_crescimento_2) -> None:
        self.populacao_1 = int(populacao_1)
        self.populacao_2 = int(populacao_2)
        self.taxa_crescimento_1 = float(taxa_crescimento_1)
        self.taxa_crescimento_2 = float(taxa_crescimento_2)
        self.anos = 0

    def calculo(self) -> int:
        """ Retorna em quantos anos a população 1 vai ficar maior que a 2"""

        while self.populacao_1 <= self.populacao_2:
            self.anos += 1
            self.populacao_1 = math.floor((self.populacao_1 * (self.taxa_crescimento_1 / 100)) + self.populacao_1)
            self.populacao_2 = math.floor((self.populacao_2 * (self.taxa_crescimento_2 / 100)) + self.populacao_2)
            if self.anos > 100:
                break
        return self.anos

    def __str__(self) -> str:
        if self.calculo() > 100:
            return "Mais de 1 seculo."
        else:
            return f'{self.calculo()} anos.'

numero_testes = int(input())

while numero_testes > 0:
    numero_testes -= 1
    populacao_a, populacao_b, crescimento_a, crescimento_b = input().split()
    objeto = Populacao(populacao_a, populacao_b, crescimento_a, crescimento_b)
    print(objeto)
    
# while numero_testes > 0:
#     numero_testes -= 1
#     populacao_a, populacao_b, crescimento_a, crescimento_b = input().split()
#     populacao_a = int(populacao_a)
#     populacao_b = int(populacao_b)
#     crescimento_a = float(crescimento_a)
#     crescimento_b = float(crescimento_b)
#     anos = 0
#     while populacao_a <= populacao_b:
#         anos += 1
#         populacao_a = math.floor((populacao_a * (crescimento_a / 100)) + populacao_a)
#         populacao_b = math.floor((populacao_b * (crescimento_b / 100)) + populacao_b)
#         if anos > 100:
#             break

#     if anos > 100:
#         print("Mais de 1 seculo")
#     else:    
#         print(f'{anos} anos.')
