# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character(_("Peyton"), color="BF93F2", image="peyton")
define r = Character(_("Rain"), color="E19E75", image="rain")
define f = Character(_("Farah"), color="59A4D6", image="farah")
define a = Character(_("Alien"), color="FFFFFF", image="alien")

define d = Character("Programmer Pooch", image="dog_coding.jpg")

default inventory = dict()
default knowledgeBase = dict()

default schedule.rawTime = 497
default schedule.clock_time = "08:17 AM"

default inv.charge = False
default inv.has_key = False
default knows_key_location = False

default calc.hour = 60
default calc.clockMax = 12
default calc.halfDay = calc.hour * calc.clockMax

default test.charZoom = .4
default test.level = 1.0

default minigame.cards_per_turn = 2

# The game starts here.
label start:

    stop music fadeout 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    $ restart_loop()

    "A bright light wakes you up. For half a second, you’re disoriented. {w=.5}"
    extend "You were having a very realistic dream. Then your surroundings sink in. {nw}"
    extend "All cool, just your room. {nw}"
    extend "The sun is stabbing through a gap in the curtains and poking you in the face. {nw}"
    extend "Your alarm clock tells you it’s August 1st, [schedule.clock_time]. {nw}"
    show screen clock_screen()
    extend "When did you go to bed last night? "
    extend "You don’t remember, but you do remember agreeing to have coffee with a friend this morning."

    menu:
        "Get up.":
            jump explore_your_room
        "Grab your phone.":
            jump grab_your_phone

label grab_your_phone:
    $ add_minutes(1)
    "You get up and grab your phone, {w=.5}"
    extend "but not without knocking over one of the many tiny frog statues your family has gifted you since you mentioned to your mum that you thought frogs were neat once ten years ago. {nw}"
    extend "Your phone is not plugged in. The battery is dead. {nw}"
    extend "You’re supposed to meet your friend soon."

    menu:
        "Lay around waiting for it to charge":
            jump lay_around_waiting_charge
        "Go get breakfast":
            jump explore_your_room

label lay_around_waiting_charge:
    "You get back in bed and spend another 45 minutes staring at your dusty ceiling fan. {nw}"
    $ add_minutes(45)
    extend "You should really buy one of those dusters on a stick. {nw}"
    extend "Your phone is not fully charged, but it will be useful in an emergency. {nw}"
    extend "If you don’t leave now, you will definitely be late. Time to get up."
    $ inv.charge = True
    jump explore_your_room

default loops.key_location = 0

label explore_your_room:
    $ add_minutes(1)
    "You take a good look around the room. {nw}"
    extend "There are the cat in space and frog with the toadstool posters that you {nw}"
    extend "thought would add a little bit of character to your room. {nw}"
    extend "The sheets are lavender with a purple duvet to match. {nw}"
    extend "On top of the dresser is your house key! {nw}"
    extend "You were afraid that you had lost it, {nw}"
    extend "but you kept it next to one of your small frog statues to keep it safe."

    "On the nightstand behind your bed... "
    $ add_minutes(1)
    scene black
    extend "You remember passing by a newspaper stand about possible UFO sightings. {nw}"
    extend "Interested in this, you grabbed up one of the newspapers {nw}"
    scene bg bedroom
    with dissolve
    extend "and put it beside your bed to look through later. "
    extend "There's candy and candy wrappers scattered over the top, {nw}"
    extend "you'll get to throwing those out later. "
    "But where is your key?"

    if loops.key_location == 0:
        show dog_coding at top
        menu dev_choose_how_to_find_key:
            d "You can test the different ways we've talke about finding the key."

            "Randomly placed key (same position in loops)":
                $ loops.key_location = renpy.random.randint(1,4)
            "Key in whatever place is checked last (same position in loops)":
                $ loops.key_location = -1
            "Put the key in the bedside table (for testing routes)":
                $ loops.key_location = 1
            # "Key must be found with minigame (leave through window until you win)":
        hide dog_coding

    $ key_location_set = set()
    menu check_bedroom:
        set key_location_set
        "Time to take a closer look at..."

        "Your memory of last night (doesn't work yet)": #if loops.key_location == 5:
            call memory_game(["Key", "Alien", "Phone"])
        "The bedside table":
            $ add_minutes(2)
            "You find some hard candies {nw}"
            extend "and a stack of faded newspaper clippings about UFOs, {nw}"
            if is_key_here(1):
                $ inv.has_key = True
                $ knows_key_location = True
                extend "and {i}there's{/i} your room key!"
            else:
                extend "but no key."

        "The dresser drawers":
            $ add_minutes(2)
            "You're going to have to refold all of these clothes now, {nw}"
            if is_key_here(2):
                $ inv.has_key = True
                $ knows_key_location = True
                extend "but you've {i}found{/i} your room key!"
            else:
                extend "and you didn't even find the key."

        "The posters":
            $ add_minutes(2)
            "Some lovely posters of cats and toads."
            "You check to see if the you from last night thought it was {nw}"
            extend "funny to tape the key behind a poster, {w=.5}"
            extend "like a hidden message in a mystery novel, {w}"
            if is_key_here(3):
                $ inv.has_key = True
                $ knows_key_location = True
                extend "and it seems like you were tired enough to find that sort {nw}"
                extend "of shenanigans fun but awake enough to {i}actually do it.{/i} {p}"
                extend "You found the room key!"
            else:
                extend "but unfortunately it seems those kinds of shenanigans were {nw}"
                extend "not on past-you’s mind at the time. {p}"
                extend "No key!"

        "The key on the dresser":
            $ add_minutes(2)
            "That's your house key. It'll be useful once you reach the front door. {nw}"
            if is_key_here(4):
                $ inv.has_key = True
                $ knows_key_location = True
                extend "Despite it not being the normal place you keep it, {nw}"
                extend "your {i}room key{/i} is on this keyring! {w}You slip it off and pocket both."
            else:
                extend "You don't keep your room key on this keyring."

        "The outside of the bedroom" if inv.has_key:
            $ add_minutes(1)
            jump livingroom

    jump check_bedroom

