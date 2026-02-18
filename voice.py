# Prosty moduł głosu
# Pełna implementacja zmiany głosu na RP2040 w Pythonie jest trudna (opóźnienia).
# To jest szkielet, który pozwala kodowi działać.

class VoiceChanger:
    def __init__(self, audio_output):
        self.audio_out = audio_output
        self.active = False
        print("MODUŁ GŁOSU: Zainicjowano (Tryb Standby)")

    def activate(self):
        if not self.active:
            self.active = True
            # Tutaj w przyszłości kod włączający mikrofon

    def deactivate(self):
        if self.active:
            self.active = False

    def update(self):
        pass # Tutaj przetwarzanie audio w czasie rzeczywistym