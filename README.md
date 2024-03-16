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

Acesse: [localhost:8000/admin](localhost:8000/admin)

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

#### Home adm:

<img src="https://raw.githubusercontent.com/fabioacarvalho/erp_django1/master/static/assets/img/home_erp.png?token=GHSAT0AAAAAACOV56O552A4YLVC6R3LCEYMZPVAT4Q">

<br>

#### Changelist:

<img src="https://raw.githubusercontent.com/fabioacarvalho/erp_django1/master/static/assets/img/changelist.png?token=GHSAT0AAAAAACOV56O5A4DXKT4FG55FIZUIZPVATGQ">

<br>

#### Changeform:

<img src="https://raw.githubusercontent.com/fabioacarvalho/erp_django1/master/static/assets/img/changeform.png?token=GHSAT0AAAAAACOV56O4GFZPSURHJS4PWXW2ZPVAUMA">

<br>

#### Recent actions:

<img src="https://raw.githubusercontent.com/fabioacarvalho/erp_django1/master/static/assets/img/actions.png?token=GHSAT0AAAAAACOV56O57UYO3U37ROF4DDEQZPVAVFA">

<br>

#### Recent actions:

<img src="https://raw.githubusercontent.com/fabioacarvalho/erp_django1/master/static/assets/img/actions.png?token=GHSAT0AAAAAACOV56O57UYO3U37ROF4DDEQZPVAVFA">

<br>