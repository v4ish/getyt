from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("VIDEO DOWNLOADER")
print("_____________________")
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length : ",yt.length,"seconds")

'''
qty
_________________
[18]  360p 30fps
[22]  720p 30fps 
[137] 1080p 30fps no audio
'''

qty = 22
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