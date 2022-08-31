x = [-20, -10, 40, 30]
print("imprime numeros de elementos de uma lista: "+str(len(x)))

x.append(50)
print("imprime append x.append(50): "+str(x))

x.remove(-10)
print("imprime remove x.remove(-10): "+str(x))

print(x)
x.pop(2)
print("imprime remove posição com x.pop(2): "+str(x))