label livingroom:
    scene bg livingroom

    if before("8:23 AM"):
        jump livingroom_morning_talkn
    else:
        pass

    "You rush into the living room to grab your stuff. You don’t see your flatmate, "
    extend "but you can still smell the fried eggs they always have for breakfast. "
    extend "They’ve left their dirty dishes on the counter, which is unlike them. "
    extend "A closer look at the counter reveals a note from Rain. "
    "\“We need to talk.\" {w}Oh boy. "
    "You’ll have to worry about that later, though. Time to meet up with Farah."
    jump cafe


label livingroom_morning_talkn:
    "You rush into the living room to grab your stuff. {nw}"
    extend "This place brings many memories since the years that you’ve lived here. {nw}"
    extend "It’s one of the cosiest areas in your home, {nw}"
    extend "and you’ve often fallen asleep on that couch while watching movies. {nw}"
    extend "You’re surprised the Monstera plant is still alive, {nw}"
    extend "because you don’t have much of a green thumb, but it seems to be doing well. {nw}"
    extend "Oh, you’ve left some coffee cups on the table. You should take care of those later."

    show rain full_body:
        zoom .8
        ypos 1.45
    "The TV is on, but the volume is too low to make out what the newsreaders are saying. {nw}"
    extend "As you’re patting your pockets to check you have your wallet and keys, {nw}"
    extend "your flatmate walks past with an empty plate. {nw}"
    extend "You can still smell the fried eggs they always have for breakfast, {nw}"
    extend "and it’s making you peckish. Your flatmate usually has a permanent case of resting happy face, {nw}"
    show rain unhappy
    extend "but right now they don’t look cheerful."

    menu:
        "Right now they don't look cheerful"

        "These conversations shouldn't be rushed. Better take your time to talk tonight.":
            "You seek a moment of eye contact with your flatmate to give them a reassuring smile and nod. {nw}"
            show rain unhappy eyecontact
            extend "Your flawless comforting technique is not very effective, {nw}"
            extend "but you don't have time to talk right now. You are meeting Farah at the café."
            jump cafe
        "Hey, Rain. Are you okay?":
            pass

    r unhappy eyecontact "You mean you really don't know what's bothering me?"
    menu:
        "If I did I wouldn't be asking.":
            jump livingroom_morning_talk_rude
        "I really have no idea, is it something that I can help with?":
            jump livingroom_morning_talk_polite

label livingroom_morning_talk_rude:
    r annoyed "You're being awfully rude for what you did last night. {nw}"
    extend "That's not cool Peyton."

    menu:
        r "That's not cool Peyton."
        "What do you mean what I did last night? I don’t remember doing anything!":
            pass
        "I really have no idea what you’re talking about, Rain.":
            pass

    r angry "Stop joking around. {w=1.5}"
    extend "I have to go right now, I'm going to be late for my shift. {nw}"
    extend "We can talk about it later."
    jump cafe

label livingroom_morning_talk_polite:
    r unhappy eyecontact "Last night you borrowed my laptop without asking me about it. {w=.5}"
    extend "I normally don’t mind but I couldn’t find it this morning, {nw}"
    extend "and I thought I left it at the café until I found it. I was really worried!"

    menu:
        "I was really worried!"

        " I don’t remember doing that at all. I must have been more tired than I thought, I’m sorry. I’ll remember to ask you before borrowing anything of yours again.":
            jump ending2
        "Are you sure that I did that? Maybe you could have misplaced it before you left.":
            pass

    r annoyed "I was gone all day yesterday, I couldn’t have done it. When I got home last night you were already asleep, and my laptop was missing."

    menu:
        "My laptop was missing."

        "I didn’t drink last night, and I honestly don’t remember doing it. I’m sorry though, it wasn’t cool to take something of yours without asking.":
            pass
        "Maybe I was sleepwalking and took your laptop, I’m sorry. I would never take something of yours without asking.":
            pass

    jump ending 2

