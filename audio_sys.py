import audiocore
import audiopwmio
import board
import audiobusio
import config

# Inicjalizacja I2S (Wzmacniacz MAX98357)
# Piny są stałe dla Prop-Maker Feather, ale używamy definicji z board dla pewności
try:
    audio_out = audiobusio.I2SOut(board.GPIO17, board.GPIO16, board.GPIO18)
except Exception:
    print("BŁĄD AUDIO: Nie wykryto I2S!")
    audio_out = None

def play(filename):
    """
    Odtwarza plik WAV z folderu /sounds
    """
    if not audio_out:
        return

    try:
        # Otwieramy plik
        wave_file = open(f"/sounds/{filename}", "rb")
        wave = audiocore.WaveFile(wave_file)
        
        # Jeśli coś gra, zatrzymaj
        if audio_out.playing:
            audio_out.stop()
            
        audio_out.play(wave)
    except Exception as e:
        print(f"Błąd odtwarzania {filename}: {e}")