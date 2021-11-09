#3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista = []
for _ in range(4):
  numero = int(input("Digite uma nota: "))
  lista.append(numero)
  media = sum(lista) / len(lista)
print(f"As notas digitadas são: {lista}.")
print(f"A média das notas é: {media}.")