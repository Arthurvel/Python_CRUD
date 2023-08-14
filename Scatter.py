#gráfico de pontos

import matplotlib.pyplot as plt 

x = [1, 3, 5, 7, 9]

y = [2, 3, 7, 1, 0]

titulo = "Scatterplot: gráfico de dispersão"

eixox = "eixo x"

eixoy = "eixo y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#pontos do gráfico
plt.scatter(x,y, label = "Meus pontos", color = "r", marker = ".", s=90)

#lugando os pontos do gráfico 
plt.plot(x,y, color = "k", linestyle = "-.")
plt.legend()
plt.show()

#salvando o gráfico 

#dpi é o tamanho 

plt.savefig("Gráfico Pontilhado.pdf",dpi = 300)