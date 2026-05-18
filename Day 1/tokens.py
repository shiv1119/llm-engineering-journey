from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
text = "The cat is sitting on the table."
tokens = tokenizer.tokenize(text)
print(tokens)