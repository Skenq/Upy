# First Project 24/06/2021 By Hichem
import pytube
def U2():

    vid_url=str(input("URL: "))
    
    print('In Progress...')
    video=pytube.YouTube(vid_url)
    Streams=video.streams
    Filter=Streams.get_highest_resolution()
    
    print('Now downloading:',video.title)
    Filter.download("Vids")
    
    print('Done!')
U2()