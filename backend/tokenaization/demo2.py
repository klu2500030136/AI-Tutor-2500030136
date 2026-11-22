text = input("Enter a sentence: ") or "I Love Learning Python"

print("Length = ", len(text))
print("Characters in the given text are: ")

for ch in text:
    print(ch, end=",")