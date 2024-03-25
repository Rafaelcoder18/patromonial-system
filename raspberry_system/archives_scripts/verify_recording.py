import subprocess
import os

# Defina os caminhos de origem e destino
origem = '/home/rafael/patromonial-system/raspberry_system/rsync'
destino = '/caminho/para/destino/'

# Construa o comando rsync como uma lista de strings
comando_rsync = ["rsync", "-av", origem, destino]

while True:
    if len(os.listdir('/home/rafael/patromonial-system/raspberry_system/rsync')) == 1:
        # Execute o comando rsync
        try:
            # Use subprocess.run para executar o comando
            resultado = subprocess.run(comando_rsync, capture_output=True, text=True, check=True)
            
            # Verifique se a execução foi bem-sucedida
            if resultado.returncode == 0:
                print("A sincronização foi concluída com sucesso.")
            else:
                print("Ocorreu um erro durante a sincronização:", resultado.stderr)
        except subprocess.CalledProcessError as e:
            print("Erro durante a execução do comando:", e)
