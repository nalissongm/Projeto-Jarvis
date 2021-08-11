import speech_recognition as sr
import pyttsx3

import os
import datetime
import locale
import webbrowser

#classes
import core

# Reconhecedor de voz - Speech Recognition
r = sr.Recognizer()
m = sr.Microphone()

# Sintetizador de texto para audio
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty("rate", 190) # config velocity the voice
voices = engine.setProperty('voice', voices[2].id) # config voices => [0] Ana, [1] Heloisa, [2] Felipe, [3] Letícia

# Set activation keyword
# Define a palavra-chave de ativação
# Ok, google... Alexa... Siri... Cortana...

WAKE = "Jarvis" 

class  Jarvis:
    def __init__(self):
        self.r = sr.Recognizer
        self.m = sr.Microphone

    # Activate the microphone after confirmation keyword for initiate commands
    # Ativa o microfone depois da chave de ativação para iniciar os comandos
    def hear(self, r, m, response):
        try:
            with m as source:
                print("Waiting commad initial...")
                r.adjust_for_ambient_noise(source)
                r.dynamic_energy_threshold = 3000
                audio = r.listen(source, timeout=10)

                command = r.recognize_google(audio, language="pt-BR")
                return command.lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Houve um erro na rede.")
        except Exception as e:
            print(e)
            pass
    
    def  speak(self, text):
        # Create futurety two functions to set voice masculine or female
        engine.say(text)
        engine.runAndWait()
    
    def wishMe(self):
        locale.setlocale(locale.LC_ALL, 'pt-BR')
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<12:
            self.speak("Olá, senhor. Bom dia")
            print("Olá, senhor. Bom dia")
        elif hour>=12 and hour<18:
            self.speak("Olá, senhor. Boa tarde")
            print("Olá, senhor. Boa tarde")
        else:
            self.speak("Olá, senhor. Boa noite")
            print("Olá, senhor. Boa noite")

    def open_things(self, command):
        # Will need to expand on "open" commands
        if "youtube" in command:
            self.speak("O que deseja assistir hoje?")
            command = start.hear(r, m, response)  
            
            if "pesquise por" in command:
                command = command.replace('pesquise por','')
            elif "pesquise" in command:
                command = command.replace('pesquise','')
            else:
                command = command
            self.speak(f"Pesquisando por {command} no YouTube.")
            yt = webbrowser.open("https://www.youtube.com/results?search_query={}".format(command).replace(" ","+"),new=0)
            pass 

        elif "cifras" in command:
            self.speak("Abrindo o Cifras Club.")
            webbrowser.open("https://www.cifraclub.com.br/")
            pass

        elif "google" in command:
            self.speak("O que deseja pesquisar?")
            command = start.hear(r, m, response)
            if "pesquise por" in command:
                command = command.replace('pesquise por','')
            elif "pesquise" in command:
                command = command.replace('pesquise','')
            else:
                command = command
            webbrowser.open("https://www.google.com/search?q={}".format(command).encode("ascii","replace"))
            pass
        
        elif "documentos" in command:
            self.speak("Abrindo meus documentos.")
            os.startfile("C:/Users/nalisson/Documents")
            pass

        elif "pasta de downloads" in command:
            self.speak("Abrindo sua pasta de downloads.")
            os.startfile("C:/Users/nalisson/Downloads")
            pass

        else:
            self.speak("Ainda não aprendi a abrir isso. Me ensine.")
            pass
    
    def search(self,command):
        if 'youtube' in command:
            if "pesquise por" in command:
                command = command.replace('pesquise por','')
            else:
                command = command.replace('pesquise','')
            self.speak(f"Pesquisando por {command} no YouTube.")
            yt = webbrowser.open("https://www.youtube.com/results?search_query={}".format(command).replace(" ","+"),new=0)
            pass 
        else:
            if "pesquise por" in command:
                command = command.replace('pesquise por','')
            else:
                command = command.replace('pesquise','')
            self.speak(f"Pesquisando {command}...")
            webbrowser.open("https://www.google.com/search?q={}".format(command).encode("ascii","replace"))
            pass
        
    # The standard functions of the virtual assistant and main function to call other
    # As funções padrões do assistente virtual e principal função para charmar outras 
    def default_functions(self, command):
        try:
            if command.startswith('abra') or command.startswith('abrir'):
                self.open_things(command)
            elif command.startswith('pesquise') or command.startswith('pesquisar'):
                self.search(command)
            elif command == "quem é você":
                self.speak('Eu sou Jarvis. Eu sou um assistente virtual')
            elif "horas" in command:
                self.speak(core.SytemInfo.get_time())
            elif "data" in command:
                self.speak(core.SytemInfo.get_date())
            else:
                self.speak("Ainda não sei fazer isso.")
        except TypeError:
            print('Algum problema do tipo TypeError.')
            pass
        except AttributeError:
            print('Algum problema atributos.')
            pass
        except Exception as e:
            print(e)
            pass
    
    # Activate the microphone and valide keyword. If keyword == True (WAKE) => Start virtual assistant!
    # Ativa o microfone e valida a palavra-chave definida. Se a palavra-chave == Verdadeiro (WAKE) => Iniciar assistente virtual
    def listen(self, r, m):
        while True:
            try:
                with m as source:
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    r.dynamic_energy_threshold = 3000
                    audio = r.listen(source, timeout=5.0, phrase_time_limit=3.0)
                    response = r.recognize_google(audio, language="pt-BR")

                    if WAKE in response:
                        self.wishMe()
                        self.speak("Como posso ser útil?")
                        return response.lower()
                    else:
                        pass

            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Houve um erro na rede.")
            except Exception as e:
                print(e)
                pass

#Start class
start = Jarvis()
#previous_response = ""
if __name__=='__main__':
    while True:
        response = start.listen(r, m)
        command = start.hear(r, m, response)
        print(command)
        
        ''' 
        # Impede realização de comandos repetidos
        if command == previous_response:
            start.speak("Isso já foi perguntado. Se deseja perguntar novamente, repita isso de novo.")
            previous_response = ""
            response = start.listen(r, m)
            command = start.hear(r, m, response)
        '''
        start.default_functions(command)
        #previous_response = command
        print(command)
'''
else:
    print(__name__)

# Reconhecimento de fala Vosk
# Reconhecedor de voz OFFLINE - Vosk
# lib vosk
from vosk import Model, KaldiRecognizer

model = Model('model')
rec = KaldiRecognizer(model,16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=2048)
stream.start_stream()

# Loop do reconhecimento de fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            evaluate(text)
            print(text)
'''
