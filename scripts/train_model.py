from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
 
# Считываем из файла 
df = pd.read_csv('/home/sflow-admin/project/datasets/data_train.csv')

# Выделяем фичи и целевые значения
X_train = df.drop(['name', 'exp'], axis = 1)
Y_train = df['exp']

# Обучаем модель линейной регрессии
model = LinearRegression()
model.fit(X_train, Y_train)

# Сохраняем получившуюся модель в файл
with open('/home/sflow-admin/project/models/model.pickle', 'wb') as f:
    pickle.dump(model, f)