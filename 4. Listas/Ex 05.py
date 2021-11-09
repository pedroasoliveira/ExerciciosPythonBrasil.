#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
# números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista = []
lista_par = []
lista_imp = []
for _ in range(20):
  numero = int(input("Digite um número: "))
  lista.append(numero)
  if numero % 2 == 0:
    lista_par.append(numero)
  else:
    lista_imp.append(numero)

print(f"\nOs números digitados foram: {lista}.")
print(f"Os números pares digitados foram: {lista_par}.")
print(f"Os números ímpares digitados foram: {lista_imp}.")