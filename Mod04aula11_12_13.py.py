#!/usr/bin/env python
# coding: utf-8

# In[16]:


from IPython.display import display, HTML
import pandas as pd
import seaborn as sns

dado_hist={
    'Empresa 1':[4,9,6,5],
    'Empresa 2':[9, 6, 4, 15],
    'Empresa 3':[6, 4, 2, 25],
    'Empresa 4':[4, 2, 4, 35],
    'Empresa 5':[2, 4, 9, 45]
    }

df = pd.DataFrame(dado_hist)
#print(df)
display(HTML(df.to_html()))

dfa= df.head(2)
display(HTML(dfa.to_html()))
dft= df.tail(2)
display(HTML(dft.to_html()))

cm = sns.light_palette("b",as_cmap = True)

s = df.style.background_gradient(cmap = cm)
display(s)


# In[21]:


import seaborn as sns

df.loc[:4].style.background_gradient(cmap='hot')
# há vários tipos de cmap: vitidis; magma, hot etc.


# In[ ]:





# In[ ]:




