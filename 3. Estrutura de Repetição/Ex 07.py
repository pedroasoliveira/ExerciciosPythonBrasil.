#7. Faça um programa que leia 5 números e informe o maior número.

lista = []
for i in range(5):
  n = float(input("Digite um nº: "))
  lista.append(n)
  i += 1
print(f"O maior número é o: {max(lista):.0f}.")