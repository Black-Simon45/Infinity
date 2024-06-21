#Crie um programa que solicite ao usuário que digite números inteiros.

limite = 50
soma_pares = 0

while soma_pares < limite:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        soma_pares += numero
    if soma_pares >= limite:
        break

print(f"A soma total é {soma_pares}")    