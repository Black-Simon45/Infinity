nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite outra nota: "))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("Aprovado")
elif media == 10:
    print("Aprovado com distinçaõ")
else:
    print
    ("Reprovado")        