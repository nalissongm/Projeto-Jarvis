import datetime
import locale
import os

locale.setlocale(locale.LC_ALL, 'pt-BR')

class SytemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São exatamente {} horas e {} minutos.'.format(now.hour, now.minute)
        return answer

    @staticmethod
    def get_date():
        #loc = locale.getlocale()
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} de {} de {}.'.format(now.day,now.strftime("%B"),now.year)
        return answer

    @staticmethod
    def open_things(entity):
        if entity == "open|notepad":
            os.system('notepad.exe')
        else:
            pass

            
        
        