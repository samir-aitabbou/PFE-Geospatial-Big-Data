#!/bin/bash


# stop and remove all containers
docker stop $(docker ps -a -q)
echo "************************* all containers are stoped ************************* "

docker rm $(docker ps -a -q)
echo "************************* all containers are removed ************************* "

# remove all docker networks
# docker network prune -f
# echo "************************* all networks are removed ************************* "

# start the docker compose stack
echo "*************************  starting Containers ************************* "
docker compose up 