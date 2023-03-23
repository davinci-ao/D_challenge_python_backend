# D_challenge_python_backend
This application environment consists a Docker container. This container contains all code of a web application for ordering drinks. This container itself must be run by the Docker App to activate the web application. 
A Docker container allows you to develop and run the server- and clientcode independent of the operating system of the computer (Windows/Linux/MacOS) To use and run a Docker container you need to install the Docker App software first.

A Docker compose structure to setup a local persistent environment with Python Flask and some boilerplate code in HTML &amp; JS for the challenge Python Backend

## Installation
- Make sure you have docker AND docker compose installed (easiest way to do this is to install docker desktop - [Download Docker Desktop](https://www.docker.com/products/docker-desktop) )
- Run the following command: docker compose --env-file=.env.docker up -d (in the folder of your repo!)
- Let the process finish setting up your environment
- Read It's Learning, after that:
- Start coding your backend in the folder "server"
- Start coding your frontend in the folder "client"
- **Don't change the location of the client and server folder!**

## Services
- Python (latest) environment with pip installed, and the following packages:
  - flask-marshmallow
  - flask-cors

Your Python webserver is accessed through [http://localhost:5000](http://localhost:5000)

## Important!
For docker to work you need to have enabled Virtualization in your BIOS (Windows users only).

## Ports
This installation uses the following ports for it's services. these ports cannot be used by any other program. If you are experiencing troubles setting this up, you should check if these ports are unused. 

| Portnumber | used by? |
|---|---|
| 5000 | Python |


## Useful commands for setting up or managing your docker environment 

|  Title | Description  | When to run? |  Command |
|---|---|---|---|
| Up Command  | Run this command to pull & setup and run/start the containers/services/networks mentioned in the docker-compose.yml. | Run this when you want to start using this environment (you need to have docker & docker compose installed - install docker desktop for the easiest setup. | docker compose --env-file=.env.docker up -d |
| Down command | Stops and removes the containers started with the "up" command (previous command). | Run this when you want to stop using the containers and services (your data will be persisted still) OR when you want to setup a new/different environment. | docker compose --env-file=.env.docker down |
| Cleanup command | Removes stopped containers, unused networks, dangling images, and dangling build cache. && also removes all images not used by a container. | Run this when you have recently used a down command and you want to prevent docker from using stored cache to build new images. | docker system prune && docker image prune -a && docker system prune |
| Start python webserver | This command executes a command in the docker container that's running python, and that command starts the Python webserver. The output is visible through the Terminal/command prompt. The server autorefreshes when you change code in the main.py document. If you introduce a breaking error in the code, the server might crash. | Run this command when you want to start the python webserver to reflect changes you might have made. The webserver is available through the URL mentioned above. To stop the webserver you can use the ^C (control + C) key combination.| docker exec -it python_flask python main.py |
