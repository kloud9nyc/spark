from pyspark import SparkFiles
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, col, concat, explode, split
import findspark

from schemas.boston_schema import boston_schema

findspark.init("/Users/nithya/spark")

spark_builder = (
    SparkSession
        .builder
        .appName("my app")
)

spark = spark_builder.getOrCreate()

data = spark.read.csv(
    "file:////Users/nithya/PycharmProjects/PyFlow/tests/test_data/sales/boston_small.csv",
    header='true', inferSchema=True)

data.printSchema()

data.show()
