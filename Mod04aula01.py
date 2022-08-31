import pandas as pd
from IPython.display import display, HTML
import seaborn as sns

df  = pd.DataFrame(data=[[7,20],[4,9]], index=[0,1], columns=['F','C'])
df2 = pd.DataFrame({'Favor': [15, 4], 'Contra': [45, 36]})
df2 = df2.rename(index={0: 2, 1: 3},columns={'Favor':'F','Contra':'C'})
print(df)
print(df.loc[0,'C'])
print(df2)
print(df2.iloc[0,0])
df = pd.concat([df, df2])
display(HTML(df.to_html()))
print(df[df > 4])

media     = df.loc[:,'F'].mean()
variancia = df.loc[:,'C'].var(ddof=0)
print(media)
print(variancia)

# Teste um dos comandos de cada vez:
df.loc[:4].style.background_gradient(cmap='viridis')
# df.style.bar(subset=['F'], align='mid', color=['#d65f5f', '#5fba7d'])
# boxplot = df.boxplot()
