# Exam Scheduler API

## Instalation

- Install pipenv to manage the virual environment
```sh
pip install --user pipenv
```

- Spawn a new pipenv environment
```sh
pipenv shell
```

- Install the project dependencies
```sh
pip install -r requirements.txt
```

- Start the server
```sh
python manage.py runserver
```

## Usage


### Base URL
http://localhost:8000/api/v1/sheduler

### Users' Endpoints
| Name | Method  | Path | Query |
|:------|:---------|:------|:-------|
|Get all students|GET|/student/|page, limit|
|Get student by ID|GET|/student/:id|-|
|Add student|POST|/student/|-|
|Edit student details|PUT|/student/:id|-|
|Delete student record|DELETE|/student/:id/|-|

### Courses' Endpoints

### Examinations' Endpoints