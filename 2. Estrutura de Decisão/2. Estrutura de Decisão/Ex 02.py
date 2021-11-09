#2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = float(input("Digite o primeiro número: "))
if n1>0:
  print("O número digitado é positivo!")
elif n1==0:
   print("O número é nulo!")
else:
  print("O número digitado é negativo!")