import matplotlib.pyplot as p

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x2 = [6, 7, 8, 9, 10, 11, 12, 13, 14]
y1 = [1, 3, 5, 3, 1, 3, 5, 3, 1]
y2 = [2, 4, 6, 4, 2, 4, 6, 4, 2]


p.bar(x1, y1, label='Empresa 1', color='b')
p.bar(x2, y2, label='Empresa 2', color='r')
p.legend()
p.show()
