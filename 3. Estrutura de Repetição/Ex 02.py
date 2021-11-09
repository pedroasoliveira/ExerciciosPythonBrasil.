#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e
# voltando a pedir as informações.

while True:
  usuario = str(input("Digite o seu usuário: "))
  senha = str(input("Digite sua senha: "))
  if usuario == senha:
    print("A senha não pode ser igual ao usuário: ")
  else:
    print("Usuário logado. Parabéns!")
    break