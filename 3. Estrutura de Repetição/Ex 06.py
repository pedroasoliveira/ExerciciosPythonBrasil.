#6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o
# programa para que ele mostre os números um ao lado do outro.

n = int(input("Digite a quantidade de números desejados (de 1 a 20): "))
def imp_numeros (n: int):
  for i in range (1, n + 1):
      print(i, end="   ")

imp_numeros(n)