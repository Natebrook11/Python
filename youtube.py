import pytube
link = input("Youtube video link:")
yt = pytube.YouTube(link)
print("Title:", yt.title)
print("Author:", yt.author)
print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
print("Number of views:", yt.views)
length = yt.length / 60
print("Length of video:", length, "mins")
yt.streams.get_highest_resolution().download()
print("Video successfullly downloaded from", link)