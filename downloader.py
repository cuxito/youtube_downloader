# Import the necessary modules
from pytube import YouTube

# Define the URL of the video to be downloaded
video_url = input("Enter the URL of the YouTube video you want to download: ")

# Create a YouTube object with the given video URL
try:
    yt = YouTube(video_url)
except Exception as e:
    print('Error encountered while fetching details about your video', str(e))
    exit()

# Get information about the audio and video streams available for the video
streams = yt.streams

# Select the best quality stream
best = streams.get_by_itag('22')  # For example, this is the highest resolution stream which is in mp4 format for the given video. You can change it according to your need.

# Download the selected stream
print('Downloading your video...')
best.download('/path/to/save/your/video')  # Specify the path where you want to save the downloaded video.

print('Video download complete! Enjoy watching!')
