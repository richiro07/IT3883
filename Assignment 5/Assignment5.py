# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Richard Rodriguez
# Assignment Number: Assignment 5
# Due Date: 4/22
# Purpose: This program creates a SQLite database, stores temperature
#          readings from an input file, and calculates the average
#          temperature for Sunday and Thursday.
# Resources Used: Python sqlite3 documentation, course notes, and personal practice.

import sqlite3


def create_database(connection):
    """Create the temperature table if it does not already exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Temperature_Readings (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Day_Of_Week TEXT NOT NULL,
            Temperature_Value REAL NOT NULL
        )
    """)
    connection.commit()


def load_input_file(connection, input_filename):
    """Read the input file and insert each day/temperature pair into the database."""
    cursor = connection.cursor()

    # Clear old rows so the program can be run more than once without duplicating data.
    cursor.execute("DELETE FROM Temperature_Readings")

    with open(input_filename, "r", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.strip()
            if line:
                parts = line.split()
                day_of_week = parts[0]
                temperature_value = float(parts[1])

                cursor.execute("""
                    INSERT INTO Temperature_Readings (Day_Of_Week, Temperature_Value)
                    VALUES (?, ?)
                """, (day_of_week, temperature_value))

    connection.commit()


def get_average_temperature(connection, day_name):
    """Return the average temperature for the requested day."""
    cursor = connection.cursor()
    cursor.execute("""
        SELECT AVG(Temperature_Value)
        FROM Temperature_Readings
        WHERE Day_Of_Week = ?
    """, (day_name,))

    result = cursor.fetchone()[0]
    return result


def main():
    database_name = "assignment5_temperatures.db"
    input_filename = "Assignment5input.txt"

    # Connect to the SQLite database file.
    connection = sqlite3.connect(database_name)

    try:
        # Build the table and load the input data into it.
        create_database(connection)
        load_input_file(connection, input_filename)

        # Run SQL average queries for Sunday and Thursday.
        sunday_average = get_average_temperature(connection, "Sunday")
        thursday_average = get_average_temperature(connection, "Thursday")

        # Display the results to the console.
        print("Average temperature results:")
        print(f"Sunday average: {sunday_average:.2f}")
        print(f"Thursday average: {thursday_average:.2f}")

    finally:
        connection.close()


if __name__ == "__main__":
    main()
