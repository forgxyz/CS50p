vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Input: ")

for letter in word:
    if letter.lower() in vowels:
        word = word.replace(letter, "")

print(word)
