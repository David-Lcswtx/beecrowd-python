def calculaNotas(x, nota):
    qtdNotas = int(x // nota)
    x = x % nota

    print(f"{qtdNotas} nota(s) de R$ {nota}.00")

    return x

def calculaMoedas(y, moeda):
    qtdMoedas = int((y + 0.00001) // moeda)
    y = (y + 0.00001) % moeda

    print(f"{qtdMoedas} moeda(s) de R$ {moeda:.2f}")

    return y


valor = float(input())

print("NOTAS:")

valor = calculaNotas(valor, 100)
valor = calculaNotas(valor, 50)
valor = calculaNotas(valor, 20)
valor = calculaNotas(valor, 10)
valor = calculaNotas(valor, 5)
valor = calculaNotas(valor, 2)

print("MOEDAS:")

valor = calculaMoedas(valor, 1)
valor = calculaMoedas(valor, 0.5)
valor = calculaMoedas(valor, 0.25)
valor = calculaMoedas(valor, 0.1)
valor = calculaMoedas(valor, 0.05)
valor = calculaMoedas(valor, 0.01)
