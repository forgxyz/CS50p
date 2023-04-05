camel = input("camelCase: ")

snake = ""

for letter in camel:
    if letter.isupper():
        letter = "_" + letter.lower()
    snake += letter

print(snake)
