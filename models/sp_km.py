import spacy

# Khmer Language models
nlp = spacy.load("km")


khmer_text = "ភាសាខ្មែរពិតជាអស្ចារ្យណាស់!"
input_khmer_text = khmer_text

# Processing text
doc = nlp(input_khmer_text)

# initial variables sentences boundaries
sentences = []
start = 0


# iterate through the tokens in the document
for token in doc:
    # Check if the token is a sentence-ending punctuation mark
    if token.is_sent_end:
        # Extract the sentence and append it to the list of sentences
        sentences.append(doc[start:token.i + 1])
        # update the starting index for the next sentence
        start = token.i + 1

# If there are remaining tokens after the last sentence-ending punctuation
if start < len(doc):
    sentences.append(doc[start:])

# Convert the sentences to text
sentence_texts = [sent.text for sent in sentences]

print("Segmented sentences: ")
for sentence in sentence_texts:
    print(sentence)