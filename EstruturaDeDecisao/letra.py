# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: \n").lower()

if len(letra) == 1 and letra.isalpha():

    if letra in 'aeiou':
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")
else:
    print("Digite apenas uma letra válida.")
