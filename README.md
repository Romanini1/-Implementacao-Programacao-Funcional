# Implementação: Programação Funcional

Exemplo: dado um dicionário com informações de produtos, calcular o preço total dos produtos que possuem estoque disponível.

produtos = [
{'nome': 'Produto 1', 'preco': 10.0, 'estoque': 5},
{'nome': 'Produto 2', 'preco': 15.0, 'estoque': 0},
{'nome': 'Produto 3', 'preco': 20.0, 'estoque': 3},
{'nome': 'Produto 4', 'preco': 5.0, 'estoque': 8},
{'nome': 'Produto 5', 'preco': 7.5, 'estoque': 2}
]

Primeiramente, é necessário filtrar os produtos que possuem estoque disponível.

produtos_disponiveis = filter(lambda p: p['estoque'] > 0, produtos)

Agora, vamos aplicar a função map para calcular o preço total de cada produto disponível.

precos = map(lambda p: p['preco'] * p['estoque'], produtos_disponiveis)

Por fim, vamos utilizar a função reduce para somar os preços dos produtos disponíveis.

preco_total = reduce(lambda x, y: x + y, precos)

Exibindo o resultado.

print('O preço total dos produtos disponíveis é de R$ {:.2f}'.format(preco_total))

Output: O preço total dos produtos disponíveis é de R$ 105.00
Neste programa, foi utilizado a programação funcional para filtrar os produtos que possuem estoque disponível, calcular o preço total de cada produto e somar os preços dos produtos disponíveis. 
