rom uuid import UUID
from pyspark.sql.types import *

def getUUID():
        return uuid.uuid4().bytes

# print(getUUID())

spark.udf.register("UUID" ,  getUUID , BinaryType() )
spark.sql("select UUID() as id ").write.format("jdbc").option("url", "jdbc:postgresql://localhost/postgres?user=xxx&password=xxx")\
                 .option("dbtable", "xxxx").option("user" , "xxx").option("password", "xxx").mode("append").save()
