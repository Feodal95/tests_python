text = input()
i = 0
while i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        text = text[:i] + text[i + 1:]
        continue
    i += 1
print(text)