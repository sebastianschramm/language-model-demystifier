# Token Classification

## NER

![Alt text](../code_png_images/token_classification.png?raw=true)
![Alt text](../code_png_images/token_classification_response.png?raw=true)

This is a simple example using a pre-trained BERT model fine-tuned for tasks like Named Entity Recognition (NER) or Part-of-speech (POS) tagging.

```console
python token_classification.py
```

You can then enter a sentence and the model will annotate the tokens accordingly, e.g.:

- My name is Sebastian Schramm and I live in Cologne, Germany.
- As the sun sets over the historic streets of Paris, the bustling markets of Barcelona come alive, while the serene canals of Amsterdam reflect the charm of European cities.

## NER with LLMs

![Alt text](../code_png_images/token_classification_with_llm.png?raw=true)
![Alt text](../code_png_images/token_classification_with_llm_response.png?raw=true)

Here we use a LLM that has been fine-tuned for the NER task -  essentially we are using text generation to perform NER.

```bash
python token_classification_with_llm.py
```
