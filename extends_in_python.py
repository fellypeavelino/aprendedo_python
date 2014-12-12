#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

class MembroDaEscola:
  '''Representa qualquer membro da escola.'''
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    print ('(Inicializando membro: %s)' % self.nome)

  def exibe2(self):
      '''Exibe meus detalhes.'''
      print ('Nome:"%s" Idade:"%s"' % (self.nome, self.idade))

class Professor(MembroDaEscola):
  '''Representa um professor.'''

  def __init__(self, nome, idade, salario):
    MembroDaEscola.__init__(self, nome, idade)
    self.salario = salario
    print ('(Inicializando Profesor: %s)' % self.nome)

  def exibe(self):
    MembroDaEscola.exibe(self)
    print ('Salário: "%d"' % self.salario)

class Estudante(MembroDaEscola):
     #Representa um estudante.
  def __init__(self, nome, idade, nota):
    MembroDaEscola.__init__(self, nome, idade)
    self.nota = nota
    print ('(Inicializando Estudante: %s)' % self.nome)

  def exibe(self):
    MembroDaEscola.exibe(self)
    print ('Nota: "%d"' % self.nota)

p = Professor('Mr. Swaroop', 22, 30000)
e = Estudante('Samuel', 38, 75)

print # imprime uma linha em branco

membros = [p, e]
for membro in membros:
  membro.exibe2() # trabalha para ambos: Professores e Estudantes
