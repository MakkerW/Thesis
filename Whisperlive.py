from whisper_live.client import TranscriptionClient

client = TranscriptionClient("localhost", 9090, lang="en", model="small")
client("Test.mp3")  # Replace with your audio file path
