#!/bin/bash

# hostname = spark master ip
export SPARK_MASTER_HOST=`hostname`

#sourcing spark-conf.sh and load-spark-env.sh in the actual script (read and execute commands)
. "opt/spark/sbin/spark-config.sh"
. "opt/spark/bin/load-spark-env.sh"

mkdir -p $SPARK_MASTER_LOG

ln -sf /dev/stdout $SPARK_MASTER_LOG/spark-master.out

cd opt/spark/bin && spark-class org.apache.spark.deploy.master.Master \
    --ip $SPARK_MASTER_HOST --port $SPARK_MASTER_PORT --webui-port $SPARK_MASTER_WEBUI_PORT >> $SPARK_MASTER_LOG/spark-master.out