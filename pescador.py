"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
e verifique se há excesso. Se houver, gravar na variável excesso
e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
"""

__author__ = 'rmaues'

regular = 50.0

multa = 4.00

pescado = float(input("Quantos kilos você pescou ? "))

if pescado <= regular:
    print ("Você não terá que pagar nada, esta tudo regular.")
else:
    print ("Você pescou", pescado, "kg e pagará R$",(pescado - regular) * multa, "em multa, pois pescou", (pescado - regular), "kg cima do peso regular.")