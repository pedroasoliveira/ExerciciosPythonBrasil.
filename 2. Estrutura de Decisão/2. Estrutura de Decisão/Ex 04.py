#4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

x = str(input("Digite uma letra: "))
if (x=="a") or (x=="e") or (x=="i") or (x=="o") or (x=="u"):
  print("Vogal!")
else:
  print("Consoante!")