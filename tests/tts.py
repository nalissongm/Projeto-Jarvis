'''import pyttsx3

#engine = pyttsx3.init()

#Conficuração das vozes
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[2].id)

engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[3].id)

#Falar texto
engine.say('Olá meu nome é Jarvis. Sou uma inteligência artificial')
engine.runAndWait()
#print(voices)

#Printa na tela todas as vozes disponíveis'''
'''for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")'''

