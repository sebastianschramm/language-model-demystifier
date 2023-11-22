from transformers import pipeline

clf_pipe = pipeline(
    "text-classification",
    model="nlpodyssey/bert-multilingual-uncased-geo-countries-headlines",
)

prompt = (
    "Paris is celebrated around the world for its iconic"
    " Eiffel Tower and rich cultural heritage."
)
response = clf_pipe(prompt)
print(response)
