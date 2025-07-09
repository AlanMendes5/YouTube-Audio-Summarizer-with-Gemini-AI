import sys
import string
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import VideoUnavailable, RegexMatchError
import google.generativeai as genai

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

#Download video from YT
url = input("Provide a youtube video URL: ")

try:
    yt = YouTube(url, on_progress_callback=on_progress)
except (VideoUnavailable, RegexMatchError):
    print("MOST PROVIDE A VALID URL.")
    sys.exit(1)

#.downloads() return a path of the content saved.
file_path = yt.streams.get_audio_only().download(output_path=r"YOUR_PATH_HERE")

# transcript - resume
genai.configure(api_key="YOUR_API_KEY_HERE")
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

prompt = f"""
Your task is to create a summary of the text provided below.
Format the document in Markdown style.
"""

audio_file = genai.upload_file(file_path) #Upload file method.
response = model_gemini.generate_content([prompt, audio_file])

#Store the resume like a md file
file_name = remove_punctuation(yt.title)
destination = fr"YOUR_PATH_HERE{file_name}.md"
with open(destination, "w+") as f:
    f.write(response.text)

