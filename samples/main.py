from pyspark import SparkConf
from pyspark.sql import SparkSession
import time
import os
import sys

conf = SparkConf().setAppName("test")
spark = SparkSession.builder.config(conf=conf).enableHiveSupport().getOrCreate()
print("============")

for p, s, d in os.walk("/opt/spark/work-dir/"):
    print(f"{d}, {s}, {d}")

print("============")
currentDirectory = os.getcwd()
print(currentDirectory)
for p, s, d in os.walk(currentDirectory):
    print(f"{d}, {s}, {d}")

time.sleep(300)
