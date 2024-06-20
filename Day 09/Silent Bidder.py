from replit import clear
import art
bids = {}

print(art.logo)
print(art.start)

def Bidding_Auction():
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

def Greatest_Bidder():
    max = 0
    max_name = ""
    for i in bids:
        if bids[i] > max:
            max = bids[i]
            max_name = i
    print(art.end)
    print(f"The winner is {max_name} with a bid of ${max}")

Bidding_Auction() #For First Bidder
#For Next Bidders
loop = input("Are there any other bidders? Type 'yes or 'no'.")
while loop == "yes":
    clear()
    print(art.logo)
    Bidding_Auction()
    loop = input("Are there any other bidders? Type 'yes or 'no'.")
Greatest_Bidder()
