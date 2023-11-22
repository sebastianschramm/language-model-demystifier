from transformers import pipeline

qa_pipe = pipeline("question-answering", model="deepset/bert-base-cased-squad2")

document = """Cloud computing is a technology that allows individuals and businesses to
              access computing resources over the Internet. It enables users to utilize
              hardware and software that are managed by third parties at remote
              locations. Services provided by cloud computing include storage solutions,
              databases, and computing power, which can be used on a pay-per-use basis.
              This model offers flexibility and scalability, reducing the need for
              large upfront investments in infrastructure. Major providers of cloud
              computing services include Amazon Web Services (AWS), Microsoft Azure,
              and Google Cloud Platform (GCP)."""

question = "What are the major providers of cloud computing services?"

response = qa_pipe(question=question, context=document)
print(response)
