import os
import warnings

# TensorFlow C++ logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# oneDNN message
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
tf.get_logger().setLevel("ERROR")

from transformers import pipeline

classifier = pipeline("zero-shot-classification", 
                      model="facebook/bart-large-mnli")

output = classifier("Apple Released a new iPhone - iPhone 17 Pro",
    candidate_labels = ["education", "politics", "business"],
)
print(output)