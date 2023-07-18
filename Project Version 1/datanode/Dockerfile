FROM aitabbou/spark_hadoop_base_image:1.0


LABEL maintainer="samir.1.aitabbou@gmail.com"



HEALTHCHECK CMD curl -f http://localhost:9864/ || exit 1

ENV HDFS_CONF_dfs_datanode_data_dir=file:///hadoop/dfs/data
RUN mkdir -p /hadoop/dfs/data
# RUN mkdir -p /opt/hadoop/logs

VOLUME /hadoop/dfs/data



ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 9864

CMD ["/run.sh"]

