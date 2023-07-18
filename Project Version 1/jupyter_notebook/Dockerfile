
FROM aitabbou/spark_hadoop_base_image:1.0


LABEL maintainer="samir.1.aitabbou@gmail.com"



# Install Jupyter Notebook
RUN pip install jupyter

#install git 
RUN apt-get update && \
    apt-get install -y git

#install ncdump to manipulate netcdf files
# RUN apt-get update && \
#     apt-get install netcdf-bin
# RUN pip3 install matplotlib

#install and setup spark-xarray
RUN git clone https://github.com/andersy005/spark-xarray.git && cd spark-xarray && python3 setup.py install
ENV PYTHONPATH="/spark-xarray/sparkxarray:${PYTHONPATH}"
RUN echo 'export PYTHONPATH="/spark-xarray/sparkxarray:${PYTHONPATH}"' >> /root/.bashrc


# install required libriries
RUN pip install xarray==2023.3.0 netCDF4==1.6.2 scipy==1.10.0


# Set the working directory
RUN mkdir -p /app/data /app/notebooks

WORKDIR /app

# Expose the Jupyter Notebook port
EXPOSE 8889

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8889","--allow-root"]

