x = [20, 30, 10, -50]
print(x)

y = x # copiou só a referencia
y[0] = 3
print(y)
print(x)

z = x.copy()
z[0] = 25
print(z)
print(x)
