import random

card_types = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
card_ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class cards():
    def __init__(self,card_type,ranks):
        self.card_type = card_type
        self.ranks = ranks

    def __str__(self):
        return self.ranks +' Of '+self.card_type

class Deck_of_cards():
    def __init__(self):
        self.card_set=[]

        for card_type in card_types:
            for rank in card_ranks:
                main_cards = cards(card_type,rank)
                self.card_set.append(main_cards)
    def shuffle_card(self):
        random.shuffle(self.card_set)
    def deal(self):
        single_card=self.card_set.pop()
        return single_card

class player():
    def __init__(self,name):
        self.name=name
        self.card_set = []
    def remove(self):
        return self.card_set.pop(0)
    def add_card(self,new_card):
        if type(new_card) == type([]):
            return self.card_set.extend(new_card)
        else:
            return self.card_set.append(new_card)
    def __str__(self):
        return f'Player {self.name} has {len(self.card_set)} Cards.'



# GAME ON

player_one=player("one")
player_two=player("two")
new_dec=Deck_of_cards()
new_dec.shuffle_card()

for i in range(26):
    player_one.add_card(new_dec.deal())
    player_two.add_card(new_dec.deal())

game_on=True
round = 0
while game_on:
    round += 1
    print(f"Round {round}")
    if len(player_one.card_set) == 0:
        print(f"Player 1 Ount of cards, Player 2 Wins ")
        game_on = False
        break
    if len(player_two.card_set) == 0:
        print(f"Player 2 Ount of cards, Player 1 Wins ")
        game_on = False
        break
    player_one_card = []
    player_one_card.append(player_one.remove())

    player_two_card = []
    player_two_card.append(player_two.remove())
    at_war=True
    while at_war:
        if values[player_one_card[-1].ranks] > values[player_two_card[-1].ranks]:
            player_one.add_card(player_one_card)
            player_one.add_card(player_two_card)
            at_war=False
        elif values[player_two_card[-1].ranks] > values[player_one_card[-1].ranks]:
            player_two.add_card(player_two_card)
            player_two.add_card(player_one_card)
            at_war=False
        else:
            print("WAR !")
            if len(player_one.card_set) < 5:
                print("Player one Haven't Enough Card,Unable to Play!")
                print("Playe Two Won!,Player one Lose")
                game_on = False
                break
            elif len(player_two.card_set) < 5:
                print("Player two Haven't Enough Card,Unable to Play!")
                print("Playe one Won!,Player Two Lose")
                game_on = False
                break
            else:
                player_one_card.append(player_one.remove())
                player_two_card.append(player_two.remove())



