# TCP Client Code
 
host="127.0.0.1"            # Set the server address to variable host
 
port=4446               # Sets the variable port to 4446
 
from socket import *             # Imports socket module
 
s=socket(AF_INET, SOCK_STREAM)      # Creates a socket
 
s.connect((host,port))          # Connect to server address

while(1):
	data=raw_input("Enter Your Choice 1 for 7up , 2 for 7 and 3 for 7 down:  ")
	s.send(data)
	amount = s.recv(3)
	print amount

 
    
 
s.close()                            # Closes the socket
# End of code


