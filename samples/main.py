from pyspark import SparkConf, SparkFiles
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

SparkFiles[]

sys.path.append("lib.zip")
import test_spark.unit_a as unit_a
unit_a.hello()
os.chdir(SparkFiles.getRootDirectory())
with open("data.txt", 'r') as fh:
    print(fh.read())

#time.sleep(300)
spark.stop()
