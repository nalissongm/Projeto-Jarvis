import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Trazer informações youtube
import urllib.request
from bs4.element import Comment
import requests
from bs4 import BeautifulSoup as bSoup
import re
import pywhatkit
#import time



# Reconhecedor de voz - Speech Recognition
r = sr.Recognizer()
m = sr.Microphone()


# Sintetizador de texto para audio
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 190)
voices = engine.setProperty('voice', voices[3].id)

'''def voice_Property(model_voice):
    if model_voice == "":
        i = 2
    elif model_voice == 2 or model_voices == 'dois' or model_voices == "2":
        i = 2
    elif model_voice == 3 or model_voices == 'três' or model_voices == "3":
        i = 3
    
'''
WAKE = "Jarvis"



class  Jarvis:
    def __init__(self):
        self.r = sr.Recognizer
        self.m = sr.Microphone

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

    '''
    def PropertyVoice(self, model_voice):
        self.speak("Configurar voz do sistema...")
        self.speak("Para definir voz feminina, diga feminina. Para definir voz masculina, diga masculina.")
        voices_config = self.hear(r,m, response)
        try: 
            if voices_config == "feminina" or voices_config == "feminino" or voices_config == "mulher":
                model_voice = 3
                return model_voice
            elif voices_config == "masculino" or voices_config == "masculina" or voices_config == "homem":
                model_voice = 2
                return model_voice
            else:
                pass
        except:
            self.speak("Voz padrão foi definida.")
            model_voice = 2
            return model_voice
    '''    
    def open_things(self, command):
        # Will need to expand on "open" commands
        if "youtube" in command:
            self.speak("O que deseja assistir hoje?")
            command = init.hear(r, m, response)
            self.speak("Deseja que eu liste os cinco primeiros resultados?")
            option = init.hear(r, m, response)   
            if 'listar' in option or 'sim' in option in 'liste' in option:
                req = urllib.request.Request("https://www.youtube.com/results?search_query={}".format(command).replace(" ","+"))
                answer = urllib.request.urlopen(req)
                html = answer.read().decode('utf-8')

                video_ids = re.findall(r"watch\?v=(\S{11})", html)

                i=0
                while i<5:
                    quest = requests.get(f'https://www.youtube.com/watch?v={video_ids[i]}')

                    pagesoup = bSoup(quest.text,'html.parser')

                    html2 = pagesoup.find_all('meta',{'name': 'title'})
                    html3 = pagesoup.find_all('link',{'itemprop': 'name'})

                    title =html2[0]['content']
                    uploader =html3[0]['content']

                    self.speak(f'{i+1} {title} no canal {uploader}')
                    i+=1

                option = init.hear(r, m, response)
                try:
                    if 'primeiro' in option:
                        url = video_ids[0]
                        self.speak("Abrindo video no youtube.")
                        yt = pywhatkit.playonyt(f'https://www.youtube.com/watch?v={url}')
                    if 'segundo' in option:
                        url = video_ids[1]
                        self.speak("Abrindo video no youtube.")
                        yt = pywhatkit.playonyt(f'https://www.youtube.com/watch?v={url}')
                    if 'terceiro' in option:
                        url = video_ids[2]
                        self.speak("Abrindo video no youtube.")
                        yt = pywhatkit.playonyt(f'https://www.youtube.com/watch?v={url}')
                    if 'quarto' in option:
                        url = video_ids[3]
                        self.speak("Abrindo video no youtube.")
                        yt = pywhatkit.playonyt(f'https://www.youtube.com/watch?v={url}')
                    if 'quinto' in option:
                        url = video_ids[4]
                        self.speak("Abrindo vídeo no youtube.")
                        yt = pywhatkit.playonyt(f'https://www.youtube.com/watch?v={url}')
                except Exception as e:
                    self.speak("Houve um erro ao executar. Abrindo o youtube.")
                    webbrowser.open("https://www.youtube.com")        
                    pass
            elif 'cancelar' in option or 'parar' in option in '' in option:
                pass
            else:
                self.speak("Abrindo vídeo no youtube.")
                yt = pywhatkit.playonyt("https://www.youtube.com/results?search_query={}".format(command).replace(" ","+"),)
                pass 

        elif "facebook" in command:
            self.speak("Abrindo o Facebook.")
            webbrowser.open("https://www.facebook.com")
            pass

        elif "google" in command:
            self.speak("O que deseja pesquisar?")
            command = init.hear(r, m, response)
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
            self.speak("Abrindo video no youtube.")
            yt = pywhatkit.playonyt("https://www.youtube.com/results?search_query={}".format(command).replace(" ","+"),)
            pass
        else:
            if "pesquise por" in command:
                command = command.replace('pesquise por','')
            else:
                command = command.replace('pesquise','')
            self.speak(f"Pesquisando {command}...")
            webbrowser.open("https://www.google.com/search?q={}".format(command).encode("ascii","replace"))
            pass

    def default_functions(self, command):
        try:
            if command.startswith('abra') or command.startswith('abrir'):
                self.open_things(command)
            elif command.startswith('pesquise') or command.startswith('pesquisar'):
                self.search(command)
            elif command == "quem é você":
                self.speak('Eu sou Jarvis. Eu sou um assistente virtual')
            else:
                self.speak("Ainda não aprendi isso.")
        except TypeError:
            print('Algum problema do tipo TypeError.')
            pass
        except AttributeError as a:
            print(a)
            pass
        except Exception as e:
            print(e)
            pass

    def listen(self, r, m):
        while True:
            try:
                with m as source:
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    r.dynamic_energy_threshold = 3000
                    audio = r.listen(source, timeout=10.0)
                    response = r.recognize_google(audio, language="pt-BR")

                    if WAKE in response:
                        self.speak("Olá senhor como posso ser útil?")
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

init = Jarvis()
previous_response = ""
#model_voice = ""

if __name__=='__main__':
    
    while True:
        #voice_Property(model_voice)
        response = init.listen(r, m)
        command = init.hear(r, m, response)

        #if command == "configurar voz" or command == "configuração de voz" or command == "alterar voz" or command == "mudar voz":
            #init.PropertyVoice(model_voice)
        #else:
            

        if command == previous_response:
            init.speak("Isso já foi perguntado. Se deseja perguntar novamente, repita isso de novo.")
            previous_command = ""
            response = init.listen(r, m)
            command = init.hear(r, m, response)
        init.default_functions(command)
        previous_response = command
        print(command)

'''def call_jarvis():
    while True: 
        print('listening...')
        init_jarvis = active_mic()

        if init_jarvis == 'Olá, Jarvis' or init_jarvis == 'Olá Jarvis' or init_jarvis == 'Olá, jarvis' or init_jarvis == 'olá, Jarvis' or init_jarvis == 'olá, jarvis' or init_jarvis == 'olá Jarvis' or init_jarvis == 'olá jarvis':
            print('INIT COMAND..')
            break

while True:
    call_jarvis()
    print('Olá senhor. Em que posso ser útil?')
    commad = active_mic()

'''
'''
if __name__=='__main__':
    print(__name__)
else:
    print(__name__)
'''