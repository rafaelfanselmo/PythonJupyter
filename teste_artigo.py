import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0, 100, size=(15, 4)), columns=list("ABCD"))
print(df)

df = df.corr().style.background_gradient(cmap="Blues")
print(df)
df

