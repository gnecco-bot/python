from pytube import YouTube

while True:
    video = input('Enter URL: ')
    yt = YouTube(video)
    vids = yt.streams.filter(only_audio=True)
    for i in range(len(vids)):
        print(i,'. ',vids[i])
    vnum = int(input("Choose one: ")) # 1 or 4 
    vids[vnum].download() # (r'C:\users\user\download')
    print('Done')

# teste with - www.youtube.com/watch?v=hTWKbfoikeg
    
