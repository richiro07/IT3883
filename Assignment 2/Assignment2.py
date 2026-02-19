# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Richard Rodriguez
# Assignment Number: Assignment 2
# Due Date: 2/18/2026
# Purpose: This program reads a file with student names and scores,
# calculates each student’s average, and prints the results
# in descending order by average grade.
# Resources: Class notes and personal practice

# open the input file
file = open("Assignment2input.txt", "r")

students = []

# read each line in the file
for line in file:
    parts = line.strip().split()

    name = parts[0]
    scores = parts[1:]

    # convert scores to integers
    total = 0
    for score in scores:
        total += int(score)

    average = total / len(scores)

    # store name and average in a list
    students.append((name, average))

file.close()

# sort students by average in descending order
students.sort(key=lambda x: x[1], reverse=True)

# print results
for student in students:
    print(f"{student[0]} {student[1]:.2f}")
