"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

def formata_valor(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return valor_formatado

while True:
    nome = input("Digite o nome:\n")

    if len(nome) > 3:
        break
    else:
        print("Nome inválido, o nome deve ter mais de 3 caracteres.\n")


while True:
    idade = int(input("Digite a idade:\n"))

    if idade > 0 and idade <= 150:
        break
    else:
        print("Idade inválida, a idade deve ser entre 0 e 150 anos.\n")


while True:
    salario = float(input("Digite o salário:\n"))

    if salario > 0:
        break
    else:
        print("Salário inválido, o salário deve ser maior que 0.\n")


while True:
    sexo = input("Digite o sexo ('f' para feminino ou 'm' para masculino):\n").lower()

    if sexo in ["m", "f"]:
        break
    else:
        print("Sexo inválido, digite 'f' ou 'm'.\n")

sexoFinal = {"m": "Masculino", "f": "Feminino"}[sexo]


while True:
    estadoCivil = input("Digite o estado civil ('s' para solteiro(a), 'c' para casado(a), 'v' para viúvo(a) ou 'd' para divorciado(a)):\n").lower()

    if estadoCivil in ["s", "v", "c", "d"]:
        break
    else:
        print("Estado civil inválido, digite 's', 'c', 'v' ou 'd'.\n")

estadoCivilMapa = {
    ("s", "m"): "Solteiro",
    ("s", "f"): "Solteira",
    ("c", "m"): "Casado",
    ("c", "f"): "Casada",
    ("v", "m"): "Viúvo",
    ("v", "f"): "Viúva",
    ("d", "m"): "Divorciado",
    ("d", "f"): "Divorciada",
}

estadoCivilFinal = estadoCivilMapa[(estadoCivil, sexo)]

print("")
print("=-===-===-=" * 5)
print(f"Nome: {nome}.")
print(f"Idade: {idade}.")
print(f"Salário: R$ {formata_valor(salario)}.")
print(f"Sexo: {sexoFinal}.")
print(f"Estado civil: {estadoCivilFinal}.")
print("=-===-===-=" * 5)



