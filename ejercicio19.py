tupla1 = (1,2,3)
tupla2 = (4,5,6,7,8,9)
tupla_contatenada = tupla1 + tupla2
print(tupla_contatenada)

tupla_repetida = tupla1 * 3
print(tupla_repetida)

tupla3 = (1,2,3,2,2,2,2,4,1,1,1)
print(tupla3.count(2))
print(tupla3.index(4))

tupla4 = (1,2,3)
tupla5 = (1,2,3)
print(tupla4==tupla5)

tupla_anidadas = (1,(2,3),(3,4,5),(7,8,9))
print(tupla_anidadas[1])
print(tupla_anidadas[2][2])