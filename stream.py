import numpy as np
import sounddevice as sd
from piper.voice import PiperVoice

model = "./k9_2449_model.onnx"
voice = PiperVoice.load(model)
text = "What is your question? I am a very clever robot! This will start speaking befor everything has been put through the text to speech engine."

# Setup a sounddevice OutputStream with appropriate parameters
# The sample rate and channels should match the properties of the PCM data
stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
stream.start()

for audio_bytes in voice.synthesize_stream_raw(text):
    int_data = np.frombuffer(audio_bytes, dtype=np.int16)
    stream.write(int_data)

stream.stop()
stream.close()

