import pandas as pd

ind = ['I1','I2','I3','I4']
col = ['C1','C2','C3','C4']
dat = [[4,5,6,7],[9,10,15,20],[20,25,30,35],[2,4,6,8]]

df = pd.DataFrame(index=ind,columns=col,data=dat)

print(df)

print(df.sum(axis=0)) #SOMA OS VALORES  DAS COLUNAS
print(df.sum(axis=1)) #SOMA OS VALORES DAS LINHAS
print('------------------')
print(df.loc['I1','C1'])
print('------------------')
df.loc[:,'TotalLinhas'] = df.sum(axis=1) #criando uma coluna e atribuindo nela a soma das linhas

print(df)

df.loc['TotalColunas',:] = df.sum(axis=0) #criando uma coluna e atribuindo nela a soma das colunas

print(df)
