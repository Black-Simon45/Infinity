n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))

if n1 > n2 and n1 > n3:
    print(f"O maior numero é{n1}")
elif n1 > n3 and n1 < n3:
    print(f"O maior número é {n3}")
elif n3 > n2:
    print(f"O maior número é {n3}")
else:
    print(f"O maior número é {n2}")        