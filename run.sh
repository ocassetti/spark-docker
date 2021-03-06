docker build -t 'spark-2.3.3' spark-2.3.3

echo "Starting endpoint..."
docker run -v $(pwd)/workspace:/mnt/workspace/ -p 8888:8888  -i -t spark-2.3.3

echo "Cleaning up executions"
docker rm $(docker ps -aq)
