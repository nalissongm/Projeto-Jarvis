import pyttsx3


class SpeekJarvis:
    engine = pyttsx3.init()

    def __init__(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty("rate", 190)
        voices = engine.setProperty('voice', voices[3].id)
        pass

    def get_voice(self, define):
        voice_model = define
        if 'feminino' in voice_model:
            voice = 3
            return voice
        elif 'masculino' in voice_model:
            voice = 2
            return voice
        else:
            voice = 'standard'
            return voice

    def set_voice(self,voice):
        if voice == 'standard':
            i = 3
        else:
            i = voice
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[i].id)
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

talk = SpeekJarvis()
talk.speak("Oi, meu nome é Jarvis")

__name__ = __package__
    
if __name__=='__main__':
    print(__name__)
else:
    print(__name__)
        