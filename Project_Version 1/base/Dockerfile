
FROM ubuntu:latest
LABEL maintainer="samir.1.aitabbou@gmail.com"

# Install required packages
RUN apt-get update && apt-get install -y curl  openjdk-8-jdk python3 python3-pip
RUN apt-get install -y nano iputils-ping

# Set environment variables
ENV HADOOP_VERSION 3.3.5
ENV SPARK_VERSION 3.4.0
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

ENV PATH=$PATH:$SPARK_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# Install Hadoop
RUN curl -s https://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz | tar -xz -C /opt/ && \
    ln -s /opt/hadoop-$HADOOP_VERSION /opt/hadoop && \
    ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /opt/hadoop/etc/hadoop && \
    mkdir -p /opt/hadoop/logs && \
    chown -R root:root /opt/hadoop-$HADOOP_VERSION

# Install Spark
RUN curl -s https://archive.apache.org/dist/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz | tar -xz -C /opt/ && \
    ln -s /opt/spark-$SPARK_VERSION-bin-hadoop3 /opt/spark && \
    mkdir -p /opt/spark/logs && \
    chown -R root:root /opt/spark-$SPARK_VERSION-bin-hadoop3

# Upgrade pip and install Python packages
RUN pip3 install --upgrade pip && \
    pip3 install pyspark==3.4.0 findspark==2.0.1
    


COPY core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
COPY hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml