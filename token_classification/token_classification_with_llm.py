from transformers import pipeline

generation_pipeline = pipeline(
    "text-generation",
    model="Universal-NER/UniNER-7B-all",
    return_full_text=False,
    max_new_tokens=50,
)

prompt_template = """A virtual assistant answers questions from a user based on the provided text.
USER: Text: {input_text}
ASSISTANT: I’ve read this text.
USER: What describes {entity_name} in the text?
ASSISTANT:
"""

prompt = prompt_template.format_map(
    {
        "input_text": "My name is Sebastian Schramm and I live in Cologne, Germany. The other day, I was in Turin.",
        "entity_name": "city",
    }
)

response = generation_pipeline(prompt)
print(response[0]["generated_text"])
