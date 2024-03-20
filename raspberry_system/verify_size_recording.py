#!/usr/bin/env python3

"""
Autor: Rafael Prado
Data: 19/03/2024
Descrição: Este script é responsável por verificar o tamanho do arquivo de vídeo gravado e, caso atinja 2MB, move o arquivo para a pasta de análise.
"""

import os, shutil # Bibliotecas do sistema

# Verifica a quantidade de arquivos na pasta de análise e o tamanho do arquivo de vídeo gravado. Caso seja maior ou igual a 2MB, move o arquivo para a pasta de análise com a quantidade de arquivos existentes no nome.
while True: 
    try:
        quantidade_arquivos = len(os.listdir('/home/rafael/patromonial-system/raspberry_system/analisys'))
        if os.path.getsize('raspberry_system/video_gravado.avi') >= 2097152:
            shutil.move('raspberry_system/video_gravado.avi', f'/home/rafael/patromonial-system/raspberry_system/analisys/video_analisado_{quantidade_arquivos}.avi')
    except:
        pass