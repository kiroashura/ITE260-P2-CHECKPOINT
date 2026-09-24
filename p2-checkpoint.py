def calculate_average(activity1, activity2, activity3):
    return (activity1 + activity2 + activity3) / 3


def get_status(average):
    if average >= 90:
        return "Excellent, galinggg"
    elif average >= 80:
        return "Very Good, onti pa"
    elif average >= 75:
        return "Pasang awa"
    else:
        return "Failed, aray ko po"


def main():
    for student_number in range(1, 6):
        print("\nStudent", student_number)

        name = input("Enter name: ")

        activity1 = float(input("Activity 1: "))
        activity2 = float(input("Activity 2: "))
        activity3 = float(input("Activity 3: "))

        average = calculate_average(activity1, activity2, activity3)
        status = get_status(average)

        print("\nName:", name)
        print("Average:", round(average, 2))
        print("Status:", status)


if __name__ == "__main__":
    main()