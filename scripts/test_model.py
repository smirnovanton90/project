from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle
import pandas as pd
 
# Считываем из файла тестовые данные
df = pd.read_csv('/home/sflow-admin/project/datasets/data_test.csv', header=None)

# Выделяем фичи и целевые значения в тестовых данных
X_test = df.drop(['name', 'exp'], axis = 1)
Y_test = df['exp']

# Считываем ранее обученную модель из файла
model = LinearRegression()
with open('/home/sflow-admin/project/models/model.pickle', 'rb') as f:
    model = pickle.load(f)

# Рассчитываем значение целевой метрики RMSE
rmse = mean_squared_error(Y_test, model.predict(X_test), squared = False)
print("RMSE = ", rmse)