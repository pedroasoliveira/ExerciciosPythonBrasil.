#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# - o produto do dobro do primeiro com metade do segundo .
# - a soma do triplo do primeiro com o terceiro.
# - o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite o primeiro número real: "))

item_a = (2*num1)*(num2/2)
item_b = (3*num1)+num3
item_c = num3**3

print("O produto do dobro do primeiro com metade do segundo é igual a:", item_a)
print("A soma do triplo do primeiro com o terceiro é igual a:", item_b)
print("O terceiro elevado ao cubo é igual a:", item_c)