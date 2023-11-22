from transformers import pipeline

clf_pipe = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")

prompt = "I like to play football and tennis."
candidate_labels = [
    "sport",
    "music",
    "politics",
    "business",
    "technology",
    "entertainment",
    "science",
    "health",
    "war",
]
response = clf_pipe(prompt, candidate_labels=candidate_labels)
print(response)
