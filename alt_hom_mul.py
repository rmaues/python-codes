"""
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

"""
__author__ = 'rmaues'

alt = float(input("Qual a sua altura ?"))
sexo = input("Qual o seu sexo ?(Use maculino/femenino ou m/f)")

if sexo == "masculino" or sexo == "m":
    print ("Seu peso ideal é de : ", (72.7*alt)-58)
else:
    print ("Seu peso ideal é de : ", (62.1*alt)-44.7)