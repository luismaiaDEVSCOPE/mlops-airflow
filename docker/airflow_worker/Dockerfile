FROM apache/airflow:2.5.1-python3.8
USER root

RUN apt update
RUN apt install libgomp1
RUN ACCEPT_EULA=Y apt-get install -y "msodbcsql17"
USER airflow

RUN pip install --no-cache-dir lxml
RUN pip install jupyter
COPY ./requirements.txt /home/requirements.txt

RUN pip install -r /home/requirements.txt