from tokenizers import Tokenizer, models, trainers, pre_tokenizers

# Creating the bpe tokenizer so that we can train later.
tokenizer = Tokenizer(model=models.BPE())
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel()

# Training data
text = [
    "Hello world!",
    "Hello there!",
    "World of NLP",
    "Tokenization is fun",
    "Machine learning is fascinating"
]

# Training the tokenizers
trainer = trainers.BpeTrainer(vocab_size=1000, min_frequency=1)
tokenizer.train_from_iterator(text, trainer)

#Use the tokenizer to create tokens from text data
test_data = "Hello tokenization world!"
encodings = tokenizer.encode(test_data)
print("Bpe tokens: ", encodings.tokens)
print("Token Ids: ", encodings.ids)

decoded = tokenizer.decode(encodings.ids)
print("Decoded: ", decoded)
