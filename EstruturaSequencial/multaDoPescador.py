#Faça um programa para o João pescador. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.

def formata_valor(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return valor_formatado

peso = int(input("Digite o peso dos peixes: \n"))

if peso > 50:
    total = (peso - 50) * 4
    print(f"O valor total da multa será de R$ {formata_valor(total)}")
else:
    print("Não haverá multas a pagar.")
