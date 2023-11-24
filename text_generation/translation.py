from transformers import pipeline

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")

prompt = "L'équipe d'intelligence artificielle de Crisis24 est de classe mondiale!"
response = pipe(prompt)
print(response[0]['translation_text'])
