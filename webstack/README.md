# webstack

## backend requirements

apt installs:

first:

```
sudo apt-get install gcc libpq-dev -y
sudo apt-get install python-dev  python-pip -y
sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
pip3 install wheel
```

then:

```
sudo apt install pkg-config dbus build-essential git libdbus-glib-1-dev speedtest-cli lldpd
```

### linting and formatting

- autoflake, black, flake8, isort, mypy

### fastapi/uvicorn

- uvicorn, python-dotenv, fastapi

### utils

- dbus-python uvicorn python-dotenv fastapi psutil

### speedtest reqs:

https://www.speedtest.net/apps/cli

- sudo apt-get install speedtest-cli

### lldpd reqs:

- sudo apt-get install lldpd

- wlanpi user needs to be able to run `sudo lldpcli show neighbors -f json` without password, one option is to add the following line to the end of /etc/sudoers (sudo visudo):

```
wlanpi ALL=NOPASSWD:/usr/sbin/lldpcli
```

## frontend requirements

- vue.js?
- react.js? 

## backend local development

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
```

`run.sh` runs something like the following for development only:

```
uvicorn app.main:app --reload --env-file ../../.env 
```

- Local development recommendations may change.

- Now you can open your browser and interact with these URLs:

Frontend, with routes handled based on the path: http://localhost

Backend, OpenAPI based JSON based web API: http://localhost/api/

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost/docs

Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://localhost/redoc

## backend local development, additional details

before committing changes:

- for consistent styling please lint using lint.sh:
- `(venv) [~/webstack/webstack/backend/app]: ./scripts/lint.sh`

- to apply automatic formatting changes use format.sh:
- `(venv) [~/webstack/webstack/backend/app]: ./scripts/format.sh`

### general workflow

TODO

### backend tests

TODO

#### test coverage

use `tox` to automate tests and coverage stats

## frontend development

TODO

## deployment

### backend

nginx for proxy pass and static files

gunicorn for managing uvicorn processes

uvicorn as the ASGI server 

### frontend

TODO
