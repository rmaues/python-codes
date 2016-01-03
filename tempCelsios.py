# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).
__author__ = 'rmaues'

f = float(input("Qual a temperatura em Farenheit que quer converter ? "))

print (f, "Farenheit é igual a ", (5*(f-32))/9, "celsios.")
