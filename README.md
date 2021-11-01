### Base app

## App description.

### Run stack local.

- $ docker-compose -f local.yml build
- $ docker-compose -f local.yml up

### Check services

- $ docker-compose -f local.yml ps

### Kill services

- $ docker-compose -f local.yml down

### Pro tip

- $ export COMPOSE_FILE=local.yml
- $ docler-compose buid
- $ docler-compose up
- $ docler-compose ps
- $ docler-compose down

### Administrative commands

- $ docker-compose run --rm django COMMAND

- $ docker-compose run --rm django python manage.py \ createsuperuser

### Run the selected service

- $ docker-compose run --rm --service-ports SERVICE
