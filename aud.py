from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("AUDIO DOWNLOADER")
print("_____________________")
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length : ",yt.length,"seconds")

'''
qty
_________________
[140] mp4 128kbps
[251] webm 160kbps
'''

qty = 251
print("Size: ", yt.streams.get_by_itag(qty).filesize_mb, "MB")

num = int(input("Enter 1 to continue: "))

if num == 1:
    yd = yt.streams.get_by_itag(qty)

#Download folder "/Users/Name/Downloads"
    yd.download("")
    print("Downloading...")

else:
    print("Exiting...")
    exit