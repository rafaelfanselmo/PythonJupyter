x = 2
y = 3.0
z = x/y #promoção implicta de tipo
print(type(x))
print(type(y))
print(type(z))
print(z)
w = int(z) # conversão explicita de tipo
print(w)
print(type(w))
print(x**2) #potencia
t = (x + y - z * w**2)/3
print(t)
print("resultado = "+str(t))
