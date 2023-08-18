import random

def get_card_stack():
    cardStack = []
    for i in range(40):
        cardStack.append(i+1)
    return cardStack

def shuffle(cardstack):
    shuffledstack = []
    while len(cardstack)>0:
        card = random.choice(cardstack)
        cardstack.remove(card)
        shuffledstack.append(card)
    return shuffledstack

def get_top_card(cardstack):
    return cardstack.pop()

def find_and_replace(hand, card_to_replace, new_card, discard_pile):
    if card_to_replace == 0:
        discard_pile.append(new_card)
    else:
        index = hand.index(card_to_replace)
        hand.remove(card_to_replace)
        hand.insert(index, new_card)
        discard_pile.append(card_to_replace)

def add_card_to_discard(deck, discard_pile):
    if len(deck) > 0:
        card = get_top_card(deck)
        discard_pile.append(card)
    else:
        random.shuffle(discard_pile)
        deck.extend(discard_pile)
        discard_pile.clear()



def deal_initial_hand(deck):
    u_rack = []
    c_rack = []
    d_rack = []
    for i in range(10):
        u_rack.append(get_top_card(deck))
        c_rack.append(get_top_card(deck))
    d_rack.append(get_top_card(deck))
    return u_rack,c_rack,d_rack

def print_top_to_bottom(rack):
    
    for number in rack:
        print(number)

def check_racko(rack):  
    prev    = 0  
    for i in rack:
        if i > prev:
            prev = i    
        else:
            return False
    return True

def get_point(rack):  
    
    point  = 0
    prev   = 0  
    for i in rack:
        if i > prev:
            prev = i
            point += 5    
    if (point == 50):
        point +=25
    return point


def deck_or_discard_pile(deck,discard_pile, computer = False):
    while True:
        if computer == False:
            choice = input("Get card from (D)eck or Discard (P)ile = ")
        else: 
            choice = random.choice(["D", "P"])

        if "D" == choice.upper():
            return get_top_card(deck),"D"
        if "P" == choice.upper():
            return get_top_card(discard_pile),"P"
            
def which_card_replaced(hand):
    while True:
        #print("Your Hand:")
        #print_top_to_bottom(hand)
        choice = input("Which card do you want to replace? ('0' for no) = ")
        if str(choice).isnumeric():
            card = int(choice)
            if (card == 0 ):
                return card
            elif list(hand).count(card) > 0 :
                return card
            else:
                print(card, "doesn't exist your hand")    
       

def user_turn(hand, deck, discard_pile):

    while True:
        print("\033[H\033[J", end="")
        print("User Hand:")
        print_top_to_bottom(hand)
        print("Discard Pile = ", "* " * (len(discard_pile) - 1), discard_pile[-1])
        print("Deck         = ", "* " * len(deck))

        new_card, choice = deck_or_discard_pile(deck, discard_pile)
        print("Your card is = ", new_card)

        hand_card = which_card_replaced(hand)

        find_and_replace(hand, hand_card, new_card, discard_pile)

        if len(deck) == 0:
            add_card_to_discard(deck, discard_pile)
        else:
            if choice == "D":
                break




def computer_turn(hand, deck, discard_pile):

    #print("Computer's Turn:")
    #print("Computer Hand: ", hand)

    new_card, _ = deck_or_discard_pile(deck, discard_pile, True)
    #print("Computer's card is: ", new_card)

    for hand_card in hand:
        if new_card < hand_card:
            index = hand.index(hand_card)
            hand.remove(hand_card)
            hand.insert(index,new_card)
            discard_pile.append(new_card)
            break
    #print("New Computer Hand: ", hand)



def main():
    deck = get_card_stack()
    deck = shuffle(deck)
    u_rack, c_rack, discard_pile = deal_initial_hand(deck)

    while not (check_racko(u_rack) or check_racko(c_rack)):
        user_turn(u_rack, deck, discard_pile)
        computer_turn(c_rack, deck, discard_pile)

    if check_racko(u_rack):
        print("\033[H\033[J", end="")
        print("You win !!!!!!")
        print("Your Hand : ", u_rack)
        print("Your point: ", get_point(u_rack))
        print("My   point: ", get_point(c_rack))
    else:
        print("\033[H\033[J", end="")
        print("You lose !!!!!!")
        print("My Hand : ", u_rack)
        print("My   point: ", get_point(c_rack))
        print("Your point: ", get_point(u_rack))


main()
