## Airflow in Docker
Before you begin

Follow these steps to install the necessary tools.

Install Docker Community Edition (CE) on your workstation. Depending on the OS, you may need to configure your Docker instance to use 4.00 GB of memory for all containers to run properly. Please refer to the Resources section if using Docker for Windows or Docker for Mac for more information.

Install Docker Compose v1.29.1 and newer on your workstation.

Older versions of docker-compose do not support all the features required by docker-compose.yaml file, so double check that your version meets the minimum version requirements.

docker-compose.yaml
To deploy Airflow on Docker Compose, you should fetch docker-compose.yaml.

docker-compose.yaml
To deploy Airflow on Docker Compose, you should fetch docker-compose.yaml.

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.0/docker-compose.yaml'
This file contains several service definitions:

airflow-scheduler - The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.

airflow-webserver - The webserver is available at http://localhost:8080.

airflow-worker - The worker that executes the tasks given by the scheduler.

airflow-init - The initialization service.

flower - The flower app for monitoring the environment. It is available at http://localhost:5555.

postgres - The database.

redis - The redis - broker that forwards messages from scheduler to worker.

All these services allow you to run Airflow with CeleryExecutor. For more information, see Architecture Overview.

Some directories in the container are mounted, which means that their contents are synchronized between your computer and the container.

./dags - you can put your DAG files here.

./logs - contains logs from task execution and scheduler.

./plugins - you can put your custom plugins here.

This file uses the latest Airflow image (apache/airflow). If you need to install a new Python library or system library, you can build your image.

Using custom images
When you want to run Airflow locally, you might want to use an extended image, containing some additional dependencies - for example you might add new python packages, or upgrade airflow providers to a later version. This can be done very easily by placing a custom Dockerfile alongside your docker-compose.yaml. Then you can use docker-compose build command to build your image (you need to do it only once). You can also add the --build flag to your docker-compose commands to rebuild the images on-the-fly when you run other docker-compose commands.

Examples of how you can extend the image with custom providers, python packages, apt packages and more can be found in Building the image.

Initializing Environment
Before starting Airflow for the first time, You need to prepare your environment, i.e. create the necessary files, directories and initialize the database.

Setting the right Airflow user
On Linux, the quick-start needs to know your host user id and needs to have group id set to 0. Otherwise the files created in dags, logs and plugins will be created with root user. You have to make sure to configure them for the docker-compose:

mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
See Docker Compose environment variables

For other operating systems, you will get warning that AIRFLOW_UID is not set, but you can ignore it. You can also manually create the .env file in the same folder your docker-compose.yaml is placed with this content to get rid of the warning:

AIRFLOW_UID=50000
Initialize the database
On all operating systems, you need to run database migrations and create the first user account. To do it, run.

docker-compose up airflow-init
After initialization is complete, you should see a message like below.

airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.2.0
start_airflow-init_1 exited with code 0
The account created has the login airflow and the password airflow.

Cleaning-up the environment
The docker-compose we prepare is a "Quick-start" one. It is not intended to be used in production and it has a number of caveats - one of them being that the best way to recover from any problem is to clean it up and restart from the scratch.

The best way to do it is to:

Run docker-compose down --volumes --remove-orphans command in the directory you downloaded the docker-compose.yaml file

remove the whole directory where you downloaded the docker-compose.yaml file rm -rf '<DIRECTORY>'

re-download the docker-compose.yaml file

re-start following the instructions from the very beginning in this guide

Running Airflow
Now you can start all services:

    docker-compose up

In the second terminal you can check the condition of the containers and make sure that no containers are in unhealthy condition:

    $ docker ps
    CONTAINER ID   IMAGE                  COMMAND                      CREATED          STATUS                        PORTS                              NAMES
    247ebe6cf87a   apache/airflow:2.2.0   "/usr/bin/dumb-init …"   3     minutes ago    Up 3 minutes (healthy)    8080/    tcp                           compose_airflow-worker_1
    ed9b09fc84b1   apache/airflow:2.2.0   "/usr/bin/dumb-init …"   3     minutes ago    Up 3 minutes (healthy)    8080/    tcp                           compose_airflow-scheduler_1
    65ac1da2c219   apache/airflow:2.2.0   "/usr/bin/dumb-init …"   3     minutes ago    Up 3 minutes (healthy)    0.0.0.0:5555->5555/tcp,     8080/tcp   compose_flower_1
    7cb1fb603a98   apache/airflow:2.2.0   "/usr/bin/dumb-init …"   3     minutes ago    Up 3 minutes (healthy)    0.0.0.0:8080->8080/    tcp             compose_airflow-webserver_1
    74f3bbe506eb   postgres:13            "docker-entrypoint.s…"   18     minutes ago   Up 17 minutes (healthy)   5432/    tcp                           compose_postgres_1
    0bd6576d23cb   redis:latest           "docker-entrypoint.s…"   10     hours ago     Up 17 minutes (healthy)   0.0.0.0:6379->6379/    tcp             compose_redis_1

Accessing the environment
After starting Airflow, you can interact with it in 3 ways;

by running CLI commands.

via a browser using the web interface.

using the REST API.

Running the CLI commands
You can also run CLI commands, but you have to do it in one of the defined airflow-* services. For example, to run airflow info, run the following command:

docker-compose run airflow-worker airflow info
If you have Linux or Mac OS, you can make your work easier and download a optional wrapper scripts that will allow you to run commands with a simpler command.

    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.0/airflow.sh'
    chmod +x airflow.sh

Now you can run commands easier.

    ./airflow.sh info

You can also use bash as parameter to enter interactive bash shell in the container or python to enter python container.

    ./airflow.sh bash
    ./airflow.sh python

Accessing the web interface
Once the cluster has started up, you can log in to the web interface and try to run some tasks.

The webserver is available at: http://localhost:8080. The default account has the login airflow and the password airflow.

Sending requests to the REST API
Basic username password authentication is currently supported for the REST API, which means you can use common tools to send requests to the API.

The webserver is available at: http://localhost:8080. The default account has the login airflow and the password airflow.

Here is a sample curl command, which sends a request to retrieve a pool list:

    ENDPOINT_URL="http://localhost:8080/"
    curl -X GET  \
        --user "airflow:airflow" \
        "${ENDPOINT_URL}/api/v1/pools"´

## Cleaning up
To stop and delete containers, delete volumes with database data and download images, run:


    docker-compose down --volumes --rmi all