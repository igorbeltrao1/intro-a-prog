from operator import truediv
from random import random
import random
from typing import Counter


#chamando a função "random.randint" para gerar números aleátórios de 0 à 40 e printa a lista
num = [random.randint(0, 50) for x in range (50)]
contador = Counter(num)
print (f'a lista criada foi essa: {num}')

rep =  [
    item for item, quantidade in contador.items()
    if quantidade > 1
]
repetidos_num = len(rep)

for i in range(0, len(num)):
    
    for j in range(0, len(num)):
        
        if num[i] == num[j] and i != j:
            print(f'Índice: {j} | Valor: {num[j]} \n')


print(f'Há {repetidos_num} números na lista')
print(f'Os numeros repetidos são {rep}')
