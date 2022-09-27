FROM jupyterhub/jupyterhub
RUN apt-get --allow-releaseinfo-change update && \
    apt-get install -y libgtk2.0-dev sudo git python3.8-dev libkrb5-dev vim && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata &&\
    TZ=Asia/Taipei &&\
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &&\
    echo $TZ > /etc/timezone &&\
    dpkg-reconfigure -f noninteractive tzdata &&\
    rm -rf /var/lib/apt/lists/* && \
    /usr/bin/pip install cpython==0.0.6 jupyterhub-nativeauthenticator==1.0.5 jupyterhub-kubespawner==4.1.0 jupyterhub-traefik-proxy==0.3.0 && \
    /usr/bin/python3 -m jupyterhub_traefik_proxy.install --traefik --etcd --consul --output=/usr/local/bin && \
    useradd -l -u 1000 -g 100 -m jovyan && echo "jovyan:MjgyMTA2NDdAaXQK" | chpasswd && adduser jovyan sudo && \
    chown -R 1000:100 /srv/jupyterhub