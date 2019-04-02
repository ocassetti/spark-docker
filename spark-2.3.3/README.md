# DOCKER image for development

Build an image that can be used for development of Spark with python

# Using jupyter

1. Build the image using the `build.sh` command
2. Edit the `run.sh` if necessary
3. By default the entry-point run jupyter in `/mnt/workspace` which is mapped to the workspace directory
4. Get the URL for connecting from the terminal

# Using spark from Jupyter

You can use `findspark` to spin a spark job directly from Jupyter

```
import findspark
findspark.init(spark_home="/opt/spark")
import pyspark

sc = pyspark.SparkContext(appName="local-dev")
```
