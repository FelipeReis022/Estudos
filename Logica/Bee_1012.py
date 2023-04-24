""""
Exercicio:
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.
"""

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

triangle = (a * c) / 2
circle = 3.14159 * (c * c)
trapezium = ((a + b) * c) / 2
square = b * b
rectangle = a * b

print(f"TRIANGULO: {triangle:.3f}\nCIRCULO: {circle:.3f}\n"
      f"TRAPEZIO: {trapezium:.3f}\nQUADRADO: {square:.3f}\n"
      f"RETANGULO: {rectangle:.3f}")
