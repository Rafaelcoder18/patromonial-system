"""
Autor: Rafael Prado
Data: 19/03/2024
Descrição: Este script é responsável por concatenar os vídeos gravados em um único arquivo de vídeo, com o objetivo de realizar o streaming do vídeo.
"""

from moviepy.editor import VideoFileClip, concatenate_videoclips # Biblioteca para manipulação de vídeo
import os # Biblioteca do sistema

# Diretório onde os vídeos estão localizados
diretorio = '/home/rafael/patromonial-system/raspberry_system/recordings/'

# Loop infinito para verificar se existem dois arquivos de vídeo na pasta e realizar a concatenação
while True:
    if len(os.listdir(diretorio)) == 2:
        videos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.avi')] # Lista de arquivos de vídeo que você deseja concatenar
        videos.sort() # Ordena a lista de arquivos de vídeo

        video_clips = [] # Lista para armazenar os objetos VideoFileClip

        # Cria um objeto VideoFileClip para cada vídeo
        for video in videos:
            caminho_video = os.path.join(diretorio, video)
            video_clips.append(VideoFileClip(caminho_video))

        # Concatena os vídeos
        video_concatenado = concatenate_videoclips(video_clips)

        # Salva o vídeo concatenado em um novo arquivo
        video_concatenado.write_videofile('video_concatenado.avi', codec='libx264')

        # Fecha todos os objetos VideoFileClip
        for clip in video_clips:
            clip.close()

