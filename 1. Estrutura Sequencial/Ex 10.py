#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temp_celsius = float(input("Digite a temperatura em Celsius:"))
temp_faren = ((9/5)*temp_celsius+32)
print("A temperatura em Farenheit é de", temp_faren,".")