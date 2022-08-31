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

df = df.rename(index=linhas)
print(df)
