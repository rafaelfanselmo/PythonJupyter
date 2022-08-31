import matplotlib.pyplot as p

x  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [1, 3, 5, 3, 1, 3, 5, 3, 1]
y2 = [2, 4, 6, 4, 2, 4, 6, 4, 2]

p.plot(x, y1, 'b--')
p.bar(x, y2, color='gray')
p.show()
