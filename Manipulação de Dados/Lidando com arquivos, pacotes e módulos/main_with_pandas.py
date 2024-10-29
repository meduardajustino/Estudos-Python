import pandas as pd

#carregar os dados do csv para um dataframe
#df (DataFrame)
df1=pd.read_csv('abril-2024-tratado.csv')
df2=pd.read_csv('maio-2024-tratado.csv')

#juntando os dois dataframes com os dados dos 2 csvs
resultado=pd.concat([df1, df2], ignore_index=True)

#salva o resultado da junção dos dois dataframes em um csv
resultado.to_csv('abril-maio-2024_pandas.csv', index=False)
