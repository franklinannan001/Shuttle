# prompt the user for their name, the distance travelling and print the output
def main():
    name = input("What is your name: ")
    formatted_name = format_name(name)
    try:
        distance = float(input("Distance travelling(km): "))
        category = get_category(distance)
        if category is None:
            return None
        else:
            fare = calculate_fare(distance, category)
            print(
                f"{formatted_name}, your {category} trip of {distance:.1f}km costs KSH {fare:.1f}."
            )
    except ValueError:
        pass


# returns the passenger's name in title case
def format_name(n):
    n = n.strip().title()
    return n


# returns the category based on the passenger's distance
def get_category(d):
    if 0 < d <= 3:
        return "Short Hop"
    elif 3 < d <= 10:
        return "Standard"
    elif d > 10:
        return "Long Haul"
    else:
        return None


# returns the fare based on the passenger's distance and their category
def calculate_fare(d, c):
    if c == "Short Hop":
        return 20
    elif c == "Standard":
        return 15 * d
    else:
        return 10 * d


if __name__ == "__main__":
    main()
