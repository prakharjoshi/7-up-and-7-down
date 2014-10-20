# TCP Server Code
 
host="127.0.0.1"                # Set the server address to variable host
port=4446              # Sets the variable port to 4446
from socket import *  
import random              # Imports socket module


s=socket(AF_INET, SOCK_STREAM)
 
s.bind((host,port))         # Binds the socket. Note that the input to
                                         # the bind function is a tuple
 
s.listen(1)
                         # Sets socket to listening state with a  queue
                                            # of 1 connection
 
print "Listening for connections.. "
 
q,addr=s.accept()              
count = 100                                           
while(count > 0):
	a = random.randint(1,13)
	print a
	msg = q.recv(1024)
	print msg
	if msg == '3' and a < 7:
		count = count + 10
	elif msg == '2' and a == 7:
		count = count + 20
	elif msg == '1' and a > 7:
		count = count + 10
	else:
		count = count - 10
	
	"""if (msg == 1):
		if (a > 7):
			count = count + 10
		else:
			count = count - 10
	elif (msg == 2):
		if(a == 7):
			count = count + 20
		else:
			count = count - 10
	elif (msg == 3):
		if(a < 7):
			count = count + 10
		else:
			count = count - 10"""


	

		 

	amount = str(count)
	q.send(amount)
	                      
 
	
 
s.close()
 
# End of code
