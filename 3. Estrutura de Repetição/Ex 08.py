#8. Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
for i in range(5):
  n = float(input("Digite um nº: "))
  lista.append(n)
  i += 1
print(f"O maior número é o: {sum(lista):.0f}.")
print(f"O maior número é o: {sum(lista)/len(lista):.0f}.")