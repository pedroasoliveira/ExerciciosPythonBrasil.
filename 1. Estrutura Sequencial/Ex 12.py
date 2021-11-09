#12. Tendo como dados de entrada a altura de uma pessoa, construa
#um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

peso_ideal = round((72.7*altura)-58,1)

print("O seu peso ideal é", peso_ideal,"quilos!")