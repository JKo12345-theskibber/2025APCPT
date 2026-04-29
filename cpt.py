# Data with ratings added
national_parks = {
    "california": [
        {"name": "Yosemite National Park", "rating": 5},
        {"name": "Sequoia National Park", "rating": 4},
        {"name": "Death Valley National Park", "rating": 3}
    ],
    "utah": [
        {"name": "Zion National Park", "rating": 5},
        {"name": "Bryce Canyon National Park", "rating": 4},
        {"name": "Arches National Park", "rating": 5}
    ],
    "florida": [
        {"name": "Everglades National Park", "rating": 4},
        {"name": "Biscayne National Park", "rating": 3}
    ],
    "arizona": [
        {"name": "Grand Canyon National Park", "rating": 5},
        {"name": "Saguaro National Park", "rating": 4}
    ]
}

# Function 1: Find parks by state
def find_parks(state):
    return national_parks.get(state, None)

# Function 2: Search for a park across all states
def search_park(park_name):
    for state, parks in national_parks.items():
        for park in parks:
            if park_name.lower() in park["name"].lower():
                return state, park["name"]
    return None, None

# Function 3: Filter parks by rating
def filter_by_rating(min_rating):
    results = []
    for state, parks in national_parks.items():
        for park in parks:
            if park["rating"] >= min_rating:
                results.append((park["name"], state))
    return results

# Main program loop
while True:
    print("\n--- National Parks Program ---")
    print("1. Find parks by state")
    print("2. Search for a park")
    print("3. Filter parks by rating")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        state = input("Enter a state: ").lower()
        parks = find_parks(state)

        if parks:
            print("\nNational Parks in", state.title() + ":")
            for park in parks:
                print("-", park["name"])
        else:
            print("\nSorry, that state is not in the database.")

    elif choice == "2":
        name = input("Enter park name: ")
        state, park = search_park(name)

        if park:
            print(f"\n{park} is in {state.title()}.")
        else:
            print("\nPark not found.")

    elif choice == "3":
    try:
        rating = int(input("Enter minimum rating (1-5): "))
        if rating < 1 or rating > 5:          # add this
            print("\nPlease enter a number between 1 and 5.")
        else:
            results = filter_by_rating(rating)
            if results:
                print("\nParks with rating", rating, "or higher:")
                for park, state in results:
                    print(f"- {park} ({state.title()})")
            else:
                print("\nNo parks found with that rating.")
    except ValueError:
        print("\nPlease enter a valid number.")

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Try again.")
