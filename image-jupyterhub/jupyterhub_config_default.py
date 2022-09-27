import os, nativeauthenticator,tornado

c.JupyterHub.template_paths = [f'{os.path.dirname(nativeauthenticator.__file__)}/templates/']
c.Authenticator.allowed_users={"ericjiang"}
c.Authenticator.admin_users={"ericjiang"}
c.JupyterHub.spawner_class="kubespawner.KubeSpawner"
c.KubeSpawner.image="moonlight165/jupyter-hub-singleuser:0.0.4"
c.KubeSpawner.pod_name_template="jupyter-{username}"
c.KubeSpawner.cpu_guarantee=0.05
c.KubeSpawner.cpu_limit=1
c.KubeSpawner.mem_guarantee="1G"
c.KubeSpawner.mem_limit="4G"
c.KubeSpawner.env_keep=["http_proxy","https_proxy"]
c.KubeSpawner.environment={"JUPYTERHUB_API_URL": "http://localhost:31000/data-analyze/jupyter-hub/hub/api"} #k8s ingress
c.KubeSpawner.namespace="data-analyze"
c.KubeSpawner.service_account="airflow"
c.KubeSpawner.volume_mounts=[{"name":"data-analyze","mountPath":"/home/livy","subPath": "wei/jupyterhub-kube/{username}"},
                             {"name":"data-analyze","mountPath":"/opt/hadoop-2.7.3","subPath": "wei/jupyterhub-kube/hadoop-2.7.3"}]
c.KubeSpawner.volumes=[{"name": "data-analyze","persistentVolumeClaim": {"claimName": "data-analyze"}}]
c.KubeSpawner.notebook_dir="/home/livy"
c.KubeSpawner.working_dir="/home/livy"
c.KubeSpawner.args=["--SingleUserNotebookApp.default_url=/tree"]
c.KubeSpawner.http_timeout=300
c.KubeSpawner.start_timeout=300
c.KubeSpawner.image_pull_policy="Always"
c.KubeSpawner.profile_list=[{"display_name":"spark environment","slug":"pyspark","description":"image: jupyter-hub-singleuser:0.0.4-pyspark",
                             "kubespawner_override":{"image":"moonlight165/jupyter-hub-singleuser:0.0.4-pyspark"}},
                            {"display_name":"intern environment","slug":"intern","description":"image: jupyter-hub-singleuser:0.0.4-intern",
                             "kubespawner_override":{"image":"moonlight165/jupyter-hub-singleuser:0.0.4-intern"}}]
c.KubeSpawner.extra_pod_config={"hostAliases":[{"ip":"192.168.52.129","hostnames":["hadoop1"]}]}
c.LocalAuthenticator.create_system_users=False
c.JupyterHub.authenticator_class="nativeauthenticator.NativeAuthenticator"
c.NativeAuthenticator.open_signup=True
c.NativeAuthenticator.minimum_password_length=6
c.NativeAuthenticator.check_common_password=True
c.NativeAuthenticator.allowed_failed_logins=5
c.NativeAuthenticator.seconds_before_next_try=180
c.JupyterHub.shutdown_on_logout=True
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.proxy_class = "traefik_toml"
c.TraefikTomlProxy.traefik_api_password = "admin"
c.TraefikTomlProxy.traefik_api_username = "admin"
c.TraefikTomlProxy.traefik_log_level = "INFO"
c.JupyterHub.base_url ="/data-analyze/jupyter-hub" #k8s ingress