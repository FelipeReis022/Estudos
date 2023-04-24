"""Make a program that reads 3 integer values and present the greatest one 
followed by the message eh o maior."""

a, b, c = [int(x) for x in input().split()]
result = max(a, b, c)
print(result, "eh o maior")