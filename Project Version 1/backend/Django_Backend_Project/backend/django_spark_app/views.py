
# Create your views here.

import os
import numpy as np
# import cv2
# import netCDF4

from django.shortcuts import render
from django.conf import settings
from pyspark.sql import SparkSession
from django.http import HttpResponse




def members(request):
    return HttpResponse("Hello world!")
    # return render(request, "django_spark_app/templates/test_spark_connection.html", "salamo alikom from the other side")





def test_spark_connection(request):
    try:
        # Connect to Spark Master
        spark = SparkSession.builder \
                .appName('spark_cluster_mode_from_Django') \
                .master("spark://spark-master:7077") \
                .config("spark.driver.maxFrameSize", "100000000") \
                .config("spark.executor.maxResultSize", "100000000") \
                .config("spark.ui.showConsoleProgress", "true") \
                .getOrCreate()

        # spark.stop()

        message = "Successfully connected to Spark Master."

    except Exception as e:
        message = f"Failed to connect to Spark Master: {e}"
   
    context = {
        "message": message,
    }
    # return render(request, "django_spark_app/templates/test_spark_connection.html", context)
    return HttpResponse(message)



def read_netcdf_from_hdfs(request):
    # try:
    #     # Connect to Spark Master
    #     spark = SparkSession.builder \
    #             .appName('spark_cluster_mode') \
    #             .master("spark://spark-master:7077") \
    #             .config("spark.driver.maxFrameSize", "100000000") \
    #             .config("spark.executor.maxResultSize", "100000000") \
    #             .config("spark.ui.showConsoleProgress", "true") \
    #             .getOrCreate()

    #     # Read NetCDF file from HDFS

    #     hadoop fs -get "hdfs://namenode:9000/data/2m_temperature_2002_2022.nc" "/data/tmp_folder" 

    #     nc_file = "/data/tmp_folder/2m_temperature_2002_2022.nc" 

    #     from sparkxarray.reader import ncread
    #     rdd = ncread(sc, nc_file, mode='single', partition_on=['time'], partitions=100)

    #     rdd_count = rdd.count()

    #     # hdfs_path = "hdfs://namenode:9000/data/2m_temperature_2002_2022.nc"
    #     # spark_df = spark.read.format("netcdf").load(hdfs_path)

    #     # Show the DataFrame (optional)
    #     # spark_df.show()

    #     spark.stop()
    #     message = "Successfully read NetCDF file from HDFS."
    # except Exception as e:
    #     message = f"Failed to read NetCDF file from HDFS: {e}"

    # context = {
    #     "message": rdd_count,
    # }
    # return render(request, "django_spark_app/templates/read_netcdf.html", context)
    return render(request, "django_spark_app/templates/read_netcdf.html", "context")


