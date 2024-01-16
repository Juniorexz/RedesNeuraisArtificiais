# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Neurônio Artificial = Modelo computacional inspirado pelo sistema nervoso central de um animal
#que pode realizar o aprendizado de máquina ou reconhecimento de padrões.
#Para cada rede neural existe camada conectada através de nós formando uma rede

entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0] 

def soma (e, p):
    s = 0
    for i in range(3):
        #print(entradas[i])
        #print(pesos[i])
        s += e[i] * p[i]
    return s
        
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)