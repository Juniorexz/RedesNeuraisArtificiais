# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:17:33 2023

@author: JUNIOR
"""

#sigmoid Não retorna valores negativos

import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

#a = np.exp(-1)
#b = np.exp(0)
#c = np.exp(1)
#d = np.exp(2)

a = sigmoid(0)
b = np.exp(0)