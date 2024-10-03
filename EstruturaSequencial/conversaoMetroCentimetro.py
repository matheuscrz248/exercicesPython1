#Faça um Programa que converta metros para centímetros.

def cm_para_metro(cm):
    return cm / 100

def metro_para_cm(metro):
    return metro * 100

def menu():
    print("Escolha uma opção:")
    print("1 - Converter de centímetros para metros")
    print("2 - Converter de metros para centímetros \n")

menu()
escolha = input()

if escolha == '1':
    cm = float(input("Digite o valor em centímetros: \n"))
    print(f"{cm} cm equivale a {cm_para_metro(cm)} metros.")
elif escolha == '2':
    metro = float(input("Digite o valor em metros: \n"))
    print(f"{metro} metros equivale a {metro_para_cm(metro)} centímetros.")
else:
    print("Escolha inválida.")
