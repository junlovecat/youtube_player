import urllib
import urllib.parse
import urllib.request
import os
import sys
from time import sleep
try:from tqdm import tqdm
except:
    os.system('pip install tqdm')
    from tqdm import tqdm
try:
    for u in tqdm(range(0,8)):
        x=int(u)
        if(x==0):import pygame
        elif(x==1):import playsound
        elif(x==2):import re
        elif(x==3):from pytube import YouTube
        elif(x==4):import pytube
        elif(x==5):from moviepy.editor import *
        elif(x==6):from pyfiglet import Figlet
        elif(x==7):import socket
        sleep(0.001)
except ModuleNotFoundError:
    os.system('pip install pygame')
    os.system('pip install playsound')
    os.system('pip install re')
    os.system('pip install pytube')
    os.system('pip install moviepy')
    os.system('pip install pyfiglet')
    os.system('pip install socket')
    import pygame
    import playsound
    import re
    from pytube import YouTube
    import pytube
    from moviepy.editor import *
    from pyfiglet import Figlet
    import socket
def play(name):
    pygame.init()
    isplaying=True
    screen = pygame.display.set_mode((250, 50))
    pygame.display.set_caption("highlight me")
    clock = pygame.time.Clock()
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1)
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    v = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(v+0.1)
                    print("volume up: ",v+0.1)
                if event.key == pygame.K_DOWN:
                    v = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(v-0.1)
                    print("volume down: ",v-0.1)
                if event.key == pygame.K_SPACE:
                    if(isplaying==True):
                        pygame.mixer.music.pause()
                        print("?????? ??????")
                        isplaying=False
                    elif(isplaying==False):
                        pygame.mixer.music.unpause()
                        print('?????? ??????')
                        isplaying=True
                if event.key == pygame.K_ESCAPE:
                    playing=False
                    pygame.quit()
                    return
        clock.tick(60)
def main():
    try:
        a=str(input('?????? ??????, ?????? ?????? exit??? ??????????????????: '))
        if(a.lower()=='exit'):sys.exit()
        if 'youtu.be' in a or 'youtube.com' in a:yt=pytube.YouTube(a)
        else:
            query_string = urllib.parse.urlencode({
                'search_query': a
            })
            try:htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
            except:
                print("???????????? ???????????? ???????????????.")
                sys.exit()
            search_results = re.findall( r"watch\?v=(\S{11})", htm_content.read().decode())
            try:link='https://youtu.be/'+search_results[0]
            except:
                print('????????? ????????? ????????????.')
                return
            yt=pytube.YouTube(link)
    except KeyboardInterrupt:
        print('\n???????????????.')
        sys.exit()
    try:
        print('downloading: '+yt.title)
        vid=yt.streams.get_highest_resolution()
        vid.download()
        print('downloaded: '+yt.title)
        ti=str(yt.title)
        lstriplist=['~','#','$','%','^','*','\\','|',';',"'",':','"',',','.','/','?']
        for i in tqdm(range(0,len(lstriplist))):
            ti=ti.replace(str(lstriplist[int(i)]),'')
            sleep(0.1)
        try:os.remove('song.mp3')
        except:pass
    except KeyboardInterrupt:
        print('?????? ???????????? ???????????????.')
        return
    except:
        ipaddress=socket.gethostbyname(socket.gethostname())
        if ipaddress=="127.0.0.1":
            print("???????????? ???????????? ???????????????.")
            sys.exit()
        print('?????? ?????? ?????? : ',Exception.with_traceback())
        sys.exit()
    video = VideoFileClip(os.path.join(ti+".mp4"))
    video.audio.write_audiofile(os.path.join("song.mp3"))
    print('now playing: '+ti)
    play(ti)
f = Figlet(font='slant')
print(f.renderText('pygameplayer'))
while(1):main()