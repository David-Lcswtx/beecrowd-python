entrada = input().split()

nota1 = float(entrada[0])
nota2 = float(entrada[1])
nota3 = float(entrada[2])
nota4 = float(entrada[3])

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / 10

print(f"Media: {media:.1f}")

if (media >= 7.0):
    print("Aluno aprovado.")
elif (media < 5.0):
    print("Aluno reprovado.")
elif (media >= 5.0 and media <= 6.9):
    print("Aluno em exame.")

    notaExame = float(input())
    print(f"Nota do exame: {notaExame}")

    mediaFinal = (media + notaExame) / 2

    if (mediaFinal < 5.0):
        print("Aluno reprovado.")
        print(f"Media final: {mediaFinal:.1f}")
    elif (mediaFinal >= 5.0):
        print("Aluno aprovado.")
        print(f"Media final: {mediaFinal:.1f}")
