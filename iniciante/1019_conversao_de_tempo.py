n = int(input())

def calculaTempo(duracao):
    
    horas = duracao // 3600
    minutos = (duracao % 3600) // 60
    segundos = duracao % 60

    print(f"{horas}:{minutos}:{segundos}")

calculaTempo(n)