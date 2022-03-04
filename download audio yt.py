from pytube import YouTube

while True:
    video = input('Enter URL: ')
    yt = YouTube(video)
    vids = yt.streams.filter(only_audio=True)
    for i in range(len(vids)):
        print(i,'. ',vids[i])
    vnum = int(input("Choose one: "))
    vids[vnum].download()
    print('Done')
