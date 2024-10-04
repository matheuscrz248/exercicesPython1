# Faça um Programa que leia três números e mostre-os em ordem decrescente ou crescente.

while True:
    sel = int(input("Digite 1 para ordenação crescente ou digite 2 para ordenação decrescente: \n"))
    if sel == 1 or sel == 2:
        break
    else:
        print("Número inválido. Por favor, digite 1 ou 2.")

quant = int(input("Quantos números serão digitados? \n"))

num = []

for i in range(quant):
    n = float(input(f"Digite o {i + 1}º número: "))
    num.append(n)

if sel == 1:
    num.sort()
    print(f"\nOs números em ordem crescente são: {num}")
elif sel == 2:
    num.sort(reverse=True)
    print(f"\nOs números em ordem decrescente são: {num}")
