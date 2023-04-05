balance = 50

while True:
    print(f"Amount Due: {balance}")

    coin = int(input("Insert Coin: "))

    if coin not in (5, 10, 25):
        print("Invalid Coin")
        continue

    balance -= coin

    if balance == 0:
        print("Thank you for your purchase")
        break

    elif balance < 0:
        print(f"Change Owed: {-balance}")
        break
