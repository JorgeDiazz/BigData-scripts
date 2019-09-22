from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('5th_exercise').getOrCreate()
df = spark.read.option("inferSchema", "true").csv("yellow_tripdata_2019-06.csv", header=True).cache()
dff = spark.read.option("inferSchema", "true").csv("taxi*", header=True)

df1 = dff.where('Borough like "Bronx"')

df1 = df1.join(df, F.col('DOLocationID') == F.col('LocationID')).count()

print(df1)