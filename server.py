# TCP Server Code
from socket import *
from thread import *
host=""                
port=4447             
from socket import *  
import random  
from Tkinter import *            

s=socket(AF_INET, SOCK_STREAM)
address = (host,port)
s.bind(address)         
s.listen(5)



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
            #print amount
            length = len(amount)
            if length == 1:
                amount = '00' + amount 
            if length == 2:
                amount = '0' + amount
            print amount
            q.send(amount)
            b = str(a)
            card_length = len(b)
            if card_length == 1:
                b = '0' + b
            q.send(b)
            
     		

while True:
    q,addr = s.accept()
    #temp = 0
    #root = Tk()
    #root.title("Client authentication")
    #root.geometry("150x200")
    #root.play_lbl = Label(root, text = 'str(addr) + " wants to play your game. 1 for yes and 2 for no: "')
    #root.play_lbl.grid(row = 1, column = 0, sticky = W)
    #root.play_ent = Entry(root)
    #root.play_ent.grid(row = 1, column = 1, sticky = W)
    
    #root.submit_bttn = Button(root, text = "accept", command = root.play_ent.get())
    #root.submit_bttn.grid(row = 2, column = 0, sticky = W)
    #a = root.play_ent.get()
    #print()
    option = input('str(addr) + " wants to play your game. 1 for yes and 2 for no: "')   
    q.send(str(option))
    #root.mainloop()
    #root.quit()
    #root.quit()
    if option == 1:
        start_new_thread(clientthread,(q,))
s.close()
q.close()