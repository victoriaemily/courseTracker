container_name=aws_container
docker_image=54d61678f24a
docker run -td --name=$container_name $docker_image
docker cp ./requirements.txt $container_name:/

docker exec -i $container_name /bin/bash  < ./docker_install.sh
docker cp $container_name:/venv/lib/python3.8/deployment_package.zip deployment_package.zip # copied in the root dir
docker stop $container_name #stops container
docker rm $container_name

zip -g deployment_package.zip lambda_function.py