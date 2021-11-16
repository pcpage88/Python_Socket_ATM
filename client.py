''' client.py
Modified by Patrick Page
UAID: 010282806

usage: Python3 client.py HOSTNAMEorIP PORT
Reads menu selection from user, sends to server, and prints resulting server response
11/10/21 modified for Python 3
'''

import sys

# Import socket library
from socket import *

# Set hostname or IP address from command line or default to localhost
# Set port number by converting argument string to integer or use default
# Use defaults
if sys.argv.__len__() != 3:
    serverName = 'localhost'
    serverPort = 5556
# Get from command line
else:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
clientSocket.connect((serverName, serverPort))

# Function Called to Print Bank Menu
def bank_menu():       
    print (15 * "-"),("MENU") , (15 * "-")
    print ("1. Deposit")
    print ("2. Withdrawal")
    print ("3. Check Balance")
    print ("4. Exit")
    print (34 * "-")

#print banking menu to screen
bank_menu()

#initialize seperator string
sep = " "

# Get selection from user
selection = input("Please enter banking selection: ")

while selection != "4":
    # If user wants to make a deposit
    if selection == "1":
        #Deposit function
        amount = input("Enter amount to be deposited: ")

        #Error checking on amount to deposit entered by user
        while(amount.isalpha()):
            amount = input("Invalid entry. Please enter numeric amount to deposit:")
        if(float(amount) < 0.0):
            while(float(amount) < 0.0):
                amount = input("Please enter a positive amount to deposit: ")

        # add strings for user selection and deposit amount with seperator in the middle        
        fullPacket = selection + sep + amount
        clientSocket.send(fullPacket.encode('utf-8'))   #encode message to be sent to server
        depositBytes = clientSocket.recv(1024)          #receive response from server
        deposit = depositBytes.decode('utf-8')          #decode response from server and print to screeen
        print()
        print(deposit)

        #close socket and reopen for next user selection
        clientSocket.close()
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))

    # If user wants to Withdraw money    
    elif selection == "2":
        #Withdrawal function
        amount = input("Enter amount to be withdrawn: ")

        #Error checking on amount to withdrawal entered by user
        while(amount.isalpha()):
            amount = input("Invalid entry. Please enter numeric amount to deposit:")        
        if(float(amount) < 0.0):
            while(float(amount) < 0.0):
                amount = input("Please enter a positive number to withdrawal: ")

        # add strings for user selection and withdrawal amount with seperator in the middle
        fullPacket = selection + sep + amount
        clientSocket.send(fullPacket.encode('utf-8'))   #encode and send to server
        withdrawalBytes = clientSocket.recv(1024)       #receive answer from server
        withdrawal = withdrawalBytes.decode('utf-8')    #decode and then print to screen
        print()
        print(withdrawal)

        #close socket and reopen for next user selection
        clientSocket.close()                            
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))

    #user wants to check their account balance
    elif selection == "3":
        #Balance inquiry
        #selectionString = selection + " "
        selectionBytes = selection.encode('utf-8')      #encode selection byte 
        clientSocket.send(selectionBytes)               #send byte to server
        encodedBalance = clientSocket.recv(1024)        #receive response from server and print decoded message
        print()
        print(encodedBalance.decode('utf-8'))
        
        #close socket and reopne new one for next user transaction
        clientSocket.close()
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
    else:
        print("Invalid Selection. Try again!")

    print()
    bank_menu()
    selection = input("Please enter banking selection: ")


# When user selects 4(exit) then print a thank you message and close the socket one final time.
print("\nThank you for banking with U of A Bank.  Goodbye!\n")

clientSocket.close()
