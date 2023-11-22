from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences_1 = [
    "Instructions for internet use, please?",
    "Point me to the refreshments area?",
    "Location of the lavatories?",
    "I'd like to join additional learning sessions.",
    "When do the main talks begin?",
]
sentences_2 = [
    "How does one go online here?",
    "Where can I find snacks?",
    "Need to find the washroom.",
    "How to sign up for more classes?",
    "What's the schedule for keynote speeches?",
]

embeddings1 = model.encode(sentences_1, convert_to_tensor=True)
embeddings2 = model.encode(sentences_2, convert_to_tensor=True)

# Compute cosine-similarities
cosine_scores = util.cos_sim(embeddings1, embeddings2)

# Output the pairs with their score
for i in range(len(sentences_1)):
    print(
        "{} \t\t {} \t\t Score: {:.4f}".format(
            sentences_1[i], sentences_2[i], cosine_scores[i][i]
        )
    )
