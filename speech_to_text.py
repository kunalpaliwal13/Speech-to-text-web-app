import assemblyai as aai

# set the API key
aai.settings.api_key = "d@@#16#####f"
transcriber = aai.Transcriber()


transcript = transcriber.transcribe("/content/sample-1.mp3")
print(transcript.text)

transcript.audio_duration

for sentence in transcript.get_sentences():
print(sentence.text)



