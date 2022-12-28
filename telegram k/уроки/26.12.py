s = "1231212cat123123213cqt123123cat1323132cat"
с = 0

for i in range(0, len(s) - 2):
    if s[i] + s[i + 1] + s[i + 2] == "cat":
        с += 1
print(с)