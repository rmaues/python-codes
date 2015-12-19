__author__ = 'rmaues'

import random

def pergunta(resposta):
    if resposta == 1:
        return 'Com certeza'
    elif resposta == 2:
        return 'Pode ser'
    elif resposta == 3:
        return 'Muito duvidoso'

r = random.randint(1,3)

sorte = pergunta(r)

print (sorte)
