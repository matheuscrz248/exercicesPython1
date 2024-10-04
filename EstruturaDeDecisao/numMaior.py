# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input("Digite o primeiro número: \n"))
n2 = int(input("Digite o segundo número: \n"))

if n1 > n2:
    print(f"O maior número é: {n1}")
elif n2 > n1:
    print(f"O maior número é: {n2}")
else:
    print(f"Os números {n1} e {n2} são iguais.")





