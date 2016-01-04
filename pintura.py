"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
__author__ = 'rmaues'

vlrLata = 80.00

lata = 18

area = float(input("Qual é o tamanho da área que quer pintar ? (em m2) "))

if area <= 54:
    print ("Você precisara de apenas um lata, e custara R$ 80,00")
else:
    qntLitros = area / 3
    if qntLitros <= 18:
        print ("Apenas uma lata e pagará R$ 80.00")
    else:
        qntLatas = (area / 3) / 18
        print ("Você vai usar ", qntLatas, "latas e pagará R$ ", qntLatas * vlrLata)