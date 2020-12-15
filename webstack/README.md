# webstack

## backend requirements

### linting

- python3 -m pip install autoflake, black, flake8, isort, mypy

### dbus

- dbus: make sure `dbus-python` installed. requires `apt install libdbus-glib-1-dev`
- requires: `sudo apt-get install gcc python3-dev`

### fastapi/uvicorn

- uvicorn, python-dotenv, fastapi

### utils

- psutil

install reqs:

- python3 -m pip install dbus-python uvicorn python-dotenv fastapi psutil

### speedtest reqs:

https://www.speedtest.net/apps/cli

- sudo apt-get install speedtest-cli

### lldpd reqs:

- sudo apt-get install lldpd
- wlanpi user needs to be able to run lldpcli without password, one option is to add the following line to the end of /etc/sudoers (sudo visudo):

```
wlanpi ALL=NOPASSWD:/usr/sbin/lldpcli
```

## frontend requirements

- vue.js?
- react.js? 

## backend local development

- Install dependencies:

```
apt install pkg-config dbus build-essential libdbus-glib-1-dev speedtest-cli lldpd gcc python3-dev
```

- Create venv and install dependencies (subject to change).

```
cd {repo}/webstack/backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

- Future this may be installed via pipx (subject to change).

- Start the webstack with uvicorn and `--reload` to reload when code changes are saved.

```
cd {repo}/webstack/backend/app
./scripts/run.sh
uvicorn app.main:app --reload --env-file ../../.env 
```

- Local development recommendations may change.

- Now you can open your browser and interact with these URLs:

Frontend, with routes handled based on the path: http://localhost

Backend, OpenAPI based JSON based web API: http://localhost/api/

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost/docs

Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://localhost/redoc

## backend local development, additional details

before commiting changes:

- for consistent styling please lint using lint.sh:
- `(venv) [~/webstack/webstack/backend/app]: ./scripts/lint.sh`

- to apply automatic formatting changes use format.sh:
- `(venv) [~/webstack/webstack/backend/app]: ./scripts/format.sh`

### general workflow

TODO

### backend tests

TODO

#### test coverage

TODO

## frontend development

TODO

## deployment

### backend

TODO

### frontend

TODO
