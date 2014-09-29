# TCP Client Code
 
host="127.0.0.1"            # Set the server address to variable host
 
port=4446               # Sets the variable port to 4446
 
from socket import *             # Imports socket module
 
s=socket(AF_INET, SOCK_STREAM)      # Creates a socket
 
s.connect((host,port))          # Connect to server address

while(1): 
    msg=s.recv(1024)            # Receives data upto 1024 bytes and stores in variables msg
 
    print "Message from server : " + msg

    data=raw_input("Enter data to be send:  ")  # Data to be send is stored in variable data from
                                           # user
 
    s.send(data)  
 
s.close()                            # Closes the socket
# End of code


