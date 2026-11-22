# Custom BPE using predefined words and frequencies

from collections import Counter

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace


# Step 1: Define words and their frequencies

word_frequency = {
    "play": 5,
    "playing": 3,
    "played": 2
}

print("========== WORD FREQUENCIES ==========")

for word, frequency in word_frequency.items():
    print(word, ":", frequency)


# Step 2: Calculate initial adjacent character pair frequencies

pair_frequency = Counter()

print("\n========== ADJACENT CHARACTER PAIRS ==========")

for word, frequency in word_frequency.items():

    characters = list(word)

    pairs = list(zip(characters, characters[1:]))

    print("\nWord:", word)
    print("Character Pairs:", pairs)

    for pair in pairs:
        pair_frequency[pair] += frequency


print("\n========== INITIAL PAIR FREQUENCIES ==========")

for pair, frequency in pair_frequency.most_common():
    print(pair, ":", frequency)


# Step 3: Prepare training data using word frequencies

training_words = []

for word, frequency in word_frequency.items():
    training_words.extend([word] * frequency)


# Step 4: Create a BPE tokenizer

tokenizer = Tokenizer(
    BPE(unk_token="[UNK]")
)

tokenizer.pre_tokenizer = Whitespace()


# Step 5: Configure the BPE trainer

trainer = BpeTrainer(
    vocab_size=20,
    min_frequency=2,
    special_tokens=["[UNK]"]
)


# Step 6: Train the tokenizer

tokenizer.train_from_iterator(training_words, trainer)


# Step 7: Display the learned vocabulary

print("\n========== LEARNED VOCABULARY ==========")

vocabulary = tokenizer.get_vocab()

for token, token_id in sorted(
    vocabulary.items(), key=lambda item: item[1]
):
    print(token, ":", token_id)


print("\nTotal Vocabulary Size:", len(vocabulary))


# Step 8: Test the trained tokenizer

text = input("\nEnter a sentence: ")

output = tokenizer.encode(text)


print("\n========== TOKENIZATION RESULT ==========")

print("Original Text:", text)
print("BPE Tokens:", output.tokens)
print("Token IDs:", output.ids)
print("Total Tokens:", len(output.tokens))