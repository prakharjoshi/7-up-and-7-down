host="0.0.0.0"            
 
port=4447             
 
from socket import *             
 
s=socket(AF_INET, SOCK_STREAM)      
address = (host,port) 
s.connect(address) 
test = s.recv(1)
tet = int(test)


from Tkinter import *
class Application(Frame):
    """ GUI application which can retrieve an auto number to guess. """ 
    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        """ Instruction Label """
        # Create instruction label for Program
        self.inst_lbl = Label(self, text = "Follow the Steps")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        """ Player Name """         
        # Create label for name    
        self.name_lbl = Label(self, text = "Player Name: ")
        self.name_lbl.grid(row = 3, column = 0, sticky = W)
        
        # Create entry widget to accept name      
        self.name_ent = Entry(self)
        self.name_ent.grid(row = 3, column = 1, sticky = W)
        """ Bid Input """ 
        # Create label for entering Guess  
        self.bid_lbl = Label(self, text = "How much You want to bid")
        self.bid_lbl.grid(row = 6, column = 0, sticky = W)
        # Create entry widget to accept Guess  
        self.bid_ent = Entry(self)
        self.bid_ent.grid(row = 6, column = 1, sticky = W)
        # Create a space  
        #self.gap1_lbl = Label(self, text = " ")
        #self.gap1_lbl.grid(row = 3, column = 0, sticky = W)

        """play input"""
        self.play_lbl = Label(self, text = "1 for 7up, 2 for 7, 3 for 7 down")
        self.play_lbl.grid(row = 10, column = 0, sticky = W)
        # Create entry widget to accept Guess  
        self.play_ent = Entry(self)
        self.play_ent.grid(row = 10, column = 1, sticky = W)
        # Create a space  
        self.gap1_lbl = Label(self, text = " ")
        self.gap1_lbl.grid(row = 14, column = 0, sticky = W)

        """ Submit Button """
        
        # Create submit button
        self.submit_bttn = Button(self, text = "BID", command = self.reveal)
        self.submit_bttn.grid(row = 16, column = 0, sticky = W)
        # Create a space  
        self.gap2_lbl = Label(self, text = " ")
        self.gap2_lbl.grid(row = 18, column = 0, sticky = W)
        """ RESET """
        
        # Create submit button
        #self.reset_bttn = Button(self, text = "Proceed", command = self.reveal)
        #self.reset_bttn.grid(row = 6, column = 1, sticky = W)
        """ Display """
        # Create text widget to display welcome_msg
        self.display1_txt = Text(self, width = 50, height = 3, wrap = WORD)
        self.display1_txt.grid(row = 20, column = 0, columnspan = 2, sticky = W)
        # Create text widget to display bid_msg
        self.display2_txt = Text(self, width = 50, height = 3, wrap = WORD)
        self.display2_txt.grid(row = 21, column = 0, columnspan = 2, sticky = W)
        # Create text widget to display result_msg
        self.display3_txt = Text(self, width = 50, height = 5, wrap = WORD)
        self.display3_txt.grid(row = 22, column = 0, columnspan = 2, sticky = W)
        # Create text widget to display choice_msg
        self.display4_txt = Text(self, width = 45, height = 2, wrap = WORD)
        self.display4_txt.grid(row = 23, column = 0, columnspan = 2, sticky = W)
        # Create text widget to display card_msg
        self.display5_txt = Text(self, width = 45, height = 2, wrap = WORD)
        self.display5_txt.grid(row = 24, column = 0, columnspan = 2, sticky = W)
        
    def reveal(self):
        global tries
        name = self.name_ent.get()
        next_bid = self.bid_ent.get()
        choice = self.play_ent.get()
        welcome_msg = "Welcome " + name 
        bid_msg = " Your Bid was: " + next_bid
        choice_msg = "You have entered " + str(choice)
        s.send(next_bid)
        s.send(choice)
        
        res = s.recv(3)
        res = int(res)
        print res
        if res > 0 and res != " ":
            result_msg = "You have " + str(res) + " amount left."
        elif res == 001:
            result_msg = "You entered wrong choice"
        else:
            result_msg = "You Lost all your Money!! :("
        card = s.recv(2)
        print card
        card_msg = "Card number comes is " + str(card)
        # Display
        self.display1_txt.delete(0.0, END)
        self.display1_txt.insert(0.0, welcome_msg)
        self.display2_txt.delete(0.0, END)
        self.display2_txt.insert(0.0, bid_msg)
        self.display3_txt.delete(0.0, END)
        self.display3_txt.insert(0.0, result_msg)
        self.display4_txt.delete(0.0, END)
        self.display4_txt.insert(0.0, choice_msg)
        self.display5_txt.delete(0.0, END)
        self.display5_txt.insert(0.0, card_msg)
        
    
# Main manager
if(tet == 1):
    root = Tk()
    root.title("7 Up and 7 Down")
    root.geometry("900x600")
    app = Application(root)
    root.mainloop()
    s.close()
