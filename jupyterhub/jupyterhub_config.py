import os

# --- Configuração Geral ---
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# --- Configuração do Autenticador ---
c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.DummyAuthenticator.password = "test"
c.Authenticator.allow_all = True

c.NativeAuthenticator.enable_auth_state = True
c.NativeAuthenticator.open_signup = True

# Define a lista de usuários que podem fazer login
c.Authenticator.allowed_users = {'admin', 'jun'} # <-- ADICIONE 'jun'

# Define os usuários administradores
c.Authenticator.admin_users = {'admin', 'jun'} # <-- ADICIONE 'jun'

# --- Configuração do Spawner (continua igual) ---
# --- Configuração do Spawner (como os notebooks são criados) ---
# Imagem Docker que será usada para cada usuário.
# Apontamos para a nossa nova imagem customizada que tem o Jupyter AI.
# c.DockerSpawner.image = os.environ.get('DOCKER_JUPYTER_IMAGE', 'jupyter/pyspark-notebook:spark-3.3.2')
c.DockerSpawner.image = os.environ.get('docker pspip list | grep jupyter-ai', 'custom-pyspark-notebook-with-ai:latest') # <-- MUDOU AQUI

c.DockerSpawner.network_name = 'databricks-local_data-net'
c.DockerSpawner.use_internal_ip = True
notebook_dir = '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': notebook_dir,
    os.path.abspath('../jupyter_notebooks'): os.path.join(notebook_dir, 'shared_notebooks')
}
c.DockerSpawner.extra_host_config = {'privileged': True}
c.DockerSpawner.remove = True
c.JupyterHub.hub_ip = '0.0.0.0'

# import os jovyan@58e0a3802359:/usr$

# # --- Configuração Geral ---
# c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
# c.DummyAuthenticator.password = "test"
# c.Authenticator.allow_all = True
# # --- Configuração do Spawner (como os notebooks são criados) ---
# # Imagem Docker que será usada para cada usuário.
# # MUDAMOS A VERSÃO AQUI PARA CORRESPONDER AO CLUSTER BDE
# c.DockerSpawner.image = os.environ.get('DOCKER_JUPYTER_IMAGE', 'jupyter/pyspark-notebook:spark-3.3.0') # <-- MUDOU AQUI


# # --- Configuração do Spawner (como os notebooks são criados) ---
# # Imagem Docker que será usada para cada usuário.
# # MUDAMOS PARA A IMAGEM DO BDE PARA GARANTIR COMPATIBILIDADE DE PYTHON
# c.DockerSpawner.image = os.environ.get('DOCKER_JUPYTER_IMAGE', 'bde2020/spark-notebook:3.3.0-hadoop3.3') # <-- MUDOU AQUI

# # Nome da rede Docker que conecta todos os nossos serviços
# c.DockerSpawner.network_name = 'databricks-local_data-net'
# c.DockerSpawner.use_internal_ip = True

# # Diretório de trabalho dentro do notebook do usuário
# notebook_dir = '/home/jovyan/work'
# c.DockerSpawner.notebook_dir = notebook_dir

# # Monta volumes para persistir o trabalho do usuário e compartilhar a pasta 'notebooks'
# c.DockerSpawner.volumes = {
#     'jupyterhub-user-{username}': notebook_dir,
#     os.path.abspath('../notebooks'): os.path.join(notebook_dir, 'shared_notebooks')
# }
# c.DockerSpawner.extra_host_config = {'privileged': True}
# c.DockerSpawner.remove = True
# c.JupyterHub.hub_ip = '0.0.0.0'
