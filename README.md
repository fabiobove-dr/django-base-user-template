# django-base-user-template
 Basic django template for managing users
# SETUP:
set env vars in /environment/.env.dev <br>
use .env.template to understand what's needed
# RUN:
cd in project root, then:
> docker-compose -f .\dockerfiles\docker-compose.dev.yml --env-file .\environment\.env.dev up -d --build