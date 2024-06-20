from pydub import AudioSegment

# Ruta del archivo de audio original
audio_path = "../audio/happy_together.mp4"

# Ruta para guardar el archivo de audio recortado
output_path = "../audio/happy_together_cut.mp4"

# Cargar el archivo de audio
audio = AudioSegment.from_file(audio_path)

# Definir el tiempo de inicio y final (en milisegundos)
start_time = 1 * 60 * 1000  # 1 minuto
end_time = 2 * 60 * 1000    # 2 minutos

# Recortar el audio
audio_recortado = audio[start_time:end_time]

# Aplicar fade-in al inicio
fade_in_duration = 7 * 1000
audio_fade_in = audio_recortado.fade_in(fade_in_duration)

# Aplicar fade-out al final
fade_out_duration = 7 * 1000  
audio_fade_in_out = audio_fade_in.fade_out(fade_out_duration)

# Guardar el audio recortado
audio_fade_in_out.export(output_path, format="mp4")

print("Recorte completado")