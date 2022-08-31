import matplotlib.pyplot as p

x = [1,2,3,4,5]
y1 = [2,4,7,5,8]
y2 = [3,6,9,4,5]

p.plot(x,y1,color='blue', label='Produção')
p.plot(x,y2,color='red', label='Demanda')
p.legend()
p.grid()
p.show()

