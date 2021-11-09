#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme
# e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9)

temp_faren = float(input("Digite a temperatura em Farenheit:"))
temp_celsius = round(5*((temp_faren-32)/9),1)

print("A temperatura em Celsius é de", temp_celsius,".")