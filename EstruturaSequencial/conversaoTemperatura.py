#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius (e vice versa).

def cel_to_fah(cel):
    fah = (cel * 9/5) + 32
    return fah

def fah_to_cel(fah):
    cel = (fah - 32) * 5/9
    return cel

def menu():
    print("Escolha uma opção de conversão de temperatura:")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Converter Fahrenreit para Celsius \n")

menu()
escolha = input()

if escolha == '1':
    cel = float(input("Digite o grau em Celsius: \n"))
    print(f"{cel} graus Celsius equivale a {cel_to_fah(cel)} graus Fahrenheit.")
elif escolha == '2':
    fah = float(input("Digite o grau em Fahrenheit: \n"))
    print(f"{fah} graus Fahrenheit equivale a {fah_to_cel(fah)} graus Celsius.")
else:
    print("Escolha inválida.")