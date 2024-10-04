# Faça um programa para a leitura de duas notas parciais e que verifique se está aprovado, reprovado ou de recuperação.

n1 = int(input("Digite a primeira nota: \n"))
n2 = int(input("Digite a segunda nota: \n"))

media = (n1 + n2)/2

if media >= 7:
    print(f"O aluno foi aprovado com a média {media}.")
elif media >= 5 and media <= 6:
    print(f"O aluno está de recuperação com a média {media}")
else:
    print(f"O aluno está reprovado com a média {media}")