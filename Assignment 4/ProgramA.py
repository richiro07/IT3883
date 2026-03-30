# Program Name: ProgramB.py
# Course: IT3883/Section W01
# Student Name: Richard Rodriguez
# Assignment Number: Assignment 4
# Due Date: 04/01/2026
# Purpose: This program listens for a message from Program A over a socket,
# converts the message to uppercase, displays it, and sends the uppercase
# version back to Program A.
# Resources Used: Course notes, assignment instructions.

import socket

HOST = "127.0.0.1"
PORT = 40001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Type messages (type 'exit' to quit):")

while True:
    message = input("You: ")
    client_socket.sendall(message.encode())

    if message.lower() == "exit":
        break

    response = client_socket.recv(1024).decode()
    print("Server:", response)

client_socket.close()
