"""
Autor: Rafael Prado
Data: 19/03/2024
Descrição: Este script é responsável por capturar o vídeo da câmera e gravar em um arquivo de vídeo.
"""

import cv2 # Biblioteca para captura e processamento de vídeo
import os, threading as th, time # Bibliotecas do sistema
import queue # Biblioteca para criar uma fila de frames

cap = cv2.VideoCapture(0) # Define a camera a ser utilizada
fourcc = cv2.VideoWriter_fourcc(*'XVID') # Define o codec a ser utilizado
recording = None # Variável para armazenar o gravador de vídeo
analys = None # Variável para armazenar o analisador de vídeo

def create_video_writer():
    """
    Função responsável por criar o arquivo onde o vídeo será gravado.
    """
    global recording
    global analys
    while True: # Loop infinito para validar se o arquivo existe
        if not os.path.exists('/home/rafael/patromonial-system/raspberry_system/video_gravado.avi'): # Se o arquivo não existir, cria um novo passando o caminho, o codec e a quantidade de frames por segundo
            recording = cv2.VideoWriter('/home/rafael/patromonial-system/raspberry_system/video_gravado.avi', fourcc, 8, (640, 480))

def get_recording():
    """
    Função responsável por capturar o vídeo da câmera e gravar no arquivo de vídeo.
    """
    global recording
    global analys
    while True:
        ret, frame = cap.read() # Captura o frame da câmera
        if not ret: # Se não conseguir capturar o frame, encerra o loop
            break
        if recording is not None: # Se o gravador de vídeo estiver criado, grava o frame
            recording.write(frame)

# Inicializa a criação do gravador de vídeo
instance_create_video = th.Thread(target=create_video_writer)
instance_create_video.start()

# Espera um pouco para garantir que o gravador de vídeo seja criado
time.sleep(1)

# Inicia a gravação do vídeo
instance_get_recording = th.Thread(target=get_recording)
instance_get_recording.start()


# Espera que todas as threads terminem
instance_create_video.join()
instance_get_recording.join()

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
