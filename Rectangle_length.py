#function to calculate the input
def calculate_length(area, width):
    length = round(area / width, 2)
    return length


def main():
    # The greetings to the User
    print(
        "Hello fellow human 🙂, Today we are gonna find out the length of your rectangle."
    )
    #The Display questions
    area_str = input("Enter the area (cm): ")
    width_str = input("Enter the width (cm): ")
    # The calculations
    try:
        area = float(area_str)
        width = float(width_str)
    except ValueError as error:
        print(error)
    else:
        length = calculate_length(area, width)
        print(f"The length of your rectangle is {length} cm.")


if __name__ == "__main__":
    main()
