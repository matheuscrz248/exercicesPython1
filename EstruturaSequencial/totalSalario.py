def formata_valor(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return valor_formatado

ganho = int(input("Digite o ganho por hora: \n"))
horas = int(input("Digite as horas trabalhadas no mês: \n"))

salario = ganho * horas

print(f"O salário mensal é: R$ {formata_valor(salario)}.")

