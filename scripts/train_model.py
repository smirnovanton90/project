from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd

import mlflow
from mlflow.tracking import MlflowClient
 
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("train_model")

# Считываем из файла 
df = pd.read_csv('/home/sflow-admin/project/datasets/data_train.csv')

# Выделяем фичи и целевые значения
X_train = df.drop(['name', 'exp'], axis = 1)
Y_train = df['exp']

# Обучаем модель линейной регрессии
model = LinearRegression()

with mlflow.start_run():
    mlflow.sklearn.log_model(model,
                             artifact_path="lr",
                             registered_model_name="lr")
    mlflow.log_artifact(local_path="/home/sflow-admin/project/scripts/train_model.py",
                        artifact_path="train_model code")
    mlflow.end_run()

model.fit(X_train, Y_train)

# Сохраняем получившуюся модель в файл
with open('/home/sflow-admin/project/models/model.pickle', 'wb') as f:
    pickle.dump(model, f)