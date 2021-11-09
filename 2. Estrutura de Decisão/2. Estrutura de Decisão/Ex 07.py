#7. Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
  print("O maior número digitado é num1: ", num1,"!")
elif num2 > num1 and num2 > num3:
  print("O maior número digitado é num2: ", num2,"!")
elif num2 == num1 and num2 == num3:
  print("Todos os números digitados são iguais!")
else:
  print("O maior número digitado é num3: ", num3,"!")

if num1 < num2 and num1 < num3:
  print("O menor número digitado é num1: ", num1,"!")
elif num2 < num1 and num2 < num3:
  print("O maior número digitado é num2: ", num2,"!")
elif num2 == num1 and num2 == num3:
  print("Todos os números digitados são iguais!")
else:
  print("O menor número digitado é num3: ", num3,"!")