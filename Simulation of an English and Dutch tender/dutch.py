import random
from math import sqrt

# Define the Auction class
class Auction:
    def __init__(self, sellers, buyers):
        self.sellers = sellers # Set the sellers
        self.buyers = buyers # Set the buyers
        
    # Method to remove loser buyers
    def remove_loser_buyer(self,buyers_copy,loser_buyers):
        for buyer in self.buyers: # Iterate through the buyers              
            if(buyer in  loser_buyers and  (buyer in buyers_copy)): # If the buyer is a loser and is in the copy of buyers, remove them
                buyers_copy.remove(buyer)
                
    # Method to run the auction
    def run_auction(self):
        self.sellers = sorted(self.sellers, key=lambda x: x.max_price) # Sort the sellers based on max price
        for seller in self.sellers:
            print(seller.name,seller.max_price)# Print seller name and max price
        for buyer in self.buyers:
            print(buyer.name,buyer.payment_ceiling)
        for seller in self.sellers:
            timer = 15  # set a timer for 10 rounds
            self.buyers = sorted(self.buyers, key=lambda x: calculate_distance(seller.point,x.point))
            buyers_copy=[]
            buyers_copy = self.buyers[:]
            loser_buyers = []
            winner = None
            for buyer in self.buyers:
                    if(buyer.payment_ceiling>seller.min_price):
                        buyer.current_price = seller.max_price
                    else:
                        loser_buyers.append(buyer)
                        
            auction.remove_loser_buyer(buyers_copy,loser_buyers)
            while(timer>0 ):
                for buyer in buyers_copy:
                    if(buyer.is_worthwhile(seller.point,timer)):
                        winner = buyer
                        print(f"Winner: {winner.name}, Seller: {seller.name} , price = {winner.current_price}")
                        self.buyers.remove(winner)
                        break
                if (not(winner)):
                    if(seller.max_price==seller.min_price):
                        print(f"There are no buyers for {seller.name} seller")
                        break
                    else:
                        seller.proposed_decrease(timer)
                if(winner):
                    break
                timer=timer-1
        
                            
                              

class node:
    def __init__(self,name):
        self.name = name
        self.point = (random.randint(0,20),random.randint(0,20))
    



class Seller(node):
    def __init__(self, name):
        self.name = name
        self.min_price = random.randint(1,10)*100 
        self.max_price = random.randint(int(self.min_price/100), 10)*100
        self.point = (random.randint(0,20),random.randint(0,20))
        
    def proposed_decrease(self,time):
        rate = (self.max_price-self.min_price)/(time*100)
        self.max_price = (int(self.max_price/100-(random.uniform(1,rate))))*100    
        


class Buyer(node):
    def __init__(self, name):
        self.name = name
        self.payment_ceiling = random.randint(0,20)*100 
        self.current_price = 0 
        self.point = (random.randint(0,20),random.randint(0,20))
    def is_worthwhile(self,seller_point , now_time):
        max_dis = calculate_distance((20,20) , (0,0))
        distance = ((max_dis - calculate_distance(self.point , seller_point))/max_dis)*0.3
        current = ((2000-self.current_price)/2000)*0.3
        time = ((15-now_time)/15)*0.3
        x = distance + current + time + random.uniform(0, 0.1)
        if(x>=0.5):
            return True
        else:
            return False
        
        
        
    

def calculate_distance(point1, point2):
    return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Example Usage:
# sellers = [Seller("s1"), Seller("s2"), Seller("s3")]
# buyers = [Buyer("b1" , 1000,(10,5)), Buyer("b2",1500,(7,4)), Buyer("b3", 1500,(3,4)),Buyer("b4",700,(6,9))]
sellers = [Seller("s1"), Seller("s2"), Seller("s3")]
buyers = [Buyer("b1"), Buyer("b2"), Buyer("b3"),Buyer("b4")]

auction = Auction(sellers, buyers)
auction.run_auction()