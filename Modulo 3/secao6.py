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


# Procurar elementos numa lista 

# lista =[10,8,6,4,2]
# print( 3 in lista) # False
# print( 3 not in lista) # True

# lista = [10,3,45,78,1,0,4,12]
# var = lista[0]
# for i in lista :
#     if i < var :
#         var = i
# print(var) ****Para descobrir o numero maior de uma sequancia ******


# lista = [1,2,3,4,1,2,3,4,1,2,3,4]
# novaLista = []
# for i in lista :
#     if i not in novaLista :
#         novaLista.append(i)
# print(novaLista)

# ************ Para Fazer uma Contagem Distinta dentro de uma Lista ************

