entrada1 = input().split()
entrada2 = input().split()

codigoPc1 = int(entrada1[0])
numeroPc1 = int(entrada1[1])
valorUnitPc1 = round(float(entrada1[2]), 2)

codigoPc2 = int(entrada2[0])
numeroPc2 = int(entrada2[1])
valorUnitPc2 = round(float(entrada2[2]), 2)

valorFinal = (numeroPc1 * valorUnitPc1) + (numeroPc2 * valorUnitPc2)

print(f"VALOR A PAGAR: R$ {valorFinal:.2f}")
