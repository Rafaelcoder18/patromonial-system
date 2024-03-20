"""
Autor: Rafael Prado
Data: 19/03/2024
Descrição: Este script é responsável por aplicar o modelo de IA nos arquivos de vídeo da pasta de análise e move para a pasta de gravação.
"""

from ultralytics import YOLO # Biblioteca de IA
import os, shutil # Bibliotecas do sistema

model = YOLO('yolov8n.pt') # Carrega o modelo de IA
cont = 0 # Define um contador para os arquivos de vídeo

# Aplica o modelo de IA nos arquivos de vídeo da pasta de análise e move para a pasta de gravação.
while True:
     for videos in os.listdir('/home/rafael/patromonial-system/raspberry_system/analisys'):
          results = model(f'/home/rafael/patromonial-system/raspberry_system/analisys/{videos}')
          print(results)
          shutil.move(f'/home/rafael/patromonial-system/raspberry_system/analisys/{videos}', f'/home/rafael/patromonial-system/raspberry_system/recordings/recording_{cont}.avi')
          cont += 1
