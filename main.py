with open('text.txt', 'r', encoding="utf-8") as file:
    text = file.read()
unique = set(text.split())
with open('output.txt', 'w', encoding="utf-8") as f:
    for word in unique:
        f.write(word + '\n')
print(unique)
