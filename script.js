window.addEventListener('load', function() {
    var audio = document.getElementById('miAudio');
    
    // Asigna la ruta del archivo de audio recortado
    audio.src = 'audio/happy_together_cut.mp4';
    // Retrasa la reproducción por 3 segundos (3000 milisegundos)
    document.addEventListener('click', function() {
        audio.play().catch(function(error) {
            console.log('Error de reproducción automática: ', error);
        });
    }, { once: true });
});