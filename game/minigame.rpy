label end:
    call memory_game(["Alien", "Dinosaur", "Books", "Key", "Phone", "Bagel"]) from _call_memory_game
    return

default minigame.saved_shuffles = dict()
default minigame.aspect_ratio = config.screen_width / (config.screen_height - gui.textbox_height)
default minigame.yalign = .5 * (config.screen_height - gui.textbox_height) / config.screen_height
default minigame.rows = 1
default minigame.columns = 1
default minigame.card_size = 618

label memory_game(cards=[]):

    ##### Images
    image Card_Empty:
        "Card_Empty.png"
    image Card_Back:
        "Card_Back.png"
    image Card_Alien:
        "Card_Alien.png"
    image Card_Bagel:
        "Card_Bagel.png"
    image Card_Books:
        "Card_Books.png"
    image Card_Chocolate:
        "Card_Chocolate.png"
    image Card_Dinosaur:
        "Card_Dinosaur.png"
    image Card_Donut:
        "Card_Donut.png"
    image Card_Fancy_Coffee:
        "Card_Back.png"
    image Card_Frog:
        "Card_Frog.png"
    image Card_Key:
        "Card_Key.png"
    image Card_Laptop:
        "Card_Laptop.png"
    image Card_Mushroom:
        "Card_Mushroom.png"
    image Card_Phone:
        "Card_Phone.png"
    image Card_Pretzel:
        "Card_Pretzel.png"

    python:
        cards.sort()
        shuffle_key = tuple(cards)
        minigame.rows, minigame.columns, minigame.card_size = calculate_grid_size(len(cards)*minigame.cards_per_turn)
        try:
            cards_list = minigame.saved_shuffles[shuffle_key]
        except KeyError:
            cards = ["Card_" + card for card in cards]
            values_list = cards * minigame.cards_per_turn
            values_list += ["Card_Empty"] * ((minigame.rows * minigame.columns) - len(values_list))
            values_list = renpy.random.sample(values_list, len(values_list))
            cards_list = [{"c_number":i, "c_value": card, "c_chosen":False} for i, card in enumerate(values_list)]
            minigame.saved_shuffles[shuffle_key] = cards_list

    # Shows the game screen
    show screen memo_scr

    # The game loop
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []

        # Let's set the amount of cards that should be opened each turn (all of them should match to win)
        $ turns_left = 2

        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop

        # To prevent further clicking befor chosen cards will be processed
        $ can_click = False
        # If not all the opened cards are matched, will turn them face down after pause
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause (1.0, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False

        # If cards are matched, will check if player has opened all the cards
        else:
            $ renpy.pause (1.0, hard = True)
            python:

                # Let's remove opened cards from game field
                # But if you prefere to let them stay - just comment out next 2 lines
                # for i in range (0, len(turned_cards_numbers) ):
                #     cards_list[turned_cards_numbers[i]]["c_value"] = Null()


                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("memo_game_loop")
                renpy.jump ("memo_game_win")

        jump memo_game_loop

label memo_game_lose:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (0.1, hard = True)
    "You lose! Try again."
    jump memory_game

label memo_game_win:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (0.1, hard = True)
    "You win!"
    return

init python:
    def calculate_grid_size(numCards):
        rowCap = math.ceil(math.sqrt(numCards))
        bestRatio = numCards
        bestRows = 1
        for rows in range(2, rowCap):
            ratio = numCards / rows
            if abs(minigame.aspect_ratio - ratio) < abs(minigame.aspect_ratio - bestRatio):
                bestRatio = ratio
                bestRows = rows

        bestColumns = math.ceil(numCards / bestRows)
        usableHeight = config.screen_height - gui.textbox_height
        cardSize = int(min((config.screen_width / bestColumns), (usableHeight / bestRows)))
        return bestRows, bestColumns, cardSize
