# Exam Scheduler API

## Instalation

> [!NOTE]
>
> This project was bootstrapped using `Python 3.10`

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


### Authentication Endpoints
| Name | Method  | Path | Query |
|:------|:---------|:------|:-------|
| Login | POST | /login |-|
| Register | POST | /create_user |-|


### Students' Endpoints
| Name | Method  | Path | Query |
|:------|:---------|:------|:-------|
|Get all students|GET|/students/|page, limit|
|Get student by ID|GET|/students/:id|-|
|Edit student details|PUT|/students/update:id|-|
|Delete student record|DELETE|/students/delete/:id/|-|

### Supervisor' Endpoints
| Name | Method  | Path | Query |
|:------|:---------|:------|:-------|
|Get all supervisors|GET|/supervisors/|page, limit|
|Get supervisor by ID|GET|/supervisors/:id|-|
|Edit supervisor details|PUT|/supervisors/update:id|-|
|Delete supervisor record|DELETE|/supervisors/delete/:id/|-|

### Exam Officer' Endpoints
| Name | Method  | Path | Query |
|:------|:---------|:------|:-------|
|Get all exam officers|GET|/exam-officers/|page, limit|
|Get exam officer by ID|GET|/exam-officers/:id|-|
|Edit exam officer details|PUT|/exam-officers/update:id|-|
|Delete exam officer record|DELETE|/exam-officers/delete/:id/|-|

### Courses' Endpoints
| Name | Method  | Path | Query |
|:------|:---------|:------|:-------|
|Get all courses|GET|/courses/|page, limit|
|Get course by ID|GET|/courses/:id|-|
|Add course|POST|/courses/create|-|
|Edit course details|PUT|/courses/update:id|-|
|Delete course record|DELETE|/courses/delete/:id/|-|

### Exam Schedules' Endpoints
| Name | Method  | Path | Query |
|:------|:---------|:------|:-------|
|Get all exam schedules|GET|/exam-schedules/|page, limit|
|Get exam schedule by ID|GET|/exam-schedules/:id|-|
|Add exam schedule|POST|/exam-schedules/create|-|
|Edit exam schedule details|PUT|/exam-schedules/update:id|-|
|Delete exam schedule record|DELETE|/exam-schedules/delete/:id/|-|
