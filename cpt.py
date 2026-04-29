# Dictionary storing national parks organized by state
# Each park has a name and a rating (1-5)
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

# Returns a list of parks for a given state, or None if state not found
def find_parks(state):
    return national_parks.get(state, None)

# Searches all states for a park matching the input name
# Returns the state and park name if found, otherwise returns None, None
def search_park(park_name):
    for state, parks in national_parks.items():
        for park in parks:
            if park_name.lower() in park["name"].lower():
                return state, park["name"]
    return None, None

# Filters all parks by a minimum rating
# Returns a list of (park name, state) tuples that meet the threshold
def filter_by_rating(min_rating):
    results = []
    for state, parks in national_parks.items():
        for park in parks:
            if park["rating"] >= min_rating:
                results.append((park["name"], state))
    return results

# Main program loop — runs until user selects Quit
while True:
    print("\n--- National Parks Program ---")
    print("1. Find parks by state")
    print("2. Search for a park")
    print("3. Filter parks by rating")
    print("4. Quit")
    choice = input("Choose an option: ")

    # Option 1: Look up all parks in a given state
    if choice == "1":
        state = input("Enter a state: ").lower()
        parks = find_parks(state)
        if parks:
            print("\nNational Parks in", state.title() + ":")
            for park in parks:
                print("-", park["name"])
        else:
            print("\nSorry, that state is not in the database.")

    # Option 2: Search for a specific park by name
    elif choice == "2":
        name = input("Enter park name: ")
        state, park = search_park(name)
        if park:
            print(f"\n{park} is in {state.title()}.")
        else:
            print("\nPark not found.")

    # Option 3: Filter parks by minimum rating
    # Includes error handling for non-integer input and out-of-range values
    elif choice == "3":
        try:
            rating = int(input("Enter minimum rating (1-5): "))
            if rating < 1 or rating > 5:
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

    # Option 4: Exit the program
    elif choice == "4":
        print("\nGoodbye!")
        break

    # Handles any invalid menu input
    else:
        print("\nInvalid choice. Try again.")
