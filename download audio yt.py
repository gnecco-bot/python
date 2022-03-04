from pytube import YouTube

while True:
    video = input('Enter URL: ') # youtube link
    yt = YouTube(video)
    vids = yt.streams.filter(only_audio=True)
    for i in range(len(vids)):
        print(i,'. ',vids[i])
    vnum = int(input("Choose one: ")) # 1 or 4 
    vids[vnum].download() # (r'C:\users\user\downloads')
    print('Done')

# test with - www.youtube.com/watch?v=hTWKbfoikeg
