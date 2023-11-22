from transformers import pipeline

clf_pipe = pipeline(
    "token-classification", model="ml6team/bert-base-uncased-city-country-ner"
)

prompt = "My name is Sebastian Schramm and I live in Cologne, Germany."
response = clf_pipe(prompt)
print(response)