label ending2:
    r happy "Thank you for that. "
    show rain neutral eyecontact
    exend "I have to go now, but it's a weight off my mind."
    show rain happy
    hide rain with dissolve
    "Ending 2"
    return

label livingroom_morning_talk_unresolved:
    "Rain leaves. This is definitely a conversation to pick up again later. Then the words BREAKING NEWS and its accompanying sting on the TV do their job of catching your attention. Your very bored-looking local newsreader is joined by a frazzled colleague. There’s a blurry picture on the screen that’s very similar to the one in the newspaper you picked up yesterday."

    menu:
        "You're late. Leave to meet Farah.":
            jump cafe
        "Turn up the volume to catch what they're saying":
            jump livingroom_ufo_news

define s = Character(_("Skeptical Anchor"))
define b = Character(_("Believer Anchor"))

label livingroom_ufo_news:
    s "-ve heard stories about UFOs before, and nothing has ever come of it. What makes this time any different?"
    b "The amount of people that have witnessed it, and the photos! You can’t deny those photos. These people took the photos of before and after and one minute those things were there, and the next they weren’t."
    s "It could be any number of things, a light flare on the camera or a shadow from anything that’s nearby."
    b "We’ve already ruled out all of those possibilities, our team has gone out there and tried every trick in the book to see if they can recreate these photos and nothing that they tried worked. We could have seen an actual UFO! Think of all the possibilities that could-{nw}"

    "You’re on The UFOrum before the segment is even over. The news segment has drawn a few new members to the forum, who are hotly debating the correct pronunciation of “UFOrum”. You’d been seeing the same witnesses and pictures pop up, of course, but official news outlets don’t usually take these things that seriously. The forum had agreed that this recent evidence was overwhelming, but you had to admit that even the most cautious among you had been disappointed by false hope before. Still, this seemed more than a slow news day to you. You’re neck-deep in the latest thread and have just reported a rude comment about the red-headed newscaster to the moderators {nw}"
    add_minutes(60)
    extend "when you realise a lot of time has passed. Whoops. You were supposed to meet Farah for lunch. Time to go."
    jump cafe

label cafe:
    scene bg cafe
    add_minutes(10)
    "Upon entering the cafe the first thing you notice is the smell of the coffee beans. It’s such a relaxing smell, with an undertone of pastries and other sweets. The cafe has a lot of earth tones with soft lighting and a large landscape painting on the back wall to bring a relaxing atmosphere to it. It’s mostly quiet, a few other patrons are talking and you can hear the blender mixing some sort of icy drink."
    "Farah waves at you from their seat. {nw}"
    show farah neutral
    extend "They’ve picked out a nice table by the window and are already cradling a huge mug of a hot drink you would not hesitate to bet is decaffeinated. You indicate nonverbally that you’ll grab your standard chai latte before you join them. You avoid the croissants - this place has not yet realised that there is such a thing as too flakey - but you go for a sandwich and quickly join your friend."



label test_cafe:
    scene bg cafe

    "This scene is just for testing sizing and visible portion for the character art"
label change:

    show peyton neutral at left:
        zoom test.charZoom
        ypos test.level
    show rain neutral at center:
        zoom test.charZoom
        ypos test.level
    show friend neutral at right:
        zoom test.charZoom
        ypos test.level

    "These are currently [test.charZoom] scale. You can raise or lower them, and make the bigger or smaller."

    menu:
        "Higher":
            $ test.level -= .1
        "Lower":
            $ test.level += .1
        "Bigger":
            $ test.charZoom += .04
        "Smaller":
            $ test.charZoom -= .04
        "Exit":
            jump end

    jump change

label end:
    call memory_game(["Alien", "Dinosaur", "Books", "Key", "Phone", "Bagel"])
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
    jump memoria_game

label memo_game_win:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (0.1, hard = True)
    "You win!"
    return

init python:
    import math

    def restart_loop():
        set_time(497)
        inv.charge = False
        inv.has_key = False

    def set_time(minutesPastMidnight):
        schedule.rawTime = minutesPastMidnight
        update_clock_time()

    def update_clock_time():
        calcTime = schedule.rawTime
        if calcTime >= calc.halfDay:
            calcTime - calc.halfDay
            letters = "PM"
        else:
            letters = "AM"
        hours = calcTime // calc.hour
        minutes = calcTime % calc.hour
        if hours == 0:
            hours = calc.clockMax
        schedule.clock_time = "{0:02d}:{1:02d} {2}".format(hours, minutes, letters)

    def add_minutes(numMinutes):
        schedule.rawTime += numMinutes
        update_clock_time()

    def before(clockTimeToCheck):
        hours, minutes, letters = renpy.re.split("[: ]", clockTimeToCheck)
        calcTime = (int(hours) * 60) + int(minutes)
        if letters.upper() == "PM":
            calcTime += calc.halfDay
        return schedule.rawTime < calcTime

    def is_key_here(location):
        if loops.key_location == location:
            return True
        if loops.key_location == -1 and len(key_location_set) == 4:
            loops.key_location = location
            return True
        return False

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
