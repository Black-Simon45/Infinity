#Projeto 2

senha = input("Digite a senha: ")
confirmacao = None

while senha != confirmacao:
    confirmacao = input("Confirme a senha: ")

    if senha == confirmacao:
        print("Senha correta. Bem Vindo")
    else: 
        print("Senha incorreta. Tente novamente")    