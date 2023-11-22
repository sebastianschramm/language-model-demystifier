from transformers import pipeline

mask_pipe = pipeline("fill-mask", model="bert-large-cased")

prompt = "I am so [MASK] to talk about this topic!"
response = mask_pipe(prompt, top_k=1)
print(response)
