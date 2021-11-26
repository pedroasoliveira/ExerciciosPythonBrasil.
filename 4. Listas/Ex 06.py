#6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor
# a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

ficha = list()
while True:
  nome = str(input("Digite o nome do Aluno: "))
  n1 = float(input("Digite a primeira nota: "))
  n2 = float(input("Digite a segunda nota: "))
  n3 = float(input("Digite a terceira nota: "))
  n4 = float(input("Digite a quarta nota: "))
  media = (n1+n2+n3+n4)/4
  ficha.append([nome, [n1,n2,n3,n4], media ])
  resp = str(input("Quer continuar inserido notas? [S/N] "))
  if resp =="N" or resp == "n":
    break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
  resp2 = str(input("Mostrar alunos com média maior do que 7? [S/N] "))
  if resp =="N" or resp == "n":
    print("Programa finalizado! Obrigado")
    break