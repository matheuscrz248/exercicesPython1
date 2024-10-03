#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

def formata_valor(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return valor_formatado

ganho = int(input("Digite o ganho por hora: \n"))
horas = int(input("Digite as horas trabalhadas no mês: \n"))

salario = ganho * horas

print(f"O salário mensal é: R$ {formata_valor(salario)}.")

