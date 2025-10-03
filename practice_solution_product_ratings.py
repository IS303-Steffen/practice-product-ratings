# Practice: Vendor Product Ratings Analyzer
# Tracks 1–5 star ratings for a few products at a campus pop-up market.

ratings_dict = {
    "tshirts": [],
    "mugs": [],
    "stickers": []
}

def average_rating(ratings_dict, product):
    """
    Return the average rating (float) for a single product.
    If a product has no ratings, return 0.0.
    """
    product_ratings = ratings_dict.get(product)
    if len(product_ratings) == 0:
        return 0.0
    
    total = 0
    for r in product_ratings:
        total += r
    return total / len(product_ratings)

def latest_rating(ratings_dict, product):
    """
    Return the most recent rating for a single product.
    If there are no ratings, return None.
    """
    product_ratings = ratings_dict.get(product, [])
    if len(product_ratings) == 0:
        return None
    return product_ratings[-1]  # last appended value

print("Welcome to the Vendor Product Ratings Analyzer!")

while True:
    print("\nMenu:")
    print("1: Add a rating")
    print("2: Show average rating for each product")
    print("3: Show latest rating for each product")
    print("4: Show all raw ratings")
    print("5: Exit")
    choice = input("Enter an option (1-5): ").strip()

    if choice == "1":
        print("\nProducts:")
        for p in ratings_dict: # get the keys from the ratings dictionary
            print(f"\t{p}")

        product = input("Enter a product name: ").lower()
        
        # convert to int before doing comparison
        r = int(input("Enter a rating (1-5): "))

        if product in ratings_dict and 1 <= r <= 5:
            ratings_dict[product].append(r) # put the rating in that product's rating list
            print(f"Added rating {r} to {product}.")
        else:
            print("Invalid product or rating out of range.")

    elif choice == "2":
        print()
        for product in ratings_dict:
            avg = average_rating(ratings_dict, product)
            print(f"{product}: average = {avg:.2f}")

    elif choice == "3":
        print("\nLatest Ratings:")
        for product in ratings_dict:
            latest = latest_rating(ratings_dict, product)
            if latest is None: # could also do == instead of is, doesn't technically matter too much.
                print(f"{product}: no ratings yet")
            else:
                print(f"{product}: latest rating = {latest}")

    elif choice == "4":
        print("\n--- Raw Ratings ---")
        for product, values in ratings_dict.items():
            print(f"{product}: {values}")

    elif choice == "5":
        print("Exiting. Goodbye.")
        break

    else:
        print("Invalid choice, try again!")