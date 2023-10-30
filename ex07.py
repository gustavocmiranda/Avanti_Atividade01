import pandas as pd

df = pd.read_csv('nomedoarquivo.csv')

print(df['Column'].loc[df['Column'] == 'Condition'])    # Escolher condicao e qual comparacao fazer