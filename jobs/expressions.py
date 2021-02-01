from pyspark import SparkFiles
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,expr
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

data = spark.read.schema(boston_schema).option("header", "true").csv('file:////Users/nithya/PycharmProjects/PyFlow'
                                                                     '/tests/test_data/sales/boston_small.csv')
# Filter
# indus = data.filter('indus > 7')

# Chaining of Operations

# indus = data.filter('indus > 7').where('tax=242')

# data.select(col('indus')).show()

# dj = data.select('*').where(expr('indus < 7'))


# Remove Nulls
# data = data.dropna()

#
# data.select(expr('indus > 7') & expr('rm > 7')).show()
#
# data.show()

# Add Column
data.withColumn('indusgrt7', expr('indus>7') & expr('rm > 7')).show()

# Add Column
data.withColumn('indusgrt7', expr('indus>7') | expr('rm > 7')).show()

#Adding Multiple Column
data.\
    withColumn('indusgrt7', expr('indus>7') & expr('rm > 7')).\
    withColumn('roomplusindus', expr('indus + rm')).show()




data.select(col("indus").alias("indus-new")).show()

data.sort(col('dis'), ascending=True).show()

data.sort(col('dis').desc_nulls_last()).show()














