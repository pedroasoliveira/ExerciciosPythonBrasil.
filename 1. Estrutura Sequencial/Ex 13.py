#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# - Para homens: (72.7*h) - 58
# - Para mulheres: (62.1*h) - 44.7s

altura = float(input("Digite sua altura em metro: "))
sexo = str(input("Digite o sexo: "))

peso_ideal_masc = (72.7*altura)-58
peso_ideal_fem = (62.1*altura)-44.7

if sexo == 'masculino':
    print("Seu peso ideal é de", round(peso_ideal_masc,2))
else:
    print("Seu peso ideal é de", round(peso_ideal_fem,2))