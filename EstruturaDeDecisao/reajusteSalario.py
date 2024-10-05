# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo): aumento de 20%; salários entre R$ 280,00 e R$ 1000,00: aumento de 15%
# salários de R$ 1000,00 em diante: aumento de 5%
# Após o aumento ser realizado, informe na tela: o salário antes do reajuste; o percentual de aumento aplicado; o valor do aumento; o novo salário, após o aumento

def formata_valor(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return valor_formatado

while True:
    salInicio = float(input("Digite o salário do colaborador: \nR$ "))
    if salInicio >= 0:
        break
    else:
        print(f"Digite um valor válido. \n")

if salInicio > 0 and salInicio <= 280:
    salFinal = salInicio * 1.20
    reajuste = 20

elif salInicio > 280 and salInicio <= 1000:
    salFinal = salInicio * 1.15
    reajuste = 15

elif salInicio > 1000:
    salFinal = salInicio * 1.05
    reajuste = 5

valorAumento = salFinal - salInicio

print("")
print("=-===-===-=" * 5)
print(f"Salário antes do reajuste: R$ {formata_valor(salInicio)}.")
print(f"Percentual do reajuste a ser aplicado: {reajuste}%.")
print(f"Valor do aumento a ser aplicado: R$ {formata_valor(valorAumento)}.")
print(f"Salário após o reajuste: R$ {formata_valor(salFinal)}.")
print("=-===-===-=" * 5)