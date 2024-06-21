#Prova Estrutura de Repetição (FOR).
#Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
#Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.
#Ao final, exiba a soma dos números pares encontrados.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

soma_pares = 0
num_pares = False

for num in range(1, 21):
    if num % 2 == 0:
        soma_pares += num
        num_pares = True

if num_pares:
    print(f"A soma dos números pares no intervalo de {n1} a {n2} é: {soma_pares}")
else:
     print(f"Não há números pares no intervalo de {n1} a {n2}.")       