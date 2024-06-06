# Class for seller
import time
class Seller:
  def __init__(self, id, initial_price):
    self.id = id
    self.price = initial_price

# Class for buyer    
class Buyer:
  def __init__(self, id, distance, payment_ceiling):
    self.id = id 
    self.distance = distance
    self.payment_ceiling = payment_ceiling
    self.current_bid = 0

  def bid(self):
    return random.randint(100,200)

  def __lt__(self, other):
    if self.current_bid < other.current_bid:
      return True
    elif self.current_bid == other.current_bid:  
      if self.payment_ceiling > other.payment_ceiling:
        return True
      elif self.payment_ceiling == other.payment_ceiling:
        return self.distance < other.distance

# Auction function
def english_auction(sellers, buyers, timer):

  # Convert buyers to Buyer objects  
  # Convert buyers to Buyer objects  
  buyers_list = [Buyer(b['id'], b['distance'], b['payment_ceiling']) for b in buyers]
 

  for seller in sellers:

    # Auction loop
    while time.time() < timer: 

      # Get next buyer
      current_buyer = heappop(buyers_list)  

      # Get highest bid      
      highest_bid = get_highest_bid(buyers_list)

      # Ask for new bid      
      new_bid = current_buyer.bid()  

      # Check and update bids
      # Remove buyers

      buyers_list = get_remaining_buyers()

# Sample sellers
sellers = [
  Seller(1, 100), 
  Seller(2, 150)
]

# Sample buyers 
buyers = [
  {'id': 1, 'distance':5, 'payment_ceiling':200},
  {'id': 2, 'distance':10, 'payment_ceiling':150}, 
  {'id': 3, 'distance':15, 'payment_ceiling':300}
]

# Run auction for 5 minutes
timer = time.time() + 300

english_auction(sellers, buyers, timer)
