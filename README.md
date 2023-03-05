# Implementação: Programação Funcional

Exemplo de aplicação da programação funcional em uma lista de números

from functools import reduce

Criando uma lista de números: 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Utilizando map para calcular o quadrado de cada número na lista:  
quadrados = list(map(lambda x: x**2, numeros))

print("Lista de números originais: ", numeros)  
print("Lista de quadrados dos números: ", quadrados)

Utilizando filter para selecionar apenas números pares na lista:  
pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Lista de números originais: ", numeros)  
print("Lista de números pares: ", pares)

Utilizando reduce para calcular a média da lista de números:  
media = reduce(lambda x, y: x + y, numeros) / len(numeros)

print("Lista de números originais: ", numeros)  
print("Média dos números: ", media)
