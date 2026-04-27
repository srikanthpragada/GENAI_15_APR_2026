import os
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
#os.environ["TQDM_DISABLE"] = "1"

from transformers import pipeline

classifier = pipeline("zero-shot-classification", 
                      model="facebook/bart-large-mnli")

output = classifier("Apple Released a new iPhone - iPhone 17 Pro",
    candidate_labels = ["education", "politics", "business"],
)
print(output)