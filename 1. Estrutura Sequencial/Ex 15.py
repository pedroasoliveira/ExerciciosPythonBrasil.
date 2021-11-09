#15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que
# nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato.
# o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# - Salário Bruto :
# - IR (11%) :
# - INSS (8%) :
# - Sindicato ( 5%) :
# = Salário Liquido :
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salario_hora = float(input("Digite o valor/hora do salário: "))
horas_mes = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_total = salario_hora*horas_mes
salario_liquido = round((salario_total-(salario_total*0.11)-(salario_total*0.08)-(salario_total*0.05)),2)

print("Salário Bruto: R$", salario_total)
print("IR (11%): R$", salario_total*0.11)
print("INSS (8%): R$", round(salario_total*0.08,0))
print("Sindicato (5%): R$", round(salario_total*0.05,2))
print("Salário Líquido: R$", salario_liquido)