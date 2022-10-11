logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

from replit import clear
bid_cont=True
print(logo)
print("Welcome to the secreat auction program")

bidshanary ={}

def bid_values(self,bid_key,bid_value):

    self[bid_key]=bid_value
while bid_cont:    
    name=input("What is your Name :")
    bid=int(input("please enter your bid :$"))  
    
    bid_values(bidshanary,name,bid)
    YN=input("Is there another bidder Y/N ").upper()
    if YN =='N':
        bid_cont=False
    clear()
# print("The highest bid is:")
key_max=max(zip(bidshanary.values(),bidshanary.keys()))[1]
# print(bidshanary)
print(f"The highest bid is {bidshanary[key_max]} from {key_max}")
