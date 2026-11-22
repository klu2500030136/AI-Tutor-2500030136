word = input("Enter a word: ") or "python"

print("Word: ",word)
print("Length = ", len(word))

Characters = list(word)

print("Characters in the given word: ",Characters)

pairs = list(zip(Characters, Characters[1:]))

print("Adjacent pairs: ", pairs)