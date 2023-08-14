#construindo um gráfico de barras 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 9]

titulo = "Gráfico de barras"

eixox = "Eixo X"

eixoy = "Eixo Y"

#titulo do gráfico
#  
plt.title(titulo)

#Eixos

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y)
plt.show()

