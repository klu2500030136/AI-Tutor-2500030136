# Pretrained SentencePiece Tokenization using T5
# The marker at the beginning of a token represents a word boundary.

# Uses T5’s pretrained SentencePiece tokenizer and displays tokens, IDs, frequencies, and decoded text.

from collections import Counter
from transformers import AutoTokenizer

# Step 1: Load pretrained T5 tokenizer
tokenizer = AutoTokenizer.from_pretrained("t5-small")

# Step 2: Get input sentence
text = input("Enter a sentence: ") or "I love Learning python"

# Step 3: Generate SentencePiece tokens
tokens = tokenizer.tokenize(text)

# Step 4: Convert tokens into IDs
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("\n========== TOKENIZATION RESULT ==========")

print("Original Text:", text)
print("SentencePiece Tokens:", tokens)
print("Token IDs:", token_ids)
print("Total Tokens:", len(tokens))

# Step 5: Calculate individual token frequencies
token_frequency = Counter(tokens)

print("\n========== TOKEN FREQUENCIES ==========")

for token, frequency in token_frequency.items():
    print(token, ":", frequency)

# Step 6: Count neighboring tokens using the list shifted by one position.
pair_frequency = Counter(zip(tokens, tokens[1:]))

print("\n========== ADJACENT TOKEN PAIR FREQUENCIES ==========")

for pair, frequency in pair_frequency.items():
    print(pair, ":", frequency)

# Step 7: Decode token IDs
decoded_text = tokenizer.decode(token_ids)

print("\n========== DECODED TEXT ==========")

print("Decoded Text:", decoded_text)