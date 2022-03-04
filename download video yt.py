from pytube import YouTube

while True:
    link = input('Enter URL:')
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()
    
# teste with - www.youtube.com/watch?v=gL1pv6vt9Ig
