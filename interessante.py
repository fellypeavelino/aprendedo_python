def relatorio(salarios):
    estudantes = salarios.keys()
    #estudantes.sort()
    for estudante in estudantes:
        print ("%-20s %12.02f" % (estudante, salarios[estudante]));

        
salarios = {'maria': 6.23, 'joão': 5.45, 'josué': 4.25}
relatorio(salarios);
