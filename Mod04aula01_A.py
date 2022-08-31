import pandas as pd

ind = ['H','M']
col = ['F', 'C']
dat = [[7,20],[4,9]]

df = pd.DataFrame(data = dat, index = ind, columns = col)

print(df)
