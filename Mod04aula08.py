import pandas as pd

dados_hist = {'Empresa 1':[4,9,6], 'Empresa 2':[9,6,4]}
print(dados_hist)

dfh = pd.DataFrame(dados_hist)
print(dfh)

dado_dia = pd.Series([5,15],index=['Empresa 1','Empresa 2'])
print(dado_dia)

nova_linha = pd.DataFrame([dado_dia], index=[3])
print(nova_linha)

dfh = pd.concat([dfh,nova_linha])
print(dfh)

dfh = dfh.append(dfh) #fusão de tabelas porém repete os índices
print(dfh)
print()
print(dfh.shape) #tamanho dos dados na tabela
print()
dfh.drop_duplicates(inplace = True)
print(dfh)
print()
print(dfh[dfh>4])#imprime a tabela somente com os valores maiores que 4
print()
print(dfh[dfh['Empresa 2']>5])#imprime a tabela com valores maiores que 5 suprimindo a linha

print()
print(dfh[dfh['Empresa 1']<5])

dfh2=dfh.copy()#é preciso usar a função copy, se usar o sinal de igual será cpiado a referencia.
dfh2[dfh2 <= 4]=0.0
print(dfh2)









print()
print()
print('tste função Series insere uma colunas mas tbm uma tabela se passado uma lista de litas')
a = [1, 2,3]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])

b = [1, 2,3]

myvar2 = pd.Series(b,index=['x','y','z'])

print(myvar2)
print(myvar2['y'])





