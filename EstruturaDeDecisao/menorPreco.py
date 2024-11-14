"""
Faça um programa que pergunte o preço de cinco produtos e informe o produto mais barato
e o mais caro.
"""

def formata_valor(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return valor_formatado

precos = []

for i in range(1, 6):
    preco = float(input(f"Digite o preço do produto {i}: R$ "))
    precos.append(preco)

menor_preco = min(precos)
maior_preco = max(precos)
produto_mais_barato = precos.index(menor_preco) + 1
produto_mais_caro = precos.index(maior_preco) + 1

print(f"\nO produto {(produto_mais_barato)} tem o menor preço, que é R$ {formata_valor(menor_preco)}.")
print(f"\nO produto {(produto_mais_caro)} tem o maior preço, que é R$ {formata_valor(maior_preco)}.")
