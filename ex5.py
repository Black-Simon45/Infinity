numero_secreto = 10
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Advinhe o número: "))
    if tentativa < numero_secreto:
        print("Tentativa muito baixa")
    elif tentativa > numero_secreto:
        print("Tentativa muito alta")
print("Parabéns")