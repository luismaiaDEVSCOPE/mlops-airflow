# Best way to add multiple dependencies to the base project
# replace image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.2.0}
# with 
# build:
#   context: .
#
FROM apache/airflow:2.2.0-python3.8
USER root
RUN pip install --no-cache-dir lxml
RUN pip install jupyter
COPY ./requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt
USER airflow