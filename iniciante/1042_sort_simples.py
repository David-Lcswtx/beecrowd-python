def sortSimples(lista):

    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    for k in range(len(lista)):
        print(lista[k])

vetor = []

entrada = input().split()

for i in range(len(entrada)):
    vetor.append(int(entrada[i]))

sortSimples(vetor)

print()

for i in range(len(entrada)):
   print(int(entrada[i]))
