# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:30:37 2024

@author: JUNIOR
"""

#fit = encaixar no caso entradas e saidas
#activation = 'logistic' a quantidade de erros foi maior
'''
Descida do Gradiente é uma ferramenta padrão para otimizar
 funções complexas iterativamente dentro de um programa de computador.
Seu objetivo é: dada alguma função arbitrária, encontrar um mínimo.'''
from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()
entradas = iris.data
saidas = iris.target

redeNeural = MLPClassifier(verbose=True,
                           max_iter=1000,
                           tol=0.00001,
                           activation='logistic',
                           learning_rate_init=0.001)
redeNeural.fit(entradas, saidas)
redeNeural.predict([[5, 7.2, 5.1,  2.2]])
