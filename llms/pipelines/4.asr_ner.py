
import os
import warnings

# TensorFlow C++ logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# oneDNN message
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

#  Python warnings (including deprecation)
warnings.filterwarnings("ignore")

import tensorflow as tf
tf.get_logger().setLevel("ERROR")


from transformers import pipeline, logging
logging.set_verbosity_error()

# Load the pipeline with the Whisper model
asr = pipeline("automatic-speech-recognition",  model="openai/whisper-base.en")

# Path to your audio file (.wav or .mp3)
audio_path = "./pipelines/mlk_speech.mp3"

# Transcribe the audio
result = asr(audio_path, return_timestamps=True)
#print(result)

context = result["text"]

ner = pipeline("ner", model="dslim/bert-base-NER")

entities = ner(context)

# Display results
print("\nEntities\n")
for entity in entities:
    print(f"{entity['word']} - ({entity['score']:.2f})")
