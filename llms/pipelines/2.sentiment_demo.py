import os
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"

from transformers import pipeline

classifier = pipeline("text-classification",
                      model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
result = classifier("I love iPad")
print(result)

result = classifier("I could not stand Mr. Tom")
print(result)
