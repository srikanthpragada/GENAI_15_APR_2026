import os
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"

from transformers import pipeline

client = pipeline(task="any-to-any", model="Helsinki-NLP/opus-mt-en-hi")

text = "How are you?"
hindi = client(text)
print(hindi)




     