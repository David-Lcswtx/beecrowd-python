def calculaDuracao(horaInicio, horaFim):
    
    inicio_em_minutos = horaInicio * 60
    fim_em_minutos = horaFim * 60

    diferenca = fim_em_minutos - inicio_em_minutos

    if diferenca <= 0:
        diferenca += 24 * 60

    duracaoHoras = diferenca // 60

    return duracaoHoras


entrada = input().split()

inicio = int(entrada[0])
final = int(entrada[1])

print(f"O JOGO DUROU {calculaDuracao(inicio, final)} HORA(S)")