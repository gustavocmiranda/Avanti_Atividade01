import pandas as pd

df = pd.read_csv('nomedoarquivo.csv')

df = df.dropna()    # dropar todas as tuplas que possuam algum valor Na

