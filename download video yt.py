from pytube import YouTube

while True:
    link = input('Enter URL:')
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()