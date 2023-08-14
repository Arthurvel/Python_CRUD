#importando a função "plt"

import matplotlib.pyplot as plt

#dados do gráfico

x = [1,2, 5]
y = [2,3, 7]

#construindo o título do gráfico 

plt.title("Mine")

#contruindo os eixos

plt.xlabel("Eixo X")

plt.ylabel("Eixo Y")

#função que mostra o gráifco 
plt.plot(x,y)
plt.show()

