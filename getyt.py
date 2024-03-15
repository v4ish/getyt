import time
import pyfiglet
from pytube import YouTube
from pypresence import Presence


client_id = '1217755350795550740'
RPC = Presence(client_id)
RPC.connect()

RPC.update(
            details="Scrapping youtube",
            state="Downloading something...",
            large_image="logo",
            large_text="getyt",
            ) 


#ASCI ART
ASCII_art_1 = pyfiglet.figlet_format("getyt")
print(ASCII_art_1)
#Choice
print("1 - 160kbps Audio Downloader")
print("2 - 720p Video Downloader")
print("3 - 1080p Audio & Video Downloader")
print("99 - ffmpeg Merging")
print(" ")

choice = int(input("Choose an option: "))
print(" ")

link = (input("Paste the link here: "))
yt = YouTube(link)

#Functions

def header():
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print("Length : ",yt.length,"seconds")
    time.sleep(1)
    print("Downloading...")
    exit

#AUDIO DOWNLOADER
def audio():
    print("Getting 160kbps Audio Information...")
    print("_______________________________")
    qty = 251
    header()
    yd = yt.streams.get_by_itag(qty)
    yd.download("./Audio/160kbps/")
    print("Exiting...")
    exit
    
#VIDEO DOWNLOADER
def video():
    print("Getting 720p Video Information...")
    print("_______________________________")
    qty = 22
    header()
    yd = yt.streams.get_by_itag(qty)
    yd.download("./Video/720p/")
    print("Exiting...")
    exit

#1080P Video Downloader
def video1080p():
    print("Getting 1080p Video Information...")
    print("_______________________________")
    qty = 137 #Video
    qty2 = 251 #Audio
    header()
    yd = yt.streams.get_by_itag(qty)
    yd.download("./Video/1080p/" + yt.title)
    time.sleep(3)
    yd = yt.streams.get_by_itag(qty2)
    yd.download("./Video/1080p/" + yt.title)
    print("_______________________________")
    print("Use ffmpegy.py to Merge audio and video together")
    print("Exiting...")
    exit

#If else input
if choice == 1:
        audio()
elif choice == 2:
        video()
elif choice == 3:
        video1080p()

else:
     print("Wrong input Exiting...")

#TODO: Merge audio and video using ffmpeg

'''
qty - Audio
_________________
[140] mp4 128kbps
[251] webm 160kbps

qty - Video
_________________
[18]  360p 30fps
[22]  720p 30fps 
[137] 1080p 30fps no audio
'''



