from pytube import YouTube

# URL del video de YouTube que quieres descargar
video_url = 'https://www.youtube.com/watch?v=9ZEURntrQOg'

# Crear un objeto YouTube
yt = YouTube(video_url)

# Seleccionar el stream de audio
audio_stream = yt.streams.filter(only_audio=True).first()

# Descargar el audio
audio_stream.download(output_path='../audio', filename='happy_together.mp4')

print("Descarga completada")
