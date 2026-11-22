# WordPiece Tokenization using Pretrained BERT

from collections import Counter
from transformers import AutoTokenizer

# Load pretrained BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Get input sentence
text = input("Enter a sentence: ") or "I love Learning python"

# Generate WordPiece tokens
tokens = tokenizer.tokenize(text)

# Convert tokens into IDs
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("\n========== TOKENIZATION RESULT ==========")

print("Original Sentence:", text)
print("WordPiece Tokens:", tokens)
print("Token IDs:", token_ids)
print("Total Tokens:", len(tokens))

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

# The uncased tokenizer lowercases text, so decoding does not restore capitals.
decoded_text = tokenizer.decode(token_ids)

print("\nDecoded Text:", decoded_text)