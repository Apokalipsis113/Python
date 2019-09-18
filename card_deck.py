#card_deck.py
import pandas as pd
import numpy as np

def card_names():
#'''Create pandas.DataFrame object with deck'''
    # names for deck cards
    color = ['red', 'black']
    suit_red = ['diamonds', 'hearts']
    suit_black = ['spades', 'clubs' ]
    suit = [suit_red, suit_black]
    joker = 'Joker'
    pack = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = []
    i = 0
    j = 53
    for clr in color:
       deck.append([j, clr, None, joker])
       j += 1
       for st in suit:
           if st is suit_red:
               for st_r in suit_red:
                   for card in pack:
                       i += 1
                       deck.append([i, clr, st_r, card])
    df = pd.DataFrame(deck, columns=['index', 'color', 'suit', 'card'])
    df.set_index('index', inplace=True)
    df.sort_index(inplace=True)
    return df

def suit_name(suit_str):
    if suit_str in ['diamonds']:
        return "\u2666"
    if suit_str in ['hearts']:
        return "\u2665"
    if suit_str in ['spades']:
        return "\u2660"
    if suit_str in ['clubs']:
        return "\u2663"
    return "Jocker"