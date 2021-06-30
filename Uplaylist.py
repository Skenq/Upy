from pytube import Playlist

p = Playlist(input("Enter Youtube Playlist : "))
for video in p.videos:
    video.streams.first().download("Vids")
    for url in p.video_urls[:1]:
        print (url)