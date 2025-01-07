from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when, isnan
import os


spark = SparkSession.builder \
    .appName("Netflix EDA") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

#dataset
data_path = "/opt/spark/work-dir/data/netflix_titles.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Print schema and record count
df.printSchema()
print(f"Total records: {df.count()}")


df.show(10)


missing_values = df.select([
    count(when(col(c).isNull() | isnan(c), c)).alias(c) for c in df.columns
])
missing_values.show()

# Calculate and display missing value percentages
missing_percentage = df.select([
    ((count(when(col(c).isNull() | isnan(c), c)) / df.count()) * 100).alias(c) for c in df.columns
])
missing_percentage.show()


df.describe().show()

# Perform exploratory data analysis (EDA)
df.select("type").distinct().show()
df.groupBy("type").count().show()
df.groupBy("country").count().orderBy(col("count").desc()).show(10)
df.groupBy("release_year").count().orderBy(col("release_year").desc()).show(10)
df.filter((col("country") == "United States") & (col("type") == "Movie")).show(5)

# Save cleaned data to a new CSV file
output_dir = "/opt/spark/work-dir/data"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "cleaned_netflix_data.csv")
df.write.csv(output_path, header=True, mode="overwrite")

print(f"Cleaned data saved to {output_path}")

# Stop the Spark session
spark.stop()
