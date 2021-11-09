#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

l = float(input("Digite a medida do lado do quadrado, em centímetros: "))
area_quadrado = l**2
print(f"A área do quadrado é de {round(area_quadrado,2)} centímetros quadrados! ")
print(f"Podemos dizer também que o dobro da área desse quadrado é {area_quadrado*2} centímetros quadrados!")