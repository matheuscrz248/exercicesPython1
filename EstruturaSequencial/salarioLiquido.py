#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.

def formata_valor(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return valor_formatado

ganhoHora = int(input("Digite o ganho por horas trabalhadas: \n"))
hTrabalhadas = int(input("Digite o número de horas trabalhadas no mês: \n"))

salBruto = ganhoHora * hTrabalhadas
ir = (salBruto * 11) / 100
inss = (salBruto * 8) / 100
sindi = (salBruto * 5) / 100
salLiquido = salBruto - (ir + inss + sindi)

print("")
print(f"Salário bruto: R$ {formata_valor(salBruto)}")
print(f"IR (11%): R$ {formata_valor(ir)}")
print(f"INSS (8%): R$ {formata_valor(inss)}")
print(f"Sindicato (5%): R$ {formata_valor(sindi)}")
print(f"Salário líquido: R$ {formata_valor(salLiquido)}")
