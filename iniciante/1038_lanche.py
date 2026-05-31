entrada = input().split()

opc = int(entrada[0])
qtde = int(entrada[1])

if (opc == 1):
    valor = 4.00
elif (opc == 2):
    valor = 4.50
elif (opc == 3):
    valor = 5.00
elif (opc == 4):
    valor = 2.00
elif (opc == 5):
    valor = 1.50

total =  valor * qtde

print(f"Total: R$ {total:.2f}")

# entrada = input().split()
# entrada = entrada[0], entrada[1], ..., entrada[n]