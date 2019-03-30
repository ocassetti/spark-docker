Docker image for developing with Apache Spark
===============

Use at your own risk! This is not meant for production

# What is for

This a docker image base on Alpine Linux. It has spark installed in
`opt/spark` and Java 8.
Various Python packages for data processing are also installed.
The default entry point is `bash` (see section [[ Run | Run ]]).
The idea is to put your files in `workspace/` and then have a console on which
to run Spark or PySpark

Jupyter is available too


## Build

```
docker build -t 'spark-2.3.3' spark-2.3.3
```

## Run
```
docker run -v $(pwd)/workspace:/mnt/workspace/ -i -t spark-2.3.3
```
