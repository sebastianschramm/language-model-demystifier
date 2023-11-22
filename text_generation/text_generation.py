from transformers import pipeline

generation_pipeline = pipeline("text-generation", model="gpt2", return_full_text=False)

prompt = "The assassination of John F. Kennedy, the 35th U.S. president, occurred on"
response = generation_pipeline(prompt)
print(response[0]["generated_text"])
