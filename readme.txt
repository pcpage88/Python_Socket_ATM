//Patrick Page
//November 11, 2021
//UAID: 010282806

To run this basic Automatic Teller Machine (ATM) Socket Program you need to do the following (in this order):

1) Open two different windows command prompt or linux command line windows. 

2) Log into turing.csce.uark.edu through ssh.

3) Traverse to the folder which contains server.py in one window and the folder which contains client.py in the other.

4a) Set up the server first by typing python3 server.py #### ("####" represents the port number you would like to use.
	This is optional, if you enter nothing default port number (5556) will be selected in program).
4b) Once the server socket is established, run the client application by typing python3 client.py localhost #### ("####" represents the port number used for the server.
	This is optional, if default port number was used for the server, default for client will work as well so you can just type python3 client.py (default is localhost 5556))

5) Once the client is up and running, this is the program you (the user) will be dealing with the entire time.

6) Select an option from the menu that is printed to the screen, read the response sent back from the server, then make another selection.

7) Any other instructions you receive from the client will most likely be error-checking so follow what the instructions say.

8) Select menu option 4 and press enter to exit the program.

9) Enjoy this basic ATM machine socket program written in Python v3.9

