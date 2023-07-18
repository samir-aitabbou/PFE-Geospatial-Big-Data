# build images
echo "************************* Start building ************************* "

# docker build -t aitabbou/spark_hadoop_base_image:1.0 ./base
docker build -t aitabbou/datanode:1.0 ./datanode
docker build -t aitabbou/namenode:1.0 ./namenode
docker build -t aitabbou/spark-master:1.0 ./master 
docker build -t aitabbou/spark-worker:1.0 ./worker 
docker build -t aitabbou/jupyter-notebook:1.0 ./jupyter_notebook

echo "************************* End building ************************* "

# start the docker Containers
echo "*************************  starting Containers ************************* "
docker compose up 