from sys import argv
import time
import pyfiglet
from pytube import YouTube

#ASCI ART
ASCII_art_1 = pyfiglet.figlet_format("YT Downloader")
print(ASCII_art_1)

link = (input("Paste the link here: "))

print("1 - Audio Downloader")
print("2 - Video Downloader")

choice = int(input("Choose the Downloader: "))
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
    print("Getting Audio Information...")
    print("_______________________________")
    qty = 251
    header()
    yd = yt.streams.get_by_itag(qty)
    yd.download("")
    exit
    
#VIDEO DOWNLOADER
def video():
    print("Getting Video Information...")
    print("_______________________________")
    qty = 22
    header()
    yd = yt.streams.get_by_itag(qty)
    yd.download("")
    exit

if choice == 1:
        audio()
elif choice == 2:
        video()
else:
     print("Wrong input Exiting...")
     exit

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



