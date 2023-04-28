import mlflow

logged_model = '/opt/airflow/datasets/models/current/a7f818f9ad574747b3763c95d0274b4d/artifacts/FeatureUnionpipeline/'
import os
assert os.path.exists(logged_model)

feat_model = mlflow.sklearn.load_model(logged_model)

# mlflow.set_tracking_uri('http://mlflow_server:5000') # mlflow # mlflow_server
os.environ.get('MLFLOW_TRACKING_URI')
mlflow.set_tracking_uri('/data/mlflow')

exp_name = "MODELS" # f"{args.dataset}_{args.dataset_folder}_{args.engine}"

try:
    exp_id = mlflow.create_experiment(exp_name)
    experiment = mlflow.get_experiment(exp_id)
except:
    experiment = mlflow.get_experiment_by_name(exp_name)
    
mlflow.set_experiment(exp_name)

mlflow.start_run()
mlflow.sklearn.log_model(feat_model, 'FeatureUnionpipeline')


logged_model = '/opt/airflow/datasets/models/current/a7f818f9ad574747b3763c95d0274b4d/artifacts/model/'
import os
assert os.path.exists(logged_model)
model = mlflow.sklearn.load_model(logged_model)

mlflow.sklearn.log_model(model, 'model')

mlflow.end_run()