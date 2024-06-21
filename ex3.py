n1 = float(input("Insira um número: "))
n2 = float(input("Insira um número: "))
n3 = float(input("Insira um número: "))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(n1, n2, n3)
    else:
        print(n1, n3, n2) 
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)               