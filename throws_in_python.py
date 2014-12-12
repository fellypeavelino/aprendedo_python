class ErroNumeroRuim(Exception):
    pass
def entraNumero():
    x = int(input ("Escolha um número: "))
    if x == 17:
        raise ErroNumeroRuim("17 é um número ruim")
    return x

try:
   entraNumero();
except:
    print('throws');
