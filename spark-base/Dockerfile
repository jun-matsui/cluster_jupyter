# Comece com a imagem base do Jupyter PySpark
FROM spark:3.5.7-scala2.12-java17-python3-ubuntu

ARG build_date

USER root

ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077

ARG shared_workspace=/opt/workspace

RUN mkdir -p ${shared_workspace}/data && \
    mkdir -p /usr/share/man/man1

RUN apt update

# Instala o pacote tzdata para configurar o fuso horário
RUN apt-get install -y tzdata
# Define a variável de ambiente TZ para o fuso horário de Brasília
ENV TZ="America/Sao_Paulo"
# Configura o link simbólico para /etc/localtime
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# -- Runtime
RUN mkdir -p /opt/spark/logs
VOLUME ${shared_workspace}
# CMD ["bash"]
CMD ["sleep", "infinity"]
