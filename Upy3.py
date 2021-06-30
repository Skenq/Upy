from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=khyfYITIhV0').streams.first().download("vids")
print ("Done")