salario_hora = float(input("Digite se salário por hora: "))
horas_trabalhadas = float(input("Digite a qtd de horas trabalahdas: "))

salario_bruto = salario_hora * horas_trabalhadas

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

descontos = imposto_renda + inss + sindicato

salario_liquido = salario_bruto - descontos

print(f"Salário Bruto: R${salario_bruto}\nIR(11%: R${imposto_renda}\nINSS(8%): R${inss}\n Sindicato: R$(5%))")

