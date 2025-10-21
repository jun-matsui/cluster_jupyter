ARG spark_version
FROM spark-base:latest

ARG build_date

LABEL org.label-schema.build-date=${build_date}
LABEL org.label-schema.name="Apache Spark Standalone Cluster on Docker - Spark Master Image"
LABEL org.label-schema.description="Spark master image"


EXPOSE 8080 7077
WORKDIR ${SPARK_HOME}

# Set the entrypoint to our script and the default command to start the Spark Master.
# The 'exec' in the entrypoint script will ensure the Spark Master process replaces the shell.
ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]
