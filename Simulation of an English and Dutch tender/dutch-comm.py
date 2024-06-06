import random
from math import sqrt

# Define the Auction class
class Auction:
    def __init__(self, sellers, buyers):
        self.sellers = sellers  # Set the sellers
        self.buyers = buyers  # Set the buyers

    # Method to remove loser buyers
    def remove_loser_buyer(self, buyers_copy, loser_buyers):
        for buyer in self.buyers:  # Iterate through the buyers
            if (buyer in loser_buyers and (buyer in buyers_copy)):  # If the buyer is a loser and is in the copy of buyers, remove them
                buyers_copy.remove(buyer)

    # Method to run the auction
    def run_auction(self):
        self.sellers = sorted(self.sellers, key=lambda x: x.max_price)  # Sort the sellers based on max price
        for seller in self.sellers:
            print(seller.name, seller.max_price)  # Print seller name and max price
        for buyer in self.buyers:
            print(buyer.name, buyer.payment_ceiling)  # Print buyer name and payment ceiling
        for seller in self.sellers:
            timer = 15  # Set a timer for 15 rounds
            self.buyers = sorted(self.buyers, key=lambda x: calculate_distance(seller.point, x.point))  # Sort the buyers based on distance from seller
            buyers_copy = self.buyers[:]  # Create a copy of the buyers
            loser_buyers = []  # Initialize list for loser buyers
            winner = None  # Initialize winner as None
            for buyer in self.buyers:
                if (buyer.payment_ceiling > seller.min_price):
                    buyer.current_price = seller.max_price  # Set buyer's current price to seller's max price if their payment ceiling is higher than seller's min price
                else:
                    loser_buyers.append(buyer)  # Add buyer to loser buyers list if their payment ceiling is not higher than seller's min price

            self.remove_loser_buyer(buyers_copy, loser_buyers)  # Call method to remove loser buyers
            while (timer > 0):
                for buyer in buyers_copy:
                    if (buyer.is_worthwhile(seller.point, timer)):  # Check if buyer is worthwhile at this round
                        winner = buyer  # Set winner as the buyer
                        print(f"Winner: {winner.name}, Seller: {seller.name} , price = {winner.current_price}")  # Print winner's information
                        self.buyers.remove(winner)  # Remove winner from list of buyers
                        break
                if (not (winner)):  # If there's no winner
                    if (seller.max_price == seller.min_price):  # If seller's max price equals min price
                        print(f"There are no buyers for {seller.name} seller")  # Print message indicating no buyers for the seller
                        break
                    else:
                        seller.proposed_decrease(timer)  # Call method to propose decrease in price for the seller
                if (winner):  # If there's a winner, break the loop
                    break
                timer = timer - 1  # Decrement timer

# Define the node class
class node:
    def __init__(self, name):
        self.name = name
        self.point = (random.randint(0, 20), random.randint(0, 20))  # Generate random point coordinates

# Define the Seller class which inherits from node
class Seller(node):
    def __init__(self, name):
        self.name = name
        self.min_price = random.randint(1, 10) * 100  # Generate random min price
        self.max_price = random.randint(int(self.min_price / 100), 10) * 100  # Generate random max price
        self.point = (random.randint(0, 20), random.randint(0, 20))  # Generate random point coordinates

    def proposed_decrease(self, time):
        rate = (self.max_price - self.min_price) / (time * 100)  # Calculate rate of decrease based on time
        self.max_price = (int(self.max_price / 100 - (random.uniform(1, rate)))) * 100  # Update max price with proposed decrease

# Define the Buyer class which inherits from node
class Buyer(node):
    def __init__(self, name):
        self.name = name
        self.payment_ceiling = random.randint(0, 20) * 100  # Generate random payment ceiling
        self.current_price = 0  # Initialize current price as 0

    def is_worthwhile(self, seller_point, now_time):
        max_dis = calculate_distance((20, 20), (0, 0))  # Calculate maximum distance between points
        distance = ((max_dis - calculate_distance(self.point, seller_point)) / max_dis) * 0.3  # Calculate distance factor
        current = ((2000 - self.current_price) / 2000) * 0.3  # Calculate current price factor
        time = ((15 - now_time) / 15) * 0.3  # Calculate time factor
        x = distance + current + time + random.uniform(0, 0.1)  # Calculate combined factor
        if (x >= 0.5):  # Check if combined factor is greater than or equal to 0.5
            return True
        else:
            return False

# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Example Usage:
# Create sellers and buyers
sellers = [Seller("s1"), Seller("s2"), Seller("s3")]
buyers = [Buyer("b1"), Buyer("b2"), Buyer("b3"), Buyer("b4")]

# Create an instance of Auction and run the auction
auction = Auction(sellers, buyers)
auction.run_auction()
