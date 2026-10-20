import random

#lager 2 lister med alle kortverdiene og typene og en tom liste som de skal legges inn i senere
values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
suits = ["Hearts","Spades", "Clubs", "Diamonds"]
kortstokk = []
# lager en klasse som heter kort med parameterene: suit & value
class Kort:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

for value in values:
    for suit in suits:
        kort1 = Kort(value, suit)
        kortstokk.append(kort1)






print(len(kortstokk))

random.shuffle(kortstokk)

for kort in kortstokk:
    print(kort.value, kort.suit)




