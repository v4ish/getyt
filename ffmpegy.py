import ffmpeg
import subprocess 
from sys import argv

'''
def ffmpegy():      
    input_video = ffmpeg.input('./Video/1080p/v1.webm')
    choice = int(input("Choose an option: "))

    input_audio = ffmpeg.input('./Video/1080p/a1.webm')

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./Video/1080p/Merged/Merged.mp4').run()
'''
def ffmpegy():
    videofile = str(input("Enter the Video file name with location: "))   
    audiofile = str(input("Enter the Audio file name with location: "))   
    outputfile = "output.mp4"
    codec = "copy"
    subprocess.run(f"ffmpeg -i {videofile} -i {audiofile} -c {codec} {outputfile}")

ffmpegy()