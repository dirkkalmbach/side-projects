#%%
# Import Libraries
from pytube import YouTube
import os
import argparse


# 👇🏻 C H A N G E 👇🏻
SAVE_PATH_FOLDER = "/Users/dirkkalmbach/Downloads" # <- folder
# 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="url of youtube video")
args = vars(ap.parse_args())

# download
video_url = args["name"]#"https://www.youtube.com/watch?v=_UxECPYSWVs"
print("downloading from youtube ...")
yt = YouTube(video_url)
t=yt.streams.filter(only_audio=True)
path = t[0].download(SAVE_PATH_FOLDER)

# change file extension mp4 -> mp3
try:
    os.rename(path, path[:-3]+".mp3")
except:
    print("Error: could not change file ending to .mp3")

# %%
