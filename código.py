from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = list(map(lambda x: x**2, numeros))

print("Lista de números originais: ", numeros)
print("Lista de quadrados dos números: ", quadrados)

pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Lista de números originais: ", numeros)
print("Lista de números pares: ", pares)

media = reduce(lambda x, y: x + y, numeros) / len(numeros)

print("Lista de números originais: ", numeros)
print("Média dos números: ", media)
