import numpy as np

#Questão 1:
'''
vetor = np.random.randint(1, 101, 100)
print(f'O array gerado é: {vetor}')
print(f'O valor máximo deste array é: {vetor.max()}')
print(f'O valor mínimo deste array é: {vetor.min()}')
'''
#Questão 2:
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

#Questão 3:

#Questão 4:

#Questão 5:

#Questão 6:

#Questão 7:

#Questão 8:

#Questão 9:

#Questão 10:

#Questão 11: