def main():
    current_time = input("Current time: ")

    if 7. <= convert(current_time) <= 8.:
        print("Breakfast")
    elif 12. <= convert(current_time) <= 13.:
        print("Lunch")
    elif 18 <= convert(current_time) <= 19:
        print("Dinner")
    else:
        print("Snack")


def convert(time):
    time = time.split(":")
    time = int(time[0]) + (int(time[1]) / 60)

    return time

if __name__ == "__main__":
    main()
