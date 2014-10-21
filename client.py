# TCP Client Code
import Tkinter
host="127.0.0.1"            
 
port=4446               
 
from socket import *             
 
s=socket(AF_INET, SOCK_STREAM)      
 
s.connect((host,port)) 



# Code to add widgets will go here...


while(1):
	next_bid=raw_input("How much You wanna bid, You have 100 rupees initially: ")
	data=raw_input("Enter Your Choice 1 for 7up , 2 for 7 and 3 for 7 down:  ")
	s.send(next_bid)
	s.send(data)
	amount = s.recv(4)
	print amount

s.close() 

                         


