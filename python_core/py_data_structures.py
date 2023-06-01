# Estruturas de Dados

class ObjectTest:

    def __init__(self):
        self.data = {1}

"""
Listas
​
1. Elas são mutáveis
2. Elas não são hasheaveis
"""

lista_diversa = [1, 2, 'a', 1.2, True, ObjectTest]
print(lista_diversa)

# poped = lista_diversa.pop(0)
# deleted = lista_diversa.remove(2)
print(lista_diversa)

lista_diversa.insert(0, 2)
print(lista_diversa)

"""
Tuplas
​
1. Elas são imutáveis
2. Elas são hasheaveis
"""

tupla_diversa_1 = (1, 2, 'a', 1.2, True, ObjectTest)
tupla_diversa_2 = (hash(tupla_diversa_1), 2, 'a', 1.2, True, ObjectTest)
print(f'tupla_diversa: {tupla_diversa_2}')

#poped = tupla_diversa.pop(0)
#deleted = tupla_diversa.remove(2)
print(f'tupla_diversa: {tupla_diversa_2}')

#tupla_diversa.insert(0, 2)
print(f'tupla_diversa: {tupla_diversa_2}')
print(f'hash tupla_diversa: {hash(tupla_diversa_2)}')

"""
Dicionários

1. Eles são conjuntos chave-valor (representam um Hash Map em Python)
2. Elas só aceitam como chave objetos hasheáveis
3. Ele não é hasheável (é mutável)
"""

dicionario_diverso = {tupla_diversa_2: lista_diversa}
print(f'dicionario_diverso: {dicionario_diverso}')
#print(f'hash dicionario_diverso: {hash(dicionario_diverso)}')

"""
Sets

1. Eles são conjuntos chave-valor (representam um Hash Map em Python)
2. Elas só aceitam como chave objetos hasheáveis
3. Ele não é hasheável (é mutável)
4. Seus elementos precisam ser hasheáveis
"""

set_diverse = {'a', 1}
print(set_diverse)

set_diverse.pop()
print(set_diverse)

#set_diverse.add(dicionario_diverso)
#print(set_diverse)

for i in range(0, 11, 2):
    set_diverse.add(i)

set_diverse.add(2)
print(set_diverse)

lista_duplicada = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8]
set_lista_duplicada = set(lista_duplicada)
print(set_lista_duplicada)
