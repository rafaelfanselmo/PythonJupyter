import pandas as pd

ind = ['H','M']
col = ['F','C']
dat = [[7,20],[4,9]]

df = pd.DataFrame(index=ind,columns=col,data=dat)

print(df)
print()
print("df.loc[:,'C'] ")
print(df.loc[:,'C'])
print()
print("df.iloc[1,:] ")
print(df.iloc[1,:])
print()
print("df.loc[:,['F','C']] ")
print(df.loc[:,['F','C']])

#print(df.loc['H':'M','F':'C']) exemplos de pegar range de colunas
#o mesmo pode ser feito com iloc usando valores de dos indices


