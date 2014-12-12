def posicoesQueIniciamCom(lista, letra='a'):
    result = []
    for i, palavra in enumerate(lista):
        if palavra.startswith(letra):
            result.append(i)
    return result

nomes = ['abc', 'hua', 'aaa', 'asdfg', 'bnm'];
print (posicoesQueIniciamCom(nomes));
