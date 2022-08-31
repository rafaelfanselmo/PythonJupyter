import pandas as pd

dic = {"Favor":[15,1], "Contra":[45,36]}
print(dic)
print()
print(dic.keys())
print()
print(dic.values())
print()
print(dic.items())
print()
#print(dic.index())
print()
df = pd.DataFrame(dic)
print(df)
print()
#para alterar os índex do dataframe criado
linhas = {0:"H",1:"M"}
#linhas = {"Favor":"F","Contra":"F"}

# alterando o index
df = df.rename(index=linhas)
print(df)
print()

di = df.iloc[0,1]
print(di)
print()

dl = df.loc["M","Contra"]
print(dl)
print()

df.iloc[0,0] = df.iloc[0,0] + 3
print(df)
print()     
