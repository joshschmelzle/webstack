# webstack

## backend requirements

apt install prep:

```
sudo apt install gcc libpq-dev python3-dev python3-pip python3-venv python3-wheel pkg-config dbus build-essential git libdbus-glib-1-dev -y
```

### linting and formatting

- autoflake
- black
- flake8
- isort
- mypy

### fastapi/uvicorn

- uvicorn
- python-dotenv
- fastapi

### utils

- dbus-python
- uvicorn 
- python-dotenv
- fastapi
- psutil

### ookla speedtest reqs:

```
sudo apt install gnupg1 apt-transport-https dirmngr
export INSTALL_KEY=379CE192D401AB61
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $INSTALL_KEY
echo "deb https://ookla.bintray.com/debian generic main" | sudo tee  /etc/apt/sources.list.d/speedtest.list
sudo apt update
# Other non-official binaries will conflict with Speedtest CLI
# Example how to remove using apt
# sudo apt remove speedtest-cli
sudo apt install speedtest
```

### lldpd reqs:

- install:

```
sudo apt install lldpd
```

- wlanpi user needs to be able to run `sudo lldpcli show neighbors -f json` without password, one option is to add the following line to the end of /etc/sudoers (sudo visudo):

```
wlanpi ALL=NOPASSWD:/usr/sbin/lldpcli
```

## frontend requirements

- vue.js?
- react.js? 

## backend local development

- Create virtualenv and install dependencies.

```
cd {repo}/webstack/backend
python3 -m venv env && source ./env/bin/activate
python -m pip install -U pip wheel setuptools
pip install -r requirements.txt
```

- Note that in the future this may be installed via `pipx` or `dh-virtualenv`.

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
