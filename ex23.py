#Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.

#while true:
    #n1 = int(input("Digite um núemro: "))
    #n2 = int(input("Digite um núemro: "))

    #soma = n1 + n2

    #print(soma)

    #continuar = input("Deseja continuar? S ou N")

    #if continuar == "N":
        #break


limite = 25

while soma < limite:
    numero = int(input("Digite um número: "))
    soma += numero

    print(f"A soma ultrapassou o limite de {limite}. Soma final: {soma}")    