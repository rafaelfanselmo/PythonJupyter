cores = {1:'blue',2:'red',3:'green'}
dados = {'x':[1,2,3,4], 'y':[4,5,6,7],'z':[8,9,6,7]}
print(cores[1])
print(dados['x'])
print(cores.keys())
print(cores.values())
print(dados.keys())
print(dados.values())
print(cores.items())
print(dados.items())

cores[4]='black'
print(cores.items())

dados['y'][2]=8
print(dados.items())
