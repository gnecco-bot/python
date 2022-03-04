from pytube import YouTube

while True:
    link = input('Enter URL:') # youtube link
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download() # (r'C:\users\user\downloads')
    
# test with - www.youtube.com/watch?v=gL1pv6vt9Ig
