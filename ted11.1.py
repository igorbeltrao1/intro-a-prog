import random

matriz_a = []

for i in range(10):
    
    matriz2 = []
    
    for j in range(10):    
        matriz2.append(random.randint(0, 100))
    
    matriz_a.append(matriz2)        

for linha in matriz_a:
    print(linha)
    
print('\n \n')
    


resultado_soma = 0

for l in matriz_a:
    
    for c in l:
        
        resultado_soma += c

print(f'Resultado da Soma = {resultado_soma}')
print('\n')

matrizB = []

for l in range(0, len(matriz_a)):
    
    lista_auxiliar = []
    
    for c in range(0, len(matriz_a[l])):
        
        resultado_multiplicacao = matriz_a[l][c] * 3
        lista_auxiliar.append(resultado_multiplicacao)
        
    matrizB.append(lista_auxiliar)
        
print(matrizB)