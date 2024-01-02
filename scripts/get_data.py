import requests
import json
import pandas as pd
import os

import mlflow
from mlflow.tracking import MlflowClient
 
os.environ["MLFLOW_REGISTRY_URI"] = "/home/sflow-admin/project/mlflow/"
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("get_data")

# Необходимые справочники данных
ids = []
names = []
main_types = []
is_mega = []
heights = []
weights = []
exp = []

# Количество покемонов для запроса
num = 200

with mlflow.start_run():
    # собираем данные через API
    for id in range(num)[1:]:
        uri = f"https://pokeapi.co/api/v2/pokemon/{id}/"
        content = requests.get(uri).text
        data = json.loads(content)
        ids.append(data['id'])
        names.append(data['name'])
        main_types.append(data['types'][0]['type']['name'])
        heights.append(data['height'])
        weights.append(data['weight'])    
        exp.append(data['base_experience'])
        
        uri_2 = data['forms'][0]['url']
        content_2 = requests.get(uri_2).text
        data_2 = json.loads(content_2)
        is_mega.append(data_2['is_mega'])
    
    # Формируем датафрейм из собранных данных
    data = {'name': names,
            'main_type': main_types,
            'is_mega': is_mega,
            'height': heights,
            'weight': weights,     
            'exp': exp}
    df = pd.DataFrame(data, 
                    index = ids)
    mlflow.log_artifact(local_path="/home/sflow-admin/project/scripts/get_data.py",
                        artifact_path="get_data code")
    mlflow.end_run()

# Записываем в файл
df.to_csv('/home/sflow-admin/project/datasets/data.csv')