#bloxplot, visualização que mostra o quão dispersos estão os dados

#valores muito dispersos são representados como circulos, ou seja outliners

import matplotlib.pyplot as plt 

#para gerar valores aleatorios 
import random

vetor = []

for i in range(10):

    num_ale = random.randint(0,6)
    vetor.append(num_ale)


plt.boxplot(vetor)
plt.show()
