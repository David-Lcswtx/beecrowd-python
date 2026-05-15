nome = input()
salarioFixo = round(float(input()), 2)
vendasMes = round(float(input()), 2)

total = salarioFixo + (vendasMes * 0.15)

print(f"TOTAL = R$ {total:.2f}")
