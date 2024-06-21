#Crie um programa que solicite 10 números para o usuário. O programa deve somar todos os números múltiplos de 6.

soma = 0

for i in range(1, 11):
    numero = int(input("Digite um número: "))
    if numero % 6 == 0:
        soma += numero
        if soma >= 30:
            break

print(f"A soma é {soma}: ")        