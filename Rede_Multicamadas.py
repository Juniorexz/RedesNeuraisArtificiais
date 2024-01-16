# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:04:09 2023

@author: JUNIOR
"""

#sigmoid Não retorna valores negativos
#Inicializa os pesos como valores aleatórios
#Baseado nos dados(aprendizagem supervisionada) 
#realiza os cálculos com os pesos e calcula o erro.O Weka ajuda 
#Calcula as mudanças nos pesos e os atualiza(backpropagation)
#O algoritmo termina quando o erro é pequeno
#Gradiente(gradient descent),Derivada,Cálculo do delta,Backpropagation
#Learning rate(taxa de aprendizagem), Momentum(momento)
#Cálculo do Gradiente = 
#Cálculo da Derivada
#Cálculo do DeltaSaída = Erro * DerivadasSigmoide
#Cálculo do Delta camada oculta = DerivadaSigmoide * peso * DeltaSaída




import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

#a = sigmoid(0.5)    
#b = sigmoidDerivada(a)
    
entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])

saídas = np.array([[0],[1],[1],[0]])

#pesos0 = np.array([[-0.424, -0.740, -0.961],
#                  [0.358, -0.577, -0.469]])

#pesos1 = np.array([[-0.017], [-0.893], [0.148]])

pesos0 = 2*np.random.random((2,3)) -1
pesos1 = 2*np.random.random((3,1)) -1

#epocas vai ser a quantidade de vezes que o laço vai repetir,quanto mais próximo do 0 melhor
epocas = 1000000
#taxaAprendizagem = 0.3
taxaAprendizagem = 0.5
momento = 1

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)
    
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    
    erroCamadaSaida = saídas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Erro: "  + str(mediaAbsoluta))
     
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    #Com isso consigo multiplicar linha por coluna
    pesos1Transposta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T
    pesosNovos1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovos1 * taxaAprendizagem)
    
    camadaEntradaTransposta = camadaEntrada.T
    pesosNovos0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovos0 * taxaAprendizagem)
