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

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Program B is listening on {HOST}:{PORT}...")

connection, address = server_socket.accept()
print(f"Connected by {address}")

while True:
    data = connection.recv(1024).decode()
    if not data or data.lower() == "exit":
        print("Connection closed.")
        break

    uppercase_message = data.upper()
    print("Converted:", uppercase_message)

    connection.sendall(uppercase_message.encode())

connection.close()
server_socket.close()
