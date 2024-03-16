# Simple ERP with Django

## Starting the project with Docker
 
### Buildind the image Docker

```shell
    docker build -t erp .
```
<br>

### Starting the container

```shell
    docker run -p 8000:8000 erp
```

<br>

---

## Starting locally

### Install the dependencies:

```shell
    pip install -r requirements.txt
```

<br>

### Run migrate:


```shell
    python manage.py migrate
```

<br>

### Create a super user:

```shell
    python manage.py createsuperuser
```
<br>

### Starting the server:

```shell
    python manage.py runserver
```

Acesse: [localhost:8000/admin](localhost:8000/admin)

<br>

---

# Preview
