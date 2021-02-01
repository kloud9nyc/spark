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

# data = spark.read.csv(
#     "file:////Users/nithya/PycharmProjects/PyFlow/tests/test_data/sales/boston_small.csv",
#     header='true', schema=boston_schema)

data = spark.read.schema(boston_schema).option("header", "true").csv("file:////Users/nithya/PycharmProjects/PyFlow"
                                                                     "/tests/test_data/sales/boston_small.csv")

data.printSchema()

data.show()
