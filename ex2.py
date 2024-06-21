numero_secreto = 99
tentativa = 0
tentativas_max = 5

while tentativa != numero_secreto and tentativas_max:
    tentativa = int(input("Advinhe o número: "))
    tentativas_max -= 1
    if tentativa < numero_secreto:
        print("Tentativva muito baixa")
    elif tentativa > numero_secreto:
        print("Tentativa muito alta")

if tentativa == numero_secreto:
    print("Parabéns")
else:
    print("Tentativas acabaram")        


