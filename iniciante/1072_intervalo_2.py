dentro = 0
fora = 0

x = []

n = int(input())

for i in range(n):
    valor = int(input())
    x.append(valor)

    if (valor >= 10 and valor <= 20):
        dentro += 1
    else:
        fora += 1

print(f"{dentro} in\n{fora} out")
