suits = ["spades", "clubs", "hearts", "diamonds"]
suit = suits[1]
rank = 'K'
value = 10

print(f"Your card is: {rank} of {suit}")
suits.append("FakeItem")
for suit in suits: print(suit)
suits.pop()
for suit in suits: print(suit)