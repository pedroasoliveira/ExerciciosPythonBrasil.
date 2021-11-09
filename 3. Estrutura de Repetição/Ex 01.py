#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
  try:
    numero = int(input("Digite um número entre 0 e 10: "))
  except ValueError:
    print("Deve ser fornecido um valor inteiro!")
  else:
    if 0 <= numero <= 10:
      print(f"O número está entre 0 e 10. Parabens! Número inserido: {numero}.")
      break
    else:
      print("O número inserido nao está entre 0 e 10!")