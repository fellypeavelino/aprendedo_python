#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# init.py

class Person:
  def __init__(self,nome):
    self.nome = nome
  def alo(self):
    print ('Alô, meu nome é',self.nome)

p = Person('Pedro')

p.alo()

print ('chamando com outra sintaxe')

Person('Felipe').alo()
