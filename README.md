## Todo List API

Welcome! This is the repository of Todo List API source code.

### Features
- You can consult create, update, list, get and delete Todo List.

### Requirements

- Python 3
- Django 3

### Development setup

To setup this project for local development, you have to download the repository and download the docker containers.

### Poetry
You can use Poetry to run the project.
More info about Poetry: <https://python-poetry.org/docs/>

```
python3 -m venv venv
source venv/bin/activate
poetry install
```

or

```
docker-compose up
```

### Fast setup
1. Clone this repository in your machine.
   ```
   git clone https://github.com/marlonleite/todo.git
   ```
2. Navigate to the project root folder.
3. Download and install Docker.
   <https://www.docker.com/products/docker-desktop>
4. Go to the repository folder in your terminal and run:

```
docker volume create --name=todo_database
```
and run:

```
docker-compose up
```
stop docker:
```
docker-compose down
```
5. Once the command is finished, run the following command to get the containers' ids:
``` 
docker container ls
```
OBS: You can drop and recreate `database` if build fails.
Run that cmds:
```
docker-compose run --rm web bash
```
```
psql -h db -U postgres postgres -c "DROP DATABASE postgres"
```
```
psql -h db -U postgres postgres -c "CREATE DATABASE postgres"
```
Once the new database is created, run:
```
make migrate
```
```
make create_admin
```
6. Exit the container and make sure you are in the repository folder in the terminal.
7. Kill container and rerun docker-compose again:
```
docker-compose down
```
```
docker-compose up
```
8. Good, go to Credit Recovery API Swagger Dashboard API url:
```
http://0.0.0.0:8000/
```

### Running the tests

Access the `bash docker web container`:
```
docker-compose run --rm web bash
```

Run the follow command:
```
pytest
```
or
```
pytest path/app/test
```

### Project Videos
To watch the videos project access the follow url:

1 - Documentation

https://mega.nz/file/bREE2TZK#RMSEPH3hcGQ6AmRWynAi4heFXT1GcLR01iED5b3EfJQ

2 - Swagger

https://mega.nz/file/LMNUWT5I#ccs_GJVNFLXSChdiWhLp5XoUSeH7MQ8N7PzxSMaWSMs

3 - Insominia

https://mega.nz/file/2NMwXLqD#QQT1yL1t9w5zmTcIxTpKYXazp93x8kYgPQzjG9YMa6s

4 - Tests

https://mega.nz/file/uVEUyDga#I77R8_2tKgEEyOA-WB8Eo7z0Zi93dx4C1GdI1s8lhWI


### Authorization:
`user: admin`
`pass: 123456`

### Author
Marlon Leite - <https://github.com/marlonleite/>