# BPE tokenization using Pre-trained GPT2 tokenizer

from transformers import AutoTokenizer
from collections import Counter

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = input("Enter a sentence: ") or "I love learning python"

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Original Sentence:", text)
print("BPE Tokens:",tokens)
print("Token IDs:",token_ids)
print("Length of Tokens:",len(tokens))

# Calculate individual token frequencies
token_frequency = Counter(tokens)

print("\n========== TOKEN FREQUENCIES ==========")

for token, frequency in token_frequency.items():
    print(token, ":", frequency)

# Count neighboring tokens; tokens[1:] is the same list without its first token.
pair_frequency = Counter(zip(tokens, tokens[1:]))

print("\n========== ADJACENT TOKEN PAIR FREQUENCIES ==========")

for pair, frequency in pair_frequency.items():
    print(pair, ":", frequency)

# Decode tokens
decoded_text = tokenizer.decode(token_ids)

print("\nDecoded Text:", decoded_text)