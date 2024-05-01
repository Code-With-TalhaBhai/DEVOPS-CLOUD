1. `docker build -t fastapi-with-test .`


##### Simple Container -> Run uvicorn server as written in CMD(Dockerfile)
2. `docker run -it --name="fastapi-test-container" -p 8001:8000 fastapi-with-test` (/bin/bash)-> not used with fastapi


#### Overwrites `CMD` command in Dockerfile
3. `docker run -it --name="fastapi-test-container" fastapi-with-test /bin/bash -c "poetry run pytest" `



#### Deleted Container immediately after testing(process-finishes)
4. `docker run --rm --name="fastapi-test-container" fastapi-with-test /bin/bash -c "poetry run pytest" `  


