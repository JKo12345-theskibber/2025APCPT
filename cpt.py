national_parks = {
    "california": [
        "Yosemite National Park",
        "Sequoia National Park",
        "Death Valley National Park"
    ],
    "utah": [
        "Zion National Park",
        "Bryce Canyon National Park",
        "Arches National Park"
    ],
    "florida": [
        "Everglades National Park",
        "Biscayne National Park"
    ],
    "arizona": [
        "Grand Canyon National Park",
        "Saguaro National Park"
    ]
}

# procedure
def find_parks(state):
    if state in national_parks:
        print("\nNational Parks in", state.title() + ":")
        # Iteration
        for park in national_parks[state]:
            print("-", park)
    else:
        print("\nSorry, that state is not in the database.")

#input
user_state = input("Enter a state to find national parks: ").lower()

#call the function
find_parks(user_state)
