code1, units1, price1 = input().split()
code2, units2, price2 = input().split()

units1 = int(units1)
units2 = int(units2)
price1 = float(price1)
price2 = float(price2)

result = (units1 * price1) + (units2 * price2)
print(f"VALOR A PAGAR: R$ {result:.2f}")
