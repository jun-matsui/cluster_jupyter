ARG spark_version
FROM spark-base:latest

ARG SPARK_MASTER_HOST=spark-master
ARG SPARK_MASTER_PORT=7077
ENV SPARK_WORKER_CORES 4
ENV SPARK_WORKER_MEMORY 4g

ARG build_date

LABEL org.label-schema.build-date=${build_date}
LABEL org.label-schema.name="Apache Spark Standalone Cluster on Docker - Spark Worker Image"
LABEL org.label-schema.description="Spark worker image"

# Spark Worker UI port
EXPOSE 8081
WORKDIR ${SPARK_HOME}

ENTRYPOINT ["/opt/entrypoint.sh"]
# CMD ["bin/spark-class", "org.apache.spark.deploy.worker.Worker", "spark://$SPARK_MASTER_HOST:$SPARK_MASTER_PORT"]
