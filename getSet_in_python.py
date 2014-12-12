class Person:
    def setNome(self,nome):
        self.nome = nome;
        return self.nome;
        

p = Person();
print(p.setNome('pedro'));

