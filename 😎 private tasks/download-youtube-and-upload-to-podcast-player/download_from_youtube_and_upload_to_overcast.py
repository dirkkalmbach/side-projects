#%%
# Import Libraries
from pytube import YouTube
import os

# 👇🏻 C H A N G E 👇🏻
SAVE_PATH_FOLDER = "/Users/dirkkalmbach/Downloads" # <- folder
# 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻

# download
print("downloading from youtube ...")
video_url = "https://www.youtube.com/watch?v=_UxECPYSWVs"
yt = YouTube(video_url)
t=yt.streams.filter(only_audio=True)
path = t[0].download(SAVE_PATH_FOLDER)

# change file extension mp4 -> mp3
try:
    os.rename(path, path[:-3]+".mp3")
except:
    print("Error: could not change file ending to .mp3")

# %%
