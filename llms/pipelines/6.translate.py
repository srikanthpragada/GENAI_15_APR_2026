import os
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"

from transformers import pipeline

translator = pipeline(
    task="text-generation",
    model="bigscience/bloomz-560m"
)

text = "Translate English to Spanish: How are you?"

result = translator(text, max_new_tokens=50)

print(result[0]["generated_text"])
