import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o-mini")

text = "LangGraph enables agent workflows"
tokens = encoding.encode(text)
print("Token Count: ", len(tokens))
print("Token Ids: ", tokens)

decoded = encoding.decode(tokens)
print("Decoded Tokens: ", decoded)

for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"ID: {token_id} -> {token_text}")