# Backend Licencer

## Sposób budowy i uruchomienia za pomocą docker

```sh
docker build -t licencer_be .
```

```sh
docker run --rm -p 8080:8080 --env-file ENV_FILE licencer_be 
```
