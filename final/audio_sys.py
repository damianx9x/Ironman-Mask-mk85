try:
    import audiocore
except Exception as e:
    audiocore = None
    print("BLAD AUDIO: brak audiocore:", e)

try:
    import audiobusio
except Exception as e:
    audiobusio = None
    print("BLAD AUDIO: brak audiobusio:", e)

try:
    import board
except Exception as e:
    board = None
    print("BLAD AUDIO: brak board:", e)


try:
    if audiobusio and board:
        if hasattr(board, "I2S_BIT_CLOCK") and hasattr(board, "I2S_WORD_SELECT") and hasattr(board, "I2S_DATA"):
            audio_out = audiobusio.I2SOut(board.I2S_BIT_CLOCK, board.I2S_WORD_SELECT, board.I2S_DATA)
        else:
            audio_out = audiobusio.I2SOut(board.GPIO17, board.GPIO16, board.GPIO18)
    else:
        audio_out = None
except Exception as e:
    print("BLAD AUDIO: Nie wykryto I2S:", e)
    audio_out = None

_current_wave_file = None


def play(filename):
    global _current_wave_file

    if not audio_out:
        return

    try:
        if audio_out.playing:
            audio_out.stop()
        if _current_wave_file:
            _current_wave_file.close()
            _current_wave_file = None

        _current_wave_file = open(f"/sounds/{filename}", "rb")
        wave = audiocore.WaveFile(_current_wave_file)
        audio_out.play(wave)
    except Exception as e:
        print(f"Blad odtwarzania {filename}: {e}")
