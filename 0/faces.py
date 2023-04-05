def main():
    user = input("Are you happy or sad? ")
    print(convert(user))

def convert(emoji):
    return emoji.replace(':)', '🙂').replace(':(', '😢')

main()