''' server.py
Modified by Patrick Page
UAID: 010282806

usage: Python3 server.py PORT
Take in menu selection from user, does computations if necessary, and returns result to client
11/10/21 modified for Python 3
'''

from ctypes import sizeof
import sys

# Import socket library
from socket import *

# Set port number by converting argument string to integer
# If no arguments set a default port number
# Defaults
if sys.argv.__len__() != 2:
    serverPort = 5556
# Get port number from command line
else:
    serverPort = int(sys.argv[1])

# Choose SOCK_STREAM, which is TCP
# This is a welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# The SO_REUSEADDR flag tells the kernel to reuse a local socket
# in TIME_WAIT state, without waiting for its natural timeout to expire.
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Start listening on specified port
serverSocket.bind(('', serverPort))

# Listener begins listening
serverSocket.listen(1)


print("The server is ready to receive")

#set initial balance of $100.00
balance = float(100.00)

sep = " "
connected = True

# Forever, read in banking selection, perform calculations/operations, and send back to client
while connected:
    # Wait for connection and create a new socket
    # It blocks here waiting for connection
    connectionSocket, addr = serverSocket.accept()

    # Read bytes from socket and decode them and split them based off the seperator (same sep as client)
    selection = connectionSocket.recv(1024).decode('utf-8').split(sep)

    #make variables for selection (0 position) and amount (1 position) if applicable
    if(len(selection) > 1):
        choice = selection[0]
        number = selection[1]
    else:
        choice = selection[0]  

    # Logic for depositing money (increase balance)
    if(choice == "1"):
        amount = float(number)
        balance += amount
        #format string to have floating point numbers with precision of 2 when referencing the money.
        depositString = "${:.2f}".format(amount) + " deposited...\n\nRemaining Balance: " + "${:.2f}".format(balance)
        #encode and send bytes back to client
        depositStringBytes = depositString.encode('utf-8')
        connectionSocket.send(depositStringBytes)           

    # Logic for withdrawing money (decrease balance)
    if(choice == "2"):
        amount = float(number)
        
        # Checking to ensure enough funds are there to make the withdrawal without going negative
        # (if so complete transaction, otherwise tell user insufficient funds)
        if(balance - amount < 0):
            withdrawalString = "Insufficient Funds..."
        else:
            balance -= amount
            withdrawalString = "${:.2f}".format(amount) + " withdrawn...\n\nRemaining Balance: " + "{:.2f}".format(balance)
        # Encode and send bytes back to client 
        withdrawalStringBytes = withdrawalString.encode('utf-8')
        connectionSocket.send(withdrawalStringBytes) 

    # Logic for checking balance (send balance to user)
    elif(choice == "3"):
        #encode and send string with balance to client
        balanceString = "Current Balance: ${:.2f}".format(balance)
        connectionSocket.send(balanceString.encode('utf-8'))

#final closing of socket when program stops running
connectionSocket.close()

