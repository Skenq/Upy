from pytube import YouTube

lien = 'https://www.youtube.com/watch?v=khyfYITIhV0'

video=YouTube(lien)
print ("Now Loading")
streams = video.streams.filter(progressive=True)
print (streams[0])
streams[0].download("Vids")
print ("Completed")