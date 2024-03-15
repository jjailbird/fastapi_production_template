# Docker compose

## Tips

```yaml
# docker-compose.yml
services:
  web:
    image: example/web
    profiles: ["front-end"]
  db:
    image: example/db
    profiles: ["back-end"]
```


```shell

# Run the only "web" service in docker-compose.yml
docker-compose up -d web

# Run profiles "front-end" group in docker-compose.yml 
docker-compose up -d --profile front-end up

```