import pandas as pd

dic = {"Favor":[15,1], "Contra":[45,36]}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

df = pd.DataFrame(dic)
print(df)

#para alterar os índex do dataframe criado
linhas = {0:"H",1:"M"}
#linhas = {"Favor":"F","Contra":"F"}

# alterando o index
df = df.rename(index=linhas)
print(df)

di = df.iloc[0,1]
print(di)

dl = df.loc["M","Contra"]
print(dl)

df.iloc[0,0] = df.iloc[0,0] + 3
print(df)
     
