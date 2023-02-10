name = str(input())
fixed_salary = float(input())
sales = float(input())

result = ((sales * 15) / 100) + fixed_salary
print(f"TOTAL = R$ {result:.2f}")