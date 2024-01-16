# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:58:23 2023

@author: JUNIOR
"""

import numpy as np

#Operador AND
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,0,0,1])

#Operador OR
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,1,1,1])

#Operador XOR
#Para esse problema não vai alcançar o 100% por isso nunca chega ao resultado
#XOR não é linearmente separável(não é simples)(Não é possível separar reta de classe)
 
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,1,1,0])
pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)


def treinar():
    erroTotal = 1
    while (erroTotal  != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado ' + str(pesos[j]))
        print('Total de erros ' + str(erroTotal))
        
treinar()
print('Rede neural treinada')
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))