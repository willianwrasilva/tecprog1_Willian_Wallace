import numpy as np

#Questão 1:
'''
vetor = np.random.randint(1, 101, 100)
print(f'O array gerado é: {vetor}')
print(f'O valor máximo deste array é: {vetor.max()}')
print(f'O valor mínimo deste array é: {vetor.min()}')
'''
#Questão 2:
'''
quantidade = int(input('Qual a dimensão do vetor: '))
vetor1 = np.random.randint(1,100, quantidade)
print(f'O vetor gerado pelo numpy é: {vetor1}')

def modulo_vetor(arr):
    modulo_quadratico = np.sqrt(sum(arr**2))
    return modulo_quadratico

print(f'O módulo do vetor é: {modulo_vetor(vetor1)}')
'''
#Questão 3:
'''
y_prediction = np.random.randint(1,10, 3)
y_i = np.random.randint(1,10, 3)


print(f'O vetor y_prediction é: {y_prediction}')
print(f'O vetor y_i é: {y_i}')

def calculate_eqm(arr1, arr2):
    diferenca = (arr1 - arr2)**2
    erro_quadratico_medio = diferenca.sum()/np.size(arr1)
          
    return erro_quadratico_medio

print(f'O erro quadrático médio é: {calculate_eqm(y_prediction, y_i)}')
'''
#Questão 4:
'''
linhas_4 = int(input('Digite o número de linhas: '))
colunas_4 = int(input('Digite o número de colunas: '))

def matriz_borda_um_nucleo_zero(linha, coluna):
    matriz_4 = np.ones((linha, coluna), dtype= int)
    matriz_4[1:(linha - 1),1:(coluna - 1)] = 0
    return matriz_4

print(f'A matriz é: \n{matriz_borda_um_nucleo_zero(linhas_4, colunas_4)}')
'''
#Questão 5:
'''
linhas_5 = int(input('Digite o número de linhas: '))
colunas_5 = int(input('Digite o número de colunas: '))
matriz_5 = np.random.randint(1, 21, size = (linhas_5, colunas_5))

def matriz_borda_zero(matriz):
    linha_zeros = np.array(np.zeros((1, matriz.shape[1]), dtype = int))
    coluna_zeros = np.array(np.zeros((matriz.shape[0]+2, 1), dtype = int))

    nova_matriz_5 = np.concatenate((linha_zeros, matriz))
    nova_matriz_5 = np.concatenate((nova_matriz_5, linha_zeros))
    nova_matriz_5 = np.concatenate((coluna_zeros, nova_matriz_5), axis = 1)
    nova_matriz_5 = np.concatenate((nova_matriz_5, coluna_zeros), axis = 1)

    return nova_matriz_5

print(f'Matriz inicial: \n{matriz_5}')
print(f'Matriz final: \n{matriz_borda_zero(matriz_5)}')
'''
#Questão 6:

#Questão 7:

#Questão 8:
'''
vetor_8 = np.arange(1,22,2)
print(vetor_8)
'''
#Questão 9:
'''
vetor_9 = np.random.rand(10)
print(vetor_9)
'''
#Questão 10:
'''
vetor_10 = np.random.rand(30)

def normaliza_dados(vetor):
    normalizacao = (vetor - np.mean(vetor))/np.std(vetor)
    return normalizacao

print(f'O vetor original é: \n {vetor_10}')
print(f'O vetor normalizado é: \n {normaliza_dados(vetor_10)}')
'''

#Questão 11: