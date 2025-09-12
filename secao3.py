# Operadores aritméticos: +, -, *, /, ** (adição, subtração, multiplicação, divisão, potenciação)

print(3+4)  # Adição
print (2+4.57) # Adição com float
print(-11+9.1) # Adição com número negativo
print(-5.98-285.7) # Subtração com float negativo
print(.1-0.10) # Subtração com float


print(3*5) # Multiplicação
print(3*5.0) # Multiplicação com float
print(2*-3) # Multiplicação com número negativo

print(6/2) # Divisão
print(7/2) # Divisão com resultado float
print(7/2.0) # Divisão com float    
print(7/2.0) # Divisão com float    


print(2**2) # Potenciação
print(2**3) # Potenciação
print(2**0.5) # Potenciação com float
print(9**0.5) # Potenciação com float
print(2**(2+2)) # Potenciação com adição
print((2+2)**2) # Potenciação com adição e parênteses
print(25**0.5) # Calcuar a Raiz Quadrada
print(25**(1/2)) # Calcuar a Raiz Quadrada
print(27**(1/3)) # Calcuar a Raiz Cúbica

print((2**2+2**2)**0.5) # Teorema de Pitágoras
print(((2**2)+(2**2))**0.5) # Teorema de Pitágoras com parênteses

print(2+3*5) # Ordem de precedência
print((2+3)*5) # Ordem de precedência com parênteses

# Operadores de atribuição: =, +=, -=, *=, /=, **= (atribuição simples, adição, subtração, multiplicação, divisão, potenciação)

print(10/2) # Atribuição simples 
print(11/.012) # Atribuição simples com float
print(10//2) # Atribuição simples com resultado inteiro
print(11//.012) # Atribuição simples com float e resultado inteiro
print(type(11//.012)) # Verificando o tipo do resultado inteiro
print(type(10//2)) # Verificando o tipo do resultado inteiro
# Não existe Divisão por zero
#print(10/0) # Atribuição simples com divisão por zero

print(10%2) # Resto da divisão
print(1211%14) # Resto da divisão com resultado diferente de zero
print(11%3) # Resto da divisão com resultado diferente de zero

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) # Resultado -0.5 0.5 0 -1
print((2 % -4), (2 % 4), (2 ** 3 ** 2)) # Resultado -2 2 512

#Prioridade dos operadores: 1º Parênteses, 2º Potenciação, 3º Multiplicação e Divisão, 4º Adição e Subtração
print(3 + 6 * 2 ** 2 - (1 + 2)) # Resultado 26
print(3 + 6 * 2 ** 2 - 1 + 2) # Resultado 28
print(3 + 6 * 4 - 1 + 2) # Resultado 28
print(3 + 24 - 1 + 2) # Resultado 28


print((5*((25 % 13) + 100) / (2 * 13)) // 2) # Resultado .

print(5*(112)/(26)//2) # Resumo do Calculo anterior .     

print(3*(2,4,6)) # Isso é uma tupla , não é uma lista
print(3*[2,4,6]) # Isso é uma lista , não é uma tupla
