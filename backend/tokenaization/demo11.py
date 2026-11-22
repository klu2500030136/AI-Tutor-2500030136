# Custom BPE using an external corpus

from collections import Counter
from pathlib import Path

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace


# Step 1: Read the external corpus

corpus_path = Path(__file__).with_name("corpus.txt")
print(__file__)


with open(corpus_path, "r", encoding="utf-8") as file:
    words = file.read().lower().split()


# Step 2: Calculate word frequencies

word_frequency = Counter(words)

print("========== WORD FREQUENCIES ==========")

for word, frequency in word_frequency.items():
    print(word, ":", frequency)


# Step 3: Calculate initial adjacent character pair frequencies

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


# Step 4: Prepare corpus data for training

training_words = []

for word, frequency in word_frequency.items():
    training_words.extend([word] * frequency)


# Step 5: Create a BPE tokenizer

tokenizer = Tokenizer(
    BPE(unk_token="[UNK]")
)

tokenizer.pre_tokenizer = Whitespace()


# Step 6: Configure the BPE trainer

trainer = BpeTrainer(
    vocab_size=20,
    min_frequency=2,
    special_tokens=["[UNK]"]
)


# Step 7: Train the tokenizer

tokenizer.train_from_iterator(training_words, trainer)


# Step 8: Display the learned vocabulary

print("\n========== LEARNED VOCABULARY ==========")

vocabulary = tokenizer.get_vocab()

for token, token_id in sorted(
    vocabulary.items(), key=lambda item: item[1]
):
    print(token, ":", token_id)


print("\nTotal Vocabulary Size:", len(vocabulary))


# Step 9: Test the trained tokenizer

text = input("\nEnter a sentence: ") or "I am learning python"

output = tokenizer.encode(text)


print("\n========== TOKENIZATION RESULT ==========")

print("Original Text:", text)
print("BPE Tokens:", output.tokens)
print("Token IDs:", output.ids)
print("Total Tokens:", len(output.tokens))