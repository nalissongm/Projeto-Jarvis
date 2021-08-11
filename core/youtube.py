import urllib.request
import requests
from bs4 import BeautifulSoup as bSoup
import re
import webbrowser


class Youtube:
    def __init__(self):
        pass

    def search(self,command):
        video = command
        req = urllib.request.Request("https://www.youtube.com/results?search_query={}".format(video).replace(" ","+"))
        answer = urllib.request.urlopen(req).read().decode('utf-8')
        html = re.findall(r"watch\?v=(\S{11})", answer)

        i=0
        search_yt = []
        while i<10:
            search_yt.insert(i,f'https://www.youtube.com/watch?v={html[i]}')
            i+=1
        
        return search_yt
    
    def info_video(self,buscar):
        i=0
        info_title = []
        info_uploader = []
        info_video = []
        for y in buscar:
            req = requests.get(buscar[i])
            pagesoup = bSoup(req.text,'html.parser')

            html2 = pagesoup.find_all('meta',{'name': 'title'})
            html3 = pagesoup.find_all('link',{'itemprop': 'name'})

            title =html2[0]['content']
            uploader =html3[0]['content']

            info_title.insert(i, title)
            info_uploader.insert(i,uploader)
            i+=1
        
        i=0
        for y in buscar:
            info_video.append(info_title[i] +' no canal '+ info_uploader[i])
            i+=1
            
        if 'título' in options:
            return info_title
        elif 'canal' in options:
            return info_uploader
        else:
            return info_video

    def get_info(self,buscar,opition='None'):
        if opition != 'título' or opition != 'canal':
            options = ''
        result_search = self.info_video(buscar, opition)
        #print(result_search)

        count = 0
        for i in result_search:
            print(result_search[count])
            count+=1

            
    def playlist():
        pass

    def playvd(self, command):
        if 'pesquise' in command:
            if "pesquise por" in command:
                command = command.replace('pesquise por','')
            else:
                command = command.replace('pesquise','')
            talk.speak(f"Pesquisando {command} no youtube...")
            yt = webbrowser.open("https://www.youtube.com/results?search_query={}".format(command).replace(" ","+"),)

        
            
        
yt = Youtube()
talk = SpeekJarvis()
command = input("Digite alguma pesquisa: ")
#buscar = yt.search(command)
#print(buscar)
info = yt.playvd(command)
#print(info[0])