# FRA
Fra is a Recommendation based framework. It was created with the idea of have an option for creating content-based recommendations easily via API.


## Architecture

![Architecture diagram](docs/architecture_1.png)

## Requirements
* pyenv (optional but recommended)
* poetry
* python 3.9+
* postgres
* redis

## Installation
* create a virtualenv
    >pyenv virtualenv 3.9.15 fra
    >pyenv activate fra
* create a database and update the config.py file with the name and host
    >psql; create database fra; \q
* install the requirements
    >poetry install
* migrate the models 
    > flask --app server/app db upgrade


## Running the app

* activate the environment
    > pyenv activate fra
* run the app
    > flask --app server/app run

-- For async jobs that process recommendations

    > celery -A motor.tasks worker  --loglevel=info  


OpenAPI docs will be online on YOURDOMAIN/api/swagger/ui

Follow this order to be able to get recommendations:
1. create an organization
2. add users to the organization
3. add the files with the data (some examples on example_data folder)
4. add file mapping
5. add user ratings
6. get recommendations


## TODO

* Build and publish on GCP
* Add more data set to the examples
