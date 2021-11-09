#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
# comprar, sabendo que a decisão é sempre pelo mais barato.

preco_prod1 = float(input("Digite o preço do produto 1: "))
preco_prod2 = float(input("Digite o preço do produto 2: "))
preco_prod3 = float(input("Digite o preço do produto 3: "))

if preco_prod1 == preco_prod2 and preco_prod1 == preco_prod3 and preco_prod2 == preco_prod3:
  print("Todos os produtos possuem preços iguais.")
else:
  if preco_prod1 < preco_prod2 and preco_prod1 < preco_prod3:
    print("Compre o produto 1, pois o mesmo é o mais barato!")
  elif preco_prod2 < preco_prod1 and preco_prod2 < preco_prod3:
    print("Compre o produto 2, pois o mesmo é o mais barato!")
  else:
    print("Compre o produto 3, pois o mesmo é o mais barato!")