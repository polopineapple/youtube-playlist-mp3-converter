from pytube import YouTube
from pytube import Playlist
import os 
import re 
import moviepy.editor as mp
import pydub
from pydub import AudioSegment
import ffmpy

#paste the link of your playlist here
link = "https://www.youtube.com/playlist?list=OLAK5uy_m8bI8VFOOsnLNNMWEVdR5Ww9jhzf145Co"

#paste the path of the folder you want to save the mp3 in here 
folder_path = '/Users/user/Desktop/music'


#video length double when converting from mp4 to mp3, this function helps fix it 
def fix_duration(filepath):
    ##  Create a temporary name for the current file.
    ##  i.e: 'sound.mp3' -> 'sound_temp.mp3' 
    temp_filepath = filepath[ :len(filepath) - len('.mp3')] + '_temp' + '.mp3'

    ##  Rename the file to the temporary name.
    os.rename(filepath, temp_filepath)

    ##  Run the ffmpeg command to copy this file.
    ##  This fixes the duration and creates a new file with the original name.
    command = 'ffmpeg -v quiet -i "' + temp_filepath + '" -acodec copy "' + filepath + '"'
    os.system(command)

    ##  Remove the temporary file that had the wrong duration in its metadata.
    os.remove(temp_filepath)

playlist = Playlist(link)

#this download the mp4 to the folder 
for url in playlist:
   print(YouTube(url).streams.first()
   .download(folder_path))

#this convert them to mp3 and delete the mp4 files 
for file in os.listdir(folder_path):
  if re.search('mp4', file):
    mp4_path = os.path.join(folder,file)
    mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
    AudioSegment.from_file(mp4_path).export(mp3_path, format="mp3")
    fix_duration(mp3_path)
    os.remove(mp4_path)

