from tokenize import String
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

#função que gera a onda triangular
def tr_wave(x, y_tr, i, freq):
    omega = 2.0 * np.pi * freq
    y_tr[i] = (2.75 / np.pi) * ((np.sin(omega * x)) - ((1 / 9) * np.sin(3 * omega * x)) + ((1 / 25) * np.sin(5 * omega * x))) 

#função que compara as ondas
#A lógica de comparação é a seguinte:
#   No semi-ciclo positivo da senóide: seno > triangular -> saida = 1
#                                      seno < triangular -> saida = -1
#   No semi-siclo negativo da senóide: seno > triangular -> saida = -1
#                                      seno < triangular -> saida = 1  
def compare_waves(y_sin, y_tr, i, y_mod):
    if(y_sin[i] >= 0.0):
        if(y_sin[i] > y_tr[i]):
            y_mod[i] = 1
        else:
            y_mod[i] = -1
    else:
        if(y_sin[i] < y_tr[i]):
            y_mod[i] = 1
        else:
            y_mod[i] = -1

#inicialização de variáveis
y_seno = np.zeros(10000)
y_tr = np.zeros(10000)
y_mod = np.zeros(10000)

#Preenchendo o eixo X
eixo_x = np.linspace(0.0, 1.0, 10000)

#Vetor de frequencias da onda triangular
freqs_tr = [10.0, 50.0, 100.0, 200.0]


#Recebendo frequência da senóide via input
freq_str = input("Valor da Frequencia em Hz: ")
freq = float(freq_str)

for j in range(4):
    #Preenchendo o eixo Y 
    for i in range(10000):
        sin_wave(eixo_x[i], freq, y_seno, i)
        tr_wave(eixo_x[i], y_tr, i, freqs_tr[j])

    for i in range(10000):
        compare_waves(y_seno, y_tr, i, y_mod)

    fig, axs = plt.subplots(2, figsize=(20,8))
    axs[0].set(
        ylabel = "Amplitude",
        title = f"Senóide x Onda Triangular f = {freqs_tr[j]} Hz"
    )
    axs[0].plot(eixo_x, y_seno)
    axs[0].plot(eixo_x, y_tr)
    axs[0].legend(["Senóide", "Onda Triangular"])

    axs[1].set(
        ylabel = "Amplitude",
        xlabel = "Tempo (s)",
        title = "Onda Modulada"
    )
    axs[1].plot(eixo_x, y_mod, 'tab:green')
    axs[1].legend(["Saída Modulada"])
    plt.savefig(f'plot-f-{freqs_tr[j]}Hz.png')
    plt.show()