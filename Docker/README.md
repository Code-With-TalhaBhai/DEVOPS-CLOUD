### Docker Commands

##### To Build image from Dockerfile
1. docker build -f [docker-filename](optional) -t [image_name] [docker_file_path]
    - `docker build -f Dockerfile.dev -t hello_world_img .`


##### To Create Container
2. docker run -it(optional) --name=[container_name](optional) -p[local_machine_port : container_port] [image_name] 
    - `docker run -it --name="my-container" -p 8081:8080 my_img`


##### To List Images
3. `docker images` || `docker image ls`


##### To List Running Containers
4. `docker container ls`


##### To List All Containers(whether running or stopped)
5. `docker container ls -a`


##### To Show Running Processes
6. `docker ps`


##### To Show All Process(Running + Stopped)
7. `docker ps -a`


##### To Show Container Logs
8. `docker logs [container_name]`


##### To Get Into Running Container 
9. `docker exec -it [container_name or id] /bin/bash/`


##### To Get Out Of Container Without Exiting
10. `CTRL + P + Q`


##### To Get Out Of Container With Exiting
11. `CTRL + C` || `exit`


##### To Build Image From Running Container
12. `docker commit [container_name or id] [image_name]`


### Flags of Docker Commands

1. `-t` === tag ['mostly for name']

2. `-f` === fixed ['fixed on screen to observe process']

3. `-c` === command ['Used to give CMD command or overwrite it at runtime(at the time of creating container)']

4. `-it` === interactive-terminal ['Interactive mode while creating or running container, open the process in shell']

5. `-d` === detach ['Detach mode runs process in background not opens the shell']


6. `a` === all


### Docker-Compose Commands

##### Create and Start Container
1. `docker compose up`

##### Lists containers for a Compose project, with current status
2. `docker compose ps`

##### List running compose projects
3. `docker compose ls`

##### Start the Services
4. `docker compose start`

##### Stop the Services
5. `docker compose stop`

##### Parse, resolve and render compose file in canonical format
6. `docker compose config`

##### Display the running process
7. `docker compose top`

##### Shows the Docker Compose version information
8. `docker compose version`

##### Stop and remove containers, networks
9. `docker compose down`

##### List images used by the containers created by docker compose file
10. `docker compose images`

##### If you change a service's Dockerfile or the contents of its build directory,to rebuild it.
11. `docker compose build`


##### If you want rebuild and start services both
12. `docker compose up --build -d`

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
