valor = int(input())

print(valor)

def calculaValor(valor, nota):
    qtdNotas = valor // nota
    resto = valor % nota

    print(f"{qtdNotas} nota(s) de R$ {nota},00")

    return resto

valor = calculaValor(valor, 100)
valor = calculaValor(valor, 50)
valor = calculaValor(valor, 20)
valor = calculaValor(valor, 10)
valor = calculaValor(valor, 5)
valor = calculaValor(valor, 2)
valor = calculaValor(valor, 1)