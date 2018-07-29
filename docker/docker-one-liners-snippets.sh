##################################################################
# One liners for docker legacy and current versions
##################################################################
# Stop all docker containers on a host
docker stop $(docker ps -a -q)
## or
docker ps -a -q | xargs -n 1 -P 8 -I {} docker stop {}

# Remove all docker containers on a host
docker rm $(docker ps -a -q)

# Remove all images
docker rmi $(docker images -q)

# Remove all containers with keyword cluster
docker rm $(docker ps -a |grep cluster|awk '{print $1;}')

# Remove all images with keyword cluster
docker rmi $(docker images |grep cluster|awk '{print $3;}')

# dstop() { docker stop $(docker ps -a -q); } alias dstop=dstop

# Stop exited containers and delete only non-tagged images
docker ps --filter 'status=Exited' -a | xargs docker stop docker images --filter "dangling=true" -q | xargs docker rmi



##################################################################
# Faster way to purge in newer versions of docker >= 1.13
##################################################################
# Complete system clean up
docker system prune


# To individually delete all the components, use the following commands.

docker container prune
docker image prune
docker network prune
docker volume prune
