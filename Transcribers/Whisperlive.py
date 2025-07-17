import os
from whisper_live.client import TranscriptionClient
import time

# Base folder containing MP3 files
base_folder = "/work3/s233593/combined_22/"
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define range of folder names (as strings or ints depending on your folder naming)
start_id = 4449269
end_id = 4449269

for root, dirs, files in os.walk(base_folder):
    depth = os.path.relpath(root, base_folder).count(os.sep)
    dirs[:] = [d for d in dirs if d != "CEO"]
    if depth > 1:
        continue
    dirs.sort()
    files.sort()

    folder_name = os.path.basename(root)
    try:
        folder_id = int(folder_name)
    except ValueError:
        continue  # skip folders that don't have numeric names

    if not (start_id <= folder_id <= end_id):
        continue

    print(f"Processing folder {root}", flush=True)

    for file in files:
        if file.endswith(".mp3"):
            mp3_path = os.path.join(root, file)
            txt_path = os.path.splitext(mp3_path)[0] + "_Whisper.txt"

            print(f" Transcribing: {mp3_path}", flush=True)

            client = TranscriptionClient("localhost", 9090, lang="en", model="small", max_connection_time=7200)
            transcription = client(mp3_path)

            print("Waiting for transcription to complete...", flush=True)
            time.sleep(35)

            transcription_text = "\n".join(seg["text"] for seg in client.client.transcript)

            with open(txt_path, "w") as output_file:
                output_file.write(transcription_text)

            print(f" Transcription saved: {txt_path}", flush=True)

            file_nomp3 = os.path.splitext(file)[0]
            resampled_path = os.path.join(script_directory, file_nomp3 + "_resampled.wav")
            print("resampled_path: ", resampled_path)

            if os.path.exists(resampled_path):
                os.remove(resampled_path)
                print(f" Removed resampled file: {resampled_path}", flush=True)

            client.client.close_websocket()
            del client

            time.sleep(5)

print(" All files processed!", flush=True)
