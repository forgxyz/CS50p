def main():
    fruits = [
        {"name": "Apple", "calories": 130},
        {"name": "Avocado", "calories": 50},
        {"name": "Banana", "calories": 110},
        {"name": "Cantaloupe", "calories": 50}
    ]

    request = input("Item ")

    success = False
        
    for item in fruits:
        if item["name"].lower() == request.lower():
            print(f"Calories: {item['calories']}")
            success = True

    if success:
        return True
    else:
        print("item not found")
        return False

main()