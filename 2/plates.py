def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha() or not s.isalnum():
        return False
    elif len(s) < 2 or len(s) > 6:
        return False
    elif s[-1].isalpha() and not s.isalpha():
        return False
    elif is_first_zero(s):
        return False
    else:
        return True


def is_first_zero(s):
    for letter in s:
        if letter.isdigit():
            return True if int(letter) == 0 else False


main()
