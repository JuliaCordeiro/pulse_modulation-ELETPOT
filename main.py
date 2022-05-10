import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import math as mt

#1 Fazer uma função que constrói a senoide, passando por parâmetro a frequência.
#2 Fazer uma função que realiza a série de fourier para gerar a onda triangular (N=10)
#3 Comparar o valor das duas para construir a tabela de saída da onda modulada
#4 Gerar os gráficos

#Gerando os pontos da senoide
def sin_wave(x, freq, y_sin, i):
    omega = 2.0 * np.pi * freq
    y_sin[i] = np.sin(omega * x)


def tr_fun(x, y_tr, i):
    if(i == 0):
        y_tr[i] = x*4000.0
    elif(y_tr[i-1] >= 1.0):
        y_tr[i] = -4000.0*x
    else:
        y_tr[i] = x*4000.0


y_seno = np.zeros(10000)
y_tr = np.zeros(10000)
#Preenchendo o eixo X
eixo_x = np.linspace(0.0, 1.0, 10000)


#Recebendo frequência via input
freq_str = input("Valor da Frequencia em Hz: ")
freq = float(freq_str)

#Preenchendo o eixo Y do seno
for i in range(10000):
    sin_wave(eixo_x[i], freq, y_seno, i)


plt.plot(eixo_x, y_seno)
plt.show()
