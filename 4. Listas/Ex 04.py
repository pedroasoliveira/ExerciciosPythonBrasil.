#4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram
# lidas. Imprima as consoantes.

lista = []
for _ in range(10):
  letra = str(input("Digite uma letra: "))
  lista.append(letra)
  for letra in lista:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
      lista.remove(letra)
print(f"Qtde de consoantes digitadas: {len(lista)}.")
print(f"As consoantes digitadas são: {lista}.")