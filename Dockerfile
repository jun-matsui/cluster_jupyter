# Usamos a imagem oficial do PySpark como base.
# É uma boa prática fixar a versão para garantir a consistência. Ex: :v3.5.1
FROM apache/spark-py:v3.4.0
# Trocamos para o usuário root para instalar pacotes
USER root

# Otimização: Combinamos múltiplos comandos RUN em um só para reduzir as camadas da imagem.
# - Atualizamos o pip.
# - Instalamos Jupyter Lab e os widgets necessários.
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir jupyterlab ipywidgets boto3
RUN pip install --no-cache-dir pyspark==3.4.0

# Baixamos os JARs necessários para o Spark se comunicar com S3 (MinIO)
# As versões devem ser compatíveis com a versão do Hadoop usada pelo Spark 3.4.0 (Hadoop 3.3.4)
ARG HADOOP_VERSION=3.3.4
ARG AWS_SDK_VERSION=1.12.262

RUN apt-get update && apt-get install -y wget && \
    wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar && \
    wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar && \
    apt-get remove -y wget && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
# Trocamos de volta para o usuário padrão 'spark' por segurança
 
# Define o diretório de trabalho padrão dentro do contêiner
WORKDIR /opt/spark/work-dir
