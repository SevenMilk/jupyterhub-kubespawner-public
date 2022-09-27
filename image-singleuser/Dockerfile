FROM jupyterhub/singleuser:1.0.0
USER root
RUN apt-get --allow-releaseinfo-change update && \
    apt-get install -y libgtk2.0-dev zlib1g-dev libjpeg-dev libpng-dev libkrb5-dev libssl-dev libffi-dev\
                       sudo git build-essential vim gcc python3-dev curl cargo && \
    apt-get install java-common &&\
    apt-get install -y wget && wget https://corretto.aws/downloads/latest/amazon-corretto-8-x64-linux-jdk.deb &&\
    dpkg --install amazon-corretto-8-x64-linux-jdk.deb &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata &&\
    TZ=Asia/Taipei &&\
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &&\
    echo $TZ > /etc/timezone &&\
    dpkg-reconfigure -f noninteractive tzdata &&\
    rm -rf /var/lib/apt/lists/* amazon-corretto-8-x64-linux-jdk.deb &&\
    ln -s /usr/lib/jvm/java-1.8.0-amazon-corretto /usr/lib/jvm/java-8-openjdk-amd64 &&\
    mkdir -p /home/webuser/tmp && chmod 777 /home/webuser/tmp &&\
    groupadd -g 3004 jupyter && \
    useradd -l -u 3001 -g 3004 -m livy && echo "livy:bgl2eqo" | chpasswd && adduser livy sudo && \
    echo "livy ALL=(ALL:ALL) ALL" >> /etc/sudoers && \
    chown -R 3001:3004 /opt/conda &&\
    chown -R 3001:3004 /tmp
USER livy
WORKDIR /home/livy
ENV NB_USER=livy
ENV NB_UID=3001
ENV NB_GID=3004
ENV CHOWN_HOME=/home/livy
ENV HOME=/home/livy
ARG file_name=$file_name
COPY --chown=3001:3004 .sparkmagic /home/livy/.sparkmagic
COPY --chown=3001:3004 pyspark-template.ipynb /home/livy/pyspark-template.ipynb
COPY --chown=3001:3004 default.txt /home/livy/default.txt
COPY --chown=3001:3004 ${file_name}.txt /home/livy/${file_name}.txt
RUN /opt/conda/bin/pip install --no-cache-dir --ignore-installed -r default.txt && \
    /opt/conda/bin/pip install --no-cache-dir --ignore-installed -r ${file_name}.txt && \
    /opt/conda/bin/jupyter contrib nbextension install --sys-prefix && \
    /opt/conda/bin/jupyter nbextensions_configurator enable --sys-prefix && \
    /opt/conda/bin/jupyter nbextension install --py jupyter_nbextensions_configurator --sys-prefix && \
    /opt/conda/bin/jupyter nbextension enable jupyter_nbextensions_configurator --py --sys-prefix && \   
    /opt/conda/bin/jupyter nbextension enable --py --sys-prefix widgetsnbextension && \
    /opt/conda/bin/jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/sparkkernel --sys-prefix && \
    /opt/conda/bin/jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/pysparkkernel --sys-prefix && \    
    /opt/conda/bin/jupyter-kernelspec install /opt/conda/lib/python3.7/site-packages/sparkmagic/kernels/sparkrkernel --sys-prefix && \
    /opt/conda/bin/jupyter serverextension enable --py sparkmagic && \
    rm -rf /opt/conda/pkgs/* && \
    echo HADOOP_HOME=/opt/hadoop-2.7.3 >> /home/livy/.bashrc && \
    echo HADOOP_CONF_DIR=/opt/hadoop-2.7.3/etc/hadoop >> /home/livy/.bashrc && \
    echo PATH=$PATH:/opt/hadoop-2.7.3/bin >> /home/livy/.bashrc  && \
    echo JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 >> /home/livy/.bashrc && \
    /bin/sh -c fix-permissions /etc/jupyter/

# docker build --force-rm --no-cache --build-arg file_name=pyspark -t moonlight165/jupyter-hub-singleuser:0.0.4-pyspark -f ./Dockerfile .