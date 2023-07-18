FROM aitabbou/spark_hadoop_base_image:1.0


LABEL maintainer="samir.1.aitabbou@gmail.com"


COPY master.sh /  
RUN chmod +x master.sh

# Install system dependencies required by netCDF4 and xarray
RUN apt-get update && apt-get install -y \
    libnetcdf-dev \
    libhdf5-dev \
    git

# install required packages for sparkxarray : 
RUN pip3 install netCDF4 xarray dask numpy scipy pandas distributed geopandas toolz cloudpickle 

# install sparkxarray and add sparkxarray directory to envirement variable
#install git 
# RUN apt-get update && \
#     apt-get install -y git 

#install and setup spark-xarray
RUN git clone https://github.com/andersy005/spark-xarray.git && cd spark-xarray && python3 setup.py install
ENV PYTHONPATH="/spark-xarray/sparkxarray:${PYTHONPATH}"
RUN echo 'export PYTHONPATH="/spark-xarray/sparkxarray:${PYTHONPATH}"' >> /root/.bashrc


ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /opt/spark/logs

EXPOSE 8080 7077 6066

CMD ["/bin/bash", "/master.sh"]