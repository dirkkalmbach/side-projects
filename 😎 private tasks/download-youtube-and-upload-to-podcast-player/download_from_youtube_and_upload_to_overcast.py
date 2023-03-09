#%%
# Import Libraries
from pytube import YouTube


# 👇🏻 C H A N G E 👇🏻
SAVE_PATH_FOLDER = "/Users/dirkkalmbach/Downloads" # <- folder
# 👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻👆🏻

yt = YouTube(video_url)
t=yt.streams.filter(only_audio=True)

t[0].download(SAVE_PATH_FOLDER)