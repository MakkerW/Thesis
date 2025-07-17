# Assessing the Reliability of Live Audio Transcriptions in Financial Decision-Making

This repository contains the code and materials for my master's thesis at DTU, done in collaboration with Alipes Capital. The thesis investigates how accurately modern speech-to-text models can transcribe company earnings calls in real time, with a focus on their suitability for financial decision-making.

Three models were evaluated:
- Whisper-small (via FasterWhisper)
- Whisper-large-v3 Turbo (via TensorRT-LLM)
- GPT-4o Mini Transcribe (OpenAI)

The transcriptions were benchmarked using WER, MER, and WIL, as well as custom analysis of numeric accuracy. The study also explores how model performance is affected by speaker accents, timing within calls, and Q&A segments.

Results show that open-source models like Whisper-Turbo can approach the accuracy of proprietary systems, but all models still exhibit issues with numeric reliability and spontaneous speech. The findings highlight both the promise and limitations of using ASR for real-time financial applications.

📄 The full thesis is included in this repository as `thesis.pdf`.
