# TCP Server Code
from socket import *
from thread import *
host=""                
port=4446              
from socket import *  
import random              

#CONNECTION_LIST = []
#RECV_BUFFER = 4096
s=socket(AF_INET, SOCK_STREAM)
address = (host,port)
s.bind(address)         
s.listen(5)
#CONNECTION_LIST.append(s)


def clientthread(q):
#infinite loop so that function do not terminate and thread do not end.
        count = 100
        final_count = 100
        while(count > 0):
            a = random.randint(1,13)
            bid = q.recv(3)
            money = int(bid)
            diff = final_count - money
            #print diff
            msg = q.recv(1)
            choice  = int(msg)
            if choice == 3 and a<7:
                money = 2*money
            elif choice == 2 and a == 7:
                money = 3*money
            elif choice == 1 and a>7:
                money = 2*money
            else:
                money = 000
            final_count = diff + money
            if choice in range(1,4):
                amount = str(final_count)
            else:
                amount = "001"
            print amount
            q.send(amount)
            b = str(a)
            print a
            q.send(b)
            #print "the final amount of player " + str(q) + " " + "is" + " " + amount
            #count = final_count

     		

while True:
    q,addr = s.accept()
    temp = 0
    msg = str(addr) + " wants to play your game. 1 for yes and 2 for no"
    a = input(msg)
    if a == 1:
        start_new_thread(clientthread,(q,))
s.close()
q.close()