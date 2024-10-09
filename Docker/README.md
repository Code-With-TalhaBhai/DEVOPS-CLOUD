### Docker Commands

##### 1. To Build image from Dockerfile
```
docker build -f [docker-filename](optional) -t [image_name] [docker_file_path]
docker build -f Dockerfile.dev -t hello_world_img .
```


##### 2. To Create Container
```
docker run -it(optional) --name=[container_name](optional) -p[local_machine_port : container_port] [image_name] 
docker run -it --name="my-container" -p 8081:8080 my_img
```


##### 3. To List Images
```
docker images
docker image ls
```


##### 4. To List Running Containers
```
docker container ls
```


##### 5. To List All Containers(whether running or stopped)
```
docker container ls -a
```

#####  6. To Show Running Processes
```
docker ps
```

##### 7. To Show All Process(Running + Stopped)
```
docker ps -a
```

#####  8. To Show Container Logs
```
docker logs [container_name]
```

#####  9. To Get Into Running Container 
```
docker exec -it [container_name or id] /bin/bash/
```


##### 10. To Get Out Of Container Without Exiting
```
CTRL + P + Q
```


##### 11. To Get Out Of Container With Exiting
```
CTRL + C
exit
```


##### 12. To Build Image From Running Container
```
docker commit [container_name or id] [image_name]
```

##### 13. To Start Container(Already Created)
```
docker start [container_name or id]
```


### Flags of Docker Commands

1. `-t` === tag ['mostly for name']

2. `-f` === fixed ['fixed on screen to observe process']

3. `-c` === command ['Used to give CMD command or overwrite it at runtime(at the time of creating container)']

4. `-it` === interactive-terminal ['Interactive mode while creating or running container, open the process in shell']

5. `-d` === detach ['Detach mode runs process in background not opens the shell']


6. `a` === all


### Docker-Compose Commands

##### 1. Create and Start Container(services), Build Images If Necessary
```
docker compose up
docker compose up -d (In Detach-mode)
```

##### 2. Lists containers for a Compose project, with current status
```
docker compose ps
```

##### 3. List running compose projects
```
docker compose ls
```

##### 4. Start the Services(Only Start Container thate were previously created and stop using `docker-compose stop`)
```
docker compose start
```

##### 5. Only stop the Container(Services), but not remove them
```
docker compose stop
```

##### 6. Parse, resolve and render compose file in canonical format
```
docker compose config
```

##### 7. Display the running process
```
docker compose top
```

##### 8. Shows the Docker Compose version information
```
docker compose version
```

##### 9. Stop and remove containers, networks, volumes
```
docker compose down
```

##### 10.List images used by the containers created by docker compose file
```
docker compose images
```

##### 11. If you change a service's Dockerfile or the contents of its build directory(image),to rebuild it.
```
docker compose build
```


##### 12.If you want rebuild and start services both
```
docker compose up --build -d
```

## See The Difference

1. ### CMD VS ENTRYPOINT

    - #### CMD:
        - The `CMD` instruction specifies the default command and/or arguments to execute when the container starts. It can be overridden by providing a command and/or arguments when running the container.
        - If a Dockerfile has multiple `CMD` instructions, only the last one will take effect.
        - If the `CMD` instruction is not provided in the Dockerfile, the default command is `["/bin/sh", "-c"]`

    - #### ENTRYPOINT
        - The `ENTRYPOINT` instruction specifies the executable to run when the container starts, and it also allows for the default arguments to be set.
        - Unlike CMD, the `ENTRYPOINT` command and its arguments are not overridden by providing a command when running the container. Instead, the provided command and arguments are appended to the `ENTRYPOINT` command.
        - If a Dockerfile has multiple `ENTRYPOINT` instructions, only the last one will take effect.

2. ### COPY VS ADD
    - #### COPY:
        `COPY`: This instruction copies files and directories from the host machine to the Docker image. It takes two arguments: a source path (on the host) and a destination path (in the image). It is typically used for copying local files into the image.
    
    - #### ADD:
        `ADD`: This instruction is similar to `COPY`, but it has some additional features. It can copy files and directories, as well as URLs and even extract files from archives (e.g., `tar`, `gzip`, `bzip2`). However, because of these additional features, it's considered more complex and less predictable than `COPY`.
