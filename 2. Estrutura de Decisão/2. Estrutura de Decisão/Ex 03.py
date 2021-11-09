#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

x = str(input("Digite o seu sexo (M para Masculino e F para Feminino): "))
if x=="M":
  print("Sexo Masculino!")
elif x=="F":
  print("Sexo Feminino!")
else:
  print("Sexo inválido!")