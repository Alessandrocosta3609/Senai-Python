# Operações em Listas

# lista1 = [1]
# lista2 = lista1
# lista1[0] = 2
# print(lista2)

# Aqui o resultado deveria ser 1 e não 2 quando voce roda o código .


# Como resolve isso ?
# Utilizando o FATIAMENTO  faz uma cópia independente das listas e é chamado pelo simbolo [:]

#exemplo do mesmo código fatiado

# lista1 = [1]
# lista2 = lista1[:]
# lista1[0] = 2
# print(lista2)

# Agora o resultado deu 1


# lista =[10,8,6,4,2]
# novalista = lista[1:4]
# print(novalista)

# O fatiamento nesse caso , percorre o elemento 1 ao  4 , menos 1 (posição 3 na vdd)
