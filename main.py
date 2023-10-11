import random


class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  #called when print is invoked on an object from this class
  def __str__(self):
    return f"{self.rank['rank']} of {self.suit}"


class Deck:

  def __init__(self):
    self.cards = []
    suits = ["spades", "clubs", "hearts", "diamonds"]
    ranks = [{
        "rank": "A",
        "value": 11
    }, {
        "rank": "2",
        "value": 2
    }, {
        "rank": "3",
        "value": 3
    }, {
        "rank": "4",
        "value": 4
    }, {
        "rank": "5",
        "value": 5
    }, {
        "rank": "6",
        "value": 6
    }, {
        "rank": "7",
        "value": 7
    }, {
        "rank": "8",
        "value": 8
    }, {
        "rank": "9",
        "value": 9
    }, {
        "rank": "10",
        "value": 10
    }, {
        "rank": "J",
        "value": 10
    }, {
        "rank": "Q",
        "value": 10
    }, {
        "rank": "K",
        "value": 10
    }]
    for suit in suits:
      for rank in ranks:
        self.cards.append(Card(suit, rank))

  def shuffle(self):
    if (len(self.cards) > 1):
      random.shuffle(self.cards)

  def deal(self, number):
    cards_dealt = []
    for card in range(number):
      if (len(self.cards) > 0):
        card = self.cards.pop()
        cards_dealt.append(card)
    return cards_dealt


class Hand:

  def __init__(self, dealer=False):
    self.cards = []
    self.value = 0
    self.dealer = dealer

  def addCard(self, card_list):
    self.cards.extend(card_list)

  def calculateValue(self):
    self.value = 0
    hasAce = False

    for card in self.cards:
      cardValue = int(card.rank["value"])
      self.value += cardValue
      if card.rank["rank"] == "A":
        hasAce = True

    if hasAce and self.value > 21:
      self.value -= 10

  def getValue(self):
    self.calculateValue()
    return self.value

  def isBlackjack(self):
    return self.getValue() == 21

  def display(self, showAllDealerCards=False):
    print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
    for index, card in enumerate(self.cards):
      if index == 0 and self.dealer \
      and not showAllDealerCards \
      and not self.isBlackjack():
        print("hidden")
      else:
        print(card)

    if not self.dealer:
      print("Value: ", self.getValue())
      print()


class Game:

  def play(self):
    gameNumber = 0
    gamesToPlay = 0

    while gamesToPlay <= 0:
      try:
        gamesToPlay = int(input("How many games do you want to play? "))
      except ValueError:
        print("You must enter a number.")

    while gameNumber < gamesToPlay:
      gameNumber += 1
      deck = Deck()
      deck.shuffle()

      playerHand = Hand()
      dealerHand = Hand(dealer=True)

      for i in range(2):
        playerHand.addCard(deck.deal(1))
        dealerHand.addCard(deck.deal(1))

      print()
      print("*" * 30)
      print(f"Game {gameNumber} of {gamesToPlay}")
      print("*" * 30)
      playerHand.display()
      dealerHand.display()

      if self.checkWinner(playerHand, dealerHand):
        continue
      choice = ""
      while playerHand.getValue() < 21 and choice not in ["s", "stand"]:
        choice = input("Please chooose 'Hit' or 'Stand': ").lower()
        print()
        while choice not in ["h", "hit", "s", "stand"]:
          choice = input("Please chooose 'Hit' or 'Stand' (or H/S) ").lower()
          print()
        if choice in ["hit", "h"]:
          playerHand.addCard(deck.deal(1))
          playerHand.display()
      if self.checkWinner(playerHand, dealerHand):
        continue

      playerHandValue = playerHand.getValue()
      dealerHandValue = dealerHand.getValue()

      while dealerHandValue < 17:
        dealerHand.addCard(deck.deal(1))
        dealerHandValue = dealerHand.getValue()

      dealerHand.display(showAllDealerCards=True)

      if self.checkWinner(playerHand, dealerHand):
        continue

      print("Final Results")
      print("Your hand: ", playerHandValue)
      print("Dealers hand: ", dealerHandValue)

      self.checkWinner(playerHand, dealerHand, True)

  print("\nThanks for playing")

  def checkWinner(self, playerHand, dealerHand, gameOver=False):
    if not gameOver:
      if playerHand.getValue() > 21:
        print("You busted. Dealer wins.")
        return True
      elif dealerHand.getValue() > 21:
        print("Dealer busted. You win!")
        return True
      elif dealerHand.getValue() == 21 \
      and playerHand.getValue() == 21:
        print("Both have blackjack! Tie!")
        return True
      elif playerHand.getValue() == 21:
        print("You have blackjack, you win!")
        return True
      elif dealerHand.getValue() == 21:
        print("Dealer has blackjack, you lose.")
        return True
    else:
      if playerHand.getValue() > dealerHand.getValue():
        print("You win!")
      elif playerHand.getValue == dealerHand.getValue():
        print("You tied!")
      else:
        print("Dealer wins.")
        return True
      return False


g = Game()
g.play()
