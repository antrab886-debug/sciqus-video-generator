from moviepy.editor import *
from gtts import gTTS

# Read script
with open("script.txt", "r") as f:
    script = f.read()

# Convert text to speech
tts = gTTS(text=script, lang="en")
tts.save("voiceover.mp3")

# Load voice audio
voice = AudioFileClip("voiceover.mp3")

# Create simple black background video
video = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=voice.duration)
video = video.set_audio(voice)

# Export final video
video.write_videofile("sciqus_video.mp4", fps=24)
