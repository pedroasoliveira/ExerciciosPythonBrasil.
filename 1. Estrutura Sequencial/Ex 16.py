#16.  um programa para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada. Considere que a
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
# de latas de tinta a serem compradas e o preço total.

area_pintada = float(input("Digite a medida da área a ser pintada, em metros quadrados: "))
qtde_tinta_necessária = area_pintada/3
qtde_lt_18litros = round(qtde_tinta_necessária/18,0)
preço_lt_18litros = 80.0

print("Qtde de latas necessárias:", qtde_lt_18litros,"; Valor Total em R$:", preço_lt_18litros*qtde_lt_18litros,"." )