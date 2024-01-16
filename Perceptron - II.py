# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:58:57 2023

@author: JUNIOR
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Neurônio Artificial = Modelo computacional inspirado pelo sistema nervoso central de um animal
#que pode realizar o aprendizado de máquina ou reconhecimento de padrões.
#Para cada rede neural existe camada conectada através de nós formando uma rede
#dot torna o código mais rápido sem necessida de for



import numpy as np 

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma (e, p):
    return e.dot(p)
#dot product / produto escalar

        
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)