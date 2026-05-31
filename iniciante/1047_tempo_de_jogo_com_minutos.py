def calculaDuracao(horaInicio, minutoInicio, horaFim, minutoFim):

    inicio_em_minutos = horaInicio * 60 + minutoInicio
    fim_em_minutos = horaFim * 60 + minutoFim

    diferenca = fim_em_minutos - inicio_em_minutos

    if diferenca <= 0:
        diferenca += 24 * 60

    duracaoHoras = diferenca // 60
    duracaoMinutos = diferenca % 60
    
    return duracaoHoras, duracaoMinutos

entrada = input().split()

inicioHora = int(entrada[0])
inicioMin = int(entrada[1])
finalHora = int(entrada[2])
finalMin = int(entrada[3])

duracaoH, duracaoM = calculaDuracao(inicioHora, inicioMin, finalHora, finalMin)

print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoM} MINUTO(S)")