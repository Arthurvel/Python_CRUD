import matplotlib.pyplot as plt 

#abrindo o arquivo 
dados = open("populacao_brasileira").readlines()

#criando vetores vazios parar serem preenchidos pelos valores do arquivo 
x = []
y = []

for i in range(len(dados)):
    if i !=0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x,y, color = "gray")
plt.plot(x,y, color = "r", linestyle = "--")

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
#plt.show()
plt.savefig("populacao_brasileira.png", dpi=300)
