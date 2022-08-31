import ipywidgets as wi
from IPython.display import display, HTML
import pandas as pd

dado_hist={
    'Empresa 1':[4,9,6,5],
    'Empresa 2':[9, 6, 4, 15],
    'Empresa 3':[6, 4, 2, 25],
    'Empresa 4':[4, 2, 4, 35],
    'Empresa 5':[2, 4, 9, 45]
    }

df = pd.DataFrame(dado_hist)
#print(df)
print(df) 
#display(df)

#html = df.to_html()
#display(HTML(html))


display(HTML(df.to_html()))



wi1 = wi.Output()

with wi1:
    display.display(df)

hb = wi.HBox([wi1])

#print(html)

#cria arquivo com conteúdo html e salva no diretório corrente
##tf = open('index.html','w')
##tf.write(html)
##tf.close()

