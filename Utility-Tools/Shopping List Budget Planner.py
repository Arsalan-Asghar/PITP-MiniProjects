# Week 1 - Mini Project 2 -Shopping List and Budget Planner:
def shopping_list():
    # 1. LOOP to ensure valid budget input
    while True:
        try:
            budget = float(input("Enter your budget: "))
            break # Break loop if input is a valid number
        except ValueError:
            print("Please enter a number for the budget.")

    total_cost = 0
    shopping_items = {}

    while True:
        item = input("Enter item name (or type 'done' to finish): ")
        if item.lower() == "done":
            break

        # 2. Check for duplicate items (Optional logic)
        if item in shopping_items:
            print(f"You already have {item}. Updating price.")

        try:
            price = float(input(f"Enter price of {item}: "))
            shopping_items[item] = price

        except ValueError:
            print("Invalid input! Please enter a valid price.")

    # Recalculate total accurately from the dictionary at the end
    total_cost = sum(shopping_items.values())

    print("\n--- Shopping List ---")
    for item, price in shopping_items.items():
        print(f"{item}: ${price:.2f}")

    print(f"\nTotal cost: ${total_cost:.2f}")

    # 3. Show remaining balance or deficit
    difference = budget - total_cost

    if total_cost > budget:
        print(f"Warning: You exceeded your budget by ${abs(difference):.2f}!")
    else:
        print(f"Success: You are within budget! You have ${difference:.2f} left.")

shopping_list()
