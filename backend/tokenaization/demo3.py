tokens = ["maths", "science", "english", "history", "geography"]
print("Tokens: ", tokens)

print("Length of tokens: ", len(tokens))
print("First token: ", tokens[0])
print("Last token: ", tokens[-1])
print("Last token: ", tokens[len(tokens)-1])

print("First two tokens: ", tokens[0:2])
print("Tokens in reverse: ", tokens[::-1])
print("Last two tokens: ", tokens[-2:])

for token in tokens:
    print(token, end=",")


