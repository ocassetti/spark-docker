#!/bin/bash

source /etc/profile.d/spark.sh

echo "1+1" > tmp.py
spark-submit --packages org.apache.spark:spark-avro_2.11:2.4.0,org.apache.hadoop:hadoop-aws:2.7.7 tmp.py
rm tmp.py
