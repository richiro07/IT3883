# ---------------------------------------------------
# Program Name: Assignment1.py
# Course: IT3883 / Section W01
# Student Name: Richard Rodriguez Martinez
# Assignment Number: Lab 1
# Due Date: 1/21/2026
# Purpose:
# This program provides a text-based menu that allows
# the user to append text to a buffer, clear the buffer,
# display the current buffer contents, or exit the program.
# Resources Used:
# - Class lecture slides
# - Instructor examples
# - Personal practice
# ---------------------------------------------------

# Variable to store the input buffer
input_buffer = ""

# Variable to control the loop
running = True

# Main program loop
while running:
    print("\n--- Text Buffer Menu ---")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Get user choice
    choice = input("Select an option (1-4): ")

    # Option 1: Append data
    if choice == "1":
        user_text = input("Enter text to append: ")
        input_buffer += user_text
        print("Text has been added to the buffer.")

    # Option 2: Clear buffer
    elif choice == "2":
        input_buffer = ""
        print("Input buffer has been cleared.")

    # Option 3: Display buffer
    elif choice == "3":
        if input_buffer == "":
            print("The input buffer is currently empty.")
        else:
            print("Current input buffer:")
            print(input_buffer)

    # Option 4: Exit program
    elif choice == "4":
        print("Exiting program. Goodbye!")
        running = False

    # Invalid option
    else:
        print("Invalid selection. Please choose a number between 1 and 4.")