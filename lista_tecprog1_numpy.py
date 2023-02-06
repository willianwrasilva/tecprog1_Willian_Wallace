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
    modulo_quadratico = arr*arr
    soma = 0
    for i in modulo_quadratico:
        soma += i 
    modulo_vetor = soma**(1/2)

    return modulo_vetor

print(f'O módulo do vetor é: {modulo_vetor(vetor1)}')
'''
#Questão 3:
'''
y_prediction = np.random.randint(1,10, 3)
y_i = np.random.randint(1,10, 3)

print(f'O vetor y_prediction é: {y_prediction}')
print(f'O vetor y_i é: {y_i}')

def calculate_eqm(arr1, arr2):
    soma = 0
    for i in range(len(arr1)):
        diferenca = (arr1[i] - arr2[i])**2
        soma += diferenca
    return soma/len(arr1)

print(f'O erro quadrático médio é: {calculate_eqm(y_prediction, y_i)}')
'''
#Questão 4:
'''
linhas_4 = int(input('Digite o número de linhas: '))
colunas_4 = int(input('Digite o número de colunas: '))

matriz_4 = np.ones((linhas_4, colunas_4), dtype= int)
matriz_4[1:(linhas_4 - 1),1:(colunas_4 - 1)] = 0

print(matriz_4)
'''
#Questão 5:
linhas_5 = int(input('Digite o número de linhas: '))
colunas_5 = int(input('Digite o número de colunas: '))
linha = np.array(np.zeros(linhas_5, dtype = int))
coluna = np.array(np.zeros(colunas_5, dtype = int))
matriz_5 = np.random.randint(1, 21, size = (linhas_5, colunas_5))
nova_matriz_5 = np.append(matriz_5, [linha], axis = 0)
nova1_matriz_5 = np.append(nova_matriz_5, [coluna], axis = 1)

print(matriz_5)
print(nova_matriz_5)
print(nova1_matriz_5)
#Questão 6:

#Questão 7:

#Questão 8:

#Questão 9:

#Questão 10:

#Questão 11: