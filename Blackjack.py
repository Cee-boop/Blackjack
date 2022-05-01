import sys, random as r

"""note: computer_cards [list] will always have string "comp" as the first element in 
    to identify if the computer is calling the function, hence using computer_cards from 
    index position 1 onwards when tallying sums."""


def pick_cards(hand, count):
    """
    Picks starting cards for player/comp, uses count variable for
    number of cards drawn. Checks if the function is being called by
    the computer [is_comp] and randomly choose 1 or 11 points if an ace is drawn.
    """
    
    # flag for identifying if computer is calling function:
    is_comp = False
    if len(hand) > 0 and hand[0] == 'comp': is_comp = True

    deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    while count > 0:
        # card is chosen randomly from deck:
        draw = r.choice(deck)

        # check if ace is drawn:
        if is_comp and draw == "A":
            if sum(hand) <= 10: hand.append(11)
            else: hand.append(1)

        # asks player to pick either 1 or 11 to add to score:
        if not is_comp and draw == "A":
            hand.append(int(input(f"Your cards: {hand}\nYou've drawn an ace. Add 1 or 11 points to total?: ")))

        # checks if draw is a certain card and adds/allocates the points to list/score accordingly
        royals, numbers = ["K", "Q", "J"], [2, 3, 4, 5, 6, 7, 8, 9, 10]
        if draw in royals: hand.append(10)
        if draw in numbers: hand.append(draw)

        count -= 1

    return hand


def hitting(player_cards, computer_cards, hit):
    """
    Player/computer hits. If comp's hand sum is under 17,
    draws until equal to or greater than 17.
    """
    
    while hit:
        # if hit is true: the player wants another card
        player_cards = pick_cards(player_cards, 1)
        if sum(player_cards) >= 21:
            break

        if sum(player_cards) < 21:
            hit_again = input(f"Your cards: {player_cards} {sum(player_cards)} points.\nHit again? y/n ")
            if hit_again == "n":
                hit = False
            else:
                hitting(player_cards, computer_cards, hit)

    print(f"Your final hand is: {player_cards} {sum(player_cards)} points.")

    # Blackjack rules: dealer must draw another card until their score is >= 17:
    while sum(computer_cards[1:]) < 17:
        computer_cards = pick_cards(computer_cards, 1)

    print(f"Computer's final hand: {computer_cards[1:]} {sum(computer_cards[1:])} points.")
    print(result(player_cards, computer_cards[1:]))
    new_game(input("To play again type 'y', or 'n' to quit: "))


def result(player, computer):
    """
    Checks the total sum of player/computer hands and returns the outcome.
    """
    
    if sum(computer) < sum(player) <= 21 or sum(player) <= 21 < sum(computer):
        return "You Win!"
    if sum(player) < sum(computer) <= 21 or sum(computer) <= 21 < sum(player):
        return "You Lose!"
    if sum(player) == sum(computer):
        return "Draw."
    else:
        return "You lose!"


def new_game(answer):
    """
    Meat and potatoes. Displays player/computer hands and player hits.
    """
    
    if answer == "n":
        print("Thanks for playing!")
        sys.exit()

    # calls function to deal cards for player and computer:
    player_cards, computer_cards = pick_cards([], 2), pick_cards(['comp'], 2)
    if sum(player_cards) == 21: print(result(player_cards, computer_cards[1:]))

    print(f"Your cards: {player_cards} {sum(player_cards)} points.\n"
          f"Computer's first card: {computer_cards[1]}")

    # if player wants to draw another card: hit changes to true
    hit = False
    if input("Type 'h' to hit or 'p' to pass: ") .lower() == "h": hit = True
    hitting(player_cards, computer_cards, hit)


new_game(input("Do you want to play a game of Blackjack? type 'y' or not 'n': ").lower())



