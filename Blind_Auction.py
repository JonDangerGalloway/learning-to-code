all_names = []

def new_bidder(name, bid):
    bid_dict = {}
    bid_dict["name"] = name
    bid_dict["bid"] = bid
    all_names.append(bid_dict)

should_bid = True
while should_bid:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    new_bidder(name, bid)
    # print(all_names)
    question = input("Is there another bidder? 'Yes' or 'No?' \n").lower()
    if question == "no":
        should_bid = False
        # clear()
        number = 0
        high_bidder = ""
        for bidder in range(len(all_names)):
            called = all_names[bidder]
            bids = called["bid"]
            name = called["name"]
            if bids > number:
                number = bids
                high_bidder = name
        print(f"The high bidder is {high_bidder} with a bid of ${number}!")