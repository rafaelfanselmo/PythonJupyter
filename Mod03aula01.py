import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [1,4,9,16,25,36]

plt.plot(x,y,color='blue')
plt.scatter(x,y,color='blue')
plt.title('Dados de Demanda', color='red')
plt.xlabel('Dia', color='green')
plt.ylabel('#Produtos')
plt.grid(color='orange')
plt.legend(['Estimativa','Dados'])
plt.show()
