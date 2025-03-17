import os
from whisper_live.client import TranscriptionClient
import time

# Base folder containing MP3 files
base_folder = "Data/revdotcom/combined_21"

for root, dirs, files in os.walk(base_folder):
    dirs.sort()  # Ensure folders are processed alphabetically
    files.sort()  # Ensure files are processed alphabetically

    print(f"Processing folder {root}", flush=True)

    for file in files:
        if file.endswith(".mp3"):
            mp3_path = os.path.join(root, file)

            # Change the file name to include "_Whisper"
            txt_path = os.path.splitext(mp3_path)[0] + "_Whisper.txt"

            print(f" Transcribing: {mp3_path}", flush=True)

            #  Create a NEW client for each file
            client = TranscriptionClient("localhost", 9090, lang="en", model="small")

            transcription = client(mp3_path)
            transcription_text = "\n".join(seg["text"] for seg in client.client.transcript)

            with open(txt_path, "w") as output_file:
                output_file.write(transcription_text)

            print(f" Transcription saved: {txt_path}", flush=True)

            # Close the WebSocket and destroy the client
            client.client.close_websocket()
            del client  #Force Python to delete the client object

            time.sleep(5)

print(" All files processed!", flush=True)
