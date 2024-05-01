### Commands Of Docker

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



### See The Difference

1. CMD VS ENTRYPOINT
2. COPY VS ADD