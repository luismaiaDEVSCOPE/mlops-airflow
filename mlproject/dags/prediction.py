import mlflow
import pandas as pd
import numpy as np
# from datetime import datetime

logged_model = '../models/current/a7f818f9ad574747b3763c95d0274b4d/model'
loaded_model = mlflow.sklearn.load_model(logged_model)

test_set = pd.read_parquet('/opt/airflow/datasets/absenteeism/test_set_mock.parquet')
test_set.convert_dtypes()
test_set.reset_index(drop=True, inplace=True)

# print(test_set.head())
pred_probs = loaded_model.predict_proba(test_set)

res = np.zeros(((2, len(pred_probs))))

res[0] = np.amax(pred_probs, axis=1)
res[1] = np.argmax(pred_probs, axis=1)

probs_df = pd.DataFrame(data=np.rot90(res), columns=["Prob", "Class"])
del res
print(probs_df.head())