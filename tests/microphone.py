# Testes de reconhecimento de voz para ativar por keyword dentre outros testes

# Sintetizador de texto
import time
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()


#Conficuração das vozes => [0] Ana, [1] Heloisa, [2] Felipe, [3] Letícia

class PropertyVoice:
    def __init__(self):
        pass

    def get_voice(define):
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

    def set_voice(voice):
        if voice == 'standard':
            i = 3
        else:
            i = voice
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[i].id)
    
    def speak(text):
        engine.say(text)
        engine.runAndWait()

'''asnwer = input('Deseja configurar a voz? \n digite S ou N: ')
if asnwer == 'S' or asnwer == 'Sim' or asnwer == 's':
    asnwer = input('Qual será a voz de sua preferência? \n F => femine or M => masculine: ')
    if asnwer == 'F' or asnwer == 'f':
        define = 'feminino'
        voice_config = PropertyVoice
        voice = voice_config.get_voice(define)
        voice_config.set_voice(voice)
    elif asnwer == 'M' or asnwer == 'm':
        define = 'masculino'
        voice_config = PropertyVoice
        voice = voice_config.get_voice(define)
        voice_config.set_voice(voice)
    else:
        define = 'standard'
        voice_config = PropertyVoice
        voice = voice_config.get_voice(define)
        voice_config.set_voice(voice)
elif asnwer == 'N' or asnwer == 'Não':
    define = 'standard'
    voice_config = PropertyVoice
    voice = voice_config.get_voice(define)
    voice_config.set_voice(voice)'''
    

def speak(text):
    PropertyVoice.set_voice("standard")
    PropertyVoice.speak(text)

print('Iniciando sua inteligência artificial - Jarvis...')

def talk_command():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        print('Escutando...')
        audio = r.listen(source,timeout=15,phrase_time_limit=3)

    try:
        query = r.recognize_google(audio,language="pt-BR")
        print(f'Você disse: {query}\n')
    except sr.UnknownValueError:
        print("Me desculpe, mas não entendi oque disse.")
    except Exception as e:
        query = "None"
    return query

def wishMe():
    import datetime
    import locale

    locale.setlocale(locale.LC_ALL, 'pt-BR')

    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Olá, senhor. Bom dia")
        print("Olá, senhor. Bom dia")
    elif hour>=12 and hour<18:
        speak("Olá, senhor. Boa tarde")
        print("Olá, senhor. Boa tarde")
    else:
        speak("Olá, senhor. Boa noite")
        print("Olá, senhor. Boa noite")

speak('Iniciando sua inteligência artificial - Jarvis...')
wishMe()

while True:
    init_jarvis = talk_command()
    print(init_jarvis)

    if init_jarvis == 'Olá, Jarvis' or init_jarvis == 'Olá Jarvis' or init_jarvis == 'Olá, jarvis' or init_jarvis == 'olá, Jarvis' or init_jarvis == 'olá, jarvis' or init_jarvis == 'olá Jarvis' or init_jarvis == 'olá jarvis':
        speak('Olá, Senhor. Como posso ajuda-lo?')
        query = None
        n = True
        while n == True:
            def talk_command2():
                r = sr.Recognizer()
                m = sr.Microphone()
                with m as source:
                    print('Escutando...')
                    audio = r.listen(source,timeout=15)

                try:
                    query = r.recognize_sphinx(audio,language="pt-BR")
                    print(f'Você disse: {query}\n')
                except sr.UnknownValueError:
                    print("Me desculpe, mas não entendi oque disse.")
                except Exception as e:
                    query = "None"
                return query
                
            text = talk_command2().lower()

            if text == 0:
                continue 
            elif text == "None" or text == None:
                print('Cancelando captura de som')

'''
Código Antigo

# Reconhecimento de fala Vosk
# Reconhecedor de voz OFFLINE - Vosk
# lib vosk
from vosk import Model, KaldiRecognizer

# lib pyaudio necessario para vosk
import pyaudio

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
'''
Funções utilizando classificação de texto

def speak(text):
    #Falar texto
    engine.say(text)
    engine.runAndWait()

def evaluate(text):
    entity = classify(text)

    # interação
    if entity == 'salutation|getSalutation':
        speak(core.SytemInfo.get_salutation())
    if entity == 'interaction|getInteraction':
        speak("Eu estou bem. Como o senhor está?")
    if entity == 'salutation|getSalutationGoodMorning':
        speak("Bom dia, senhor. Oque planejou para hoje?")
    if entity == 'salutation|getSalutationGoodAfternoon':
        speak("Bom tarde, senhor. Há algo em que posso ajudar?")
    if entity == "salutation|getSalutationGoodNitght":
        speak("Boa noite, senhor. Está tendo um dia agradável?")
    # datetime info
    elif entity == 'time|getTime':
        speak(core.SytemInfo.get_time())
    elif entity == 'time|getDate':
        speak(core.SytemInfo.get_date())
    # open program
    elif entity == 'open|notepad':
        speak("Abrindo o bloco de notas. Por favor aguarde um instante.")
        os.system('notepad.exe')
    elif entity == 'open|browser':
        speak("Abrindo o navegador. Por favor aguarde um instante.")
        os.system('"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"')
    # close program
    elif entity == 'close|notepad':
        speak("Fechando o bloco de notas.")
        os.system("TASKKILL /F /IM notepad.exe")
    elif entity == 'close|browser':
        speak("Fechando o navegador.")
        os.system('"TASKKILL /F /IM C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"')
    else:
        pass


    print('Text: {} Entity: {}'.format(text, entity))
'''



