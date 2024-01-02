import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Считываем из файла 
df = pd.read_csv('/home/sflow-admin/project/datasets/data.csv')

# Делаем OHE для колонки 'main_type'
one_hot = pd.get_dummies(df['main_type'])
df = df.drop('main_type',axis = 1)
df = df.join(one_hot)

# Записываем в файл
df.to_csv('/home/sflow-admin/project/datasets/data_processed.csv')