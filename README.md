[![Packages Build Status](https://circleci.com/gh/tzring/Docker-Container-Project/tree/main.svg?style=shield)](https://circleci.com/gh/tzring/Docker-Container-Project) 

# Docker-Container-Project
This is a containerized change machine app. The program will ask for the amount of change, and give the optimal coins needed for the change.

## Docker Hub Repository
This project is available at: https://hub.docker.com/repository/docker/tzring/ids721_project. 

Note that the coin change machine is implemented in tag ver3.

## Instructions for runing the program

### Install Docker
Please check the installation instruction on their [official website](https://docs.docker.com/get-docker/).

### Pull the image from Docker Hub
```
docker pull tzring/ids721_project:ver3
```

### Run the App
```
docker run -it tzring/ids721_project:ver3 python app.py
```
