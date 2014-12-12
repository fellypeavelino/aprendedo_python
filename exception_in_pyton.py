nomedoarquivo = input("Entre com o nome do arquivo: ")
try:
    f = open (nomedoarquivo, "r")
except:
    print ("Não existe arquivo chamado", nomedoarquivo)
