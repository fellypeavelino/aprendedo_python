class Horario:
    pass
def somaHorario(h1, h2):
    soma = Horario()
    soma.horas = h1.horas + h2.horas
    soma.minutos = h1.minutos + h2.minutos
    soma.segundos = h1.segundos + h2.segundos
    return soma;

print(somaHorario(11, 10));
