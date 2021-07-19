# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character(_("Peyton"), color="BF93F2", image="peyton")
define r = Character(_("Rain"), color="E19E75", image="rain")
define f = Character(_("Farah"), color="59A4D6", image="farah")
define a0 = Character(_("Alien"), color="FFFFFF", image="alien")
define a = Character(_("Alex"), color="FFFFFF", image="alien")

define d = Character("Programmer Pooch", image="dog_coding.jpg")

default inventory = dict()
default knowledgeBase = dict()

default schedule.rawTime = 497
default schedule.clock_time = "08:17 AM"

default inv.charge = False
default inv.has_key = False
default knows_key_location = False
default flag.saw_ufo_news = False

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
label start_of_loop:
    scene bg bedroom

    $ restart_loop()

    "A bright light wakes you up. For half a second, you’re disoriented. {w=.5}"
    extend "You were having a very realistic dream. Then your surroundings sink in. {nw}"
    extend "All cool, just your room. {nw}"
    extend "The sun is stabbing through a gap in the curtains and poking you in the face. {nw}"
    extend "Your alarm clock tells you it’s August 1st, [schedule.clock_time]. {nw}"
    show screen clock_screen()
    extend "When did you go to bed last night? "
    extend "You don’t remember, but you do remember agreeing to have coffee with Farah this morning."

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

    show rain neutral:
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

    jump ending2

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
    $ flag.saw_ufo_news = True
    s "-ve heard stories about UFOs before, and nothing has ever come of it. What makes this time any different?"
    b "The amount of people that have witnessed it, and the photos! You can’t deny those photos. These people took the photos of before and after and one minute those things were there, and the next they weren’t."
    s "It could be any number of things, a light flare on the camera or a shadow from anything that’s nearby."
    b "We’ve already ruled out all of those possibilities, our team has gone out there and tried every trick in the book to see if they can recreate these photos and nothing that they tried worked. We could have seen an actual UFO! Think of all the possibilities that could-{nw}"

    "You’re on The UFOrum before the segment is even over. The news segment has drawn a few new members to the forum, who are hotly debating the correct pronunciation of “UFOrum”. You’d been seeing the same witnesses and pictures pop up, of course, but official news outlets don’t usually take these things that seriously. The forum had agreed that this recent evidence was overwhelming, but you had to admit that even the most cautious among you had been disappointed by false hope before. Still, this seemed more than a slow news day to you. You’re neck-deep in the latest thread and have just reported a rude comment about the red-headed newscaster to the moderators {nw}"
    $ add_minutes(60)
    extend "when you realise a lot of time has passed. Whoops. You were supposed to meet Farah for lunch. Time to go."
    jump cafe

label cafe:
    scene bg cafe
    $ add_minutes(10)
    "Upon entering the cafe the first thing you notice is the smell of the coffee beans. It’s such a relaxing smell, with an undertone of pastries and other sweets. The cafe has a lot of earth tones with soft lighting and a large landscape painting on the back wall to bring a relaxing atmosphere to it. It’s mostly quiet, a few other patrons are talking and you can hear the blender mixing some sort of icy drink."
    "Farah waves at you from their seat. {nw}"
    show farah neutral
    extend "They’ve picked out a nice table by the window and are already cradling a huge mug of a hot drink you would not hesitate to bet is decaffeinated. You indicate nonverbally that you’ll grab your standard chai latte before you join them. You avoid the croissants - this place has not yet realised that there is such a thing as too flakey - but you go for a sandwich and quickly join your friend."

label talk_it_out_later:

    scene bg park
    "The park is much like any other outdoor area. It has a path that loops around the side of a lake with a scattering of trees and a singular bench overlooking the small lake. {nw}"

    if not flag.saw_ufo_news:

        extend "It’s unassuming and that’s why you like it. Its utter blandness seems to have repelled all other pedestrians today, so the single bench is all yours. "

        "You take a moment to reflect. Sometimes it seems like Rain’s outbursts come out of nowhere, but you know she has a habit of cropping up frustrations. She avoids confrontations until something finally breaks the dam. Exploding over one problem isn’t the way to go about it, though."

        menu:
            "What do you do next?"

            "I’ll let Rain cool off a bit.":
                jump ending3
            "We need to talk this out properly.":
                jump ending2

    else:

        scene bg park ufo with dissolve
        extend "It’s unassuming, but with a double take you realize… wait, is that a UFO?! So the papers weren’t lying! It’s unlike any UFO you’ve ever seen, the movies don’t do it justice. You could have sworn it was almost camouflaged in with everything else, and that if you hadn't taken a second look you might have completely missed it. As you circle it slowly, you notice an open hatch."

        menu:
            "What do you do?"

            "This is too much. I did not see this.":
                jump ending3
            "I get in there!":
                pass

    scene bg ufo interior
    "You’re wary as you peer inside of the UFO. You’re not sure what to expect, but you’ve seen enough horror movies to get a few ideas. From the looks of it, the walls are lined with screens, buttons, and keyboards and something that almost comically looks like a video game joystick. {nw}"
    show alien neutral with dissolve
    extend "And is that a real alien?!"

    # conversation between player character and alien. the aliens are shocked to discover their camouflage has failed, but don’t hesitate to share the truth with the player, because they plan to wipe the PC’s mind and restart the loop anyway. the aliens just want to distract the player character long enough to knock them out and restart the loop, but the player character can also try to convince the alien that this is immoral or that they’ve learned their lesson (whichever you prefer). this conversation can end in two ways.
    #
    # either: the aliens aren’t convinced. (END 4)
    # or: the player character convinces the alien. (END 1)

    a0 "Excuse me. You shouldn’t be here. How did you get here? What are you doing?"

    menu:
        "I could ask you the same questions.":
            jump alien_talk_a
        "The door was open. I thought I’d take a look.":
            jump narration_b

label alien_talk_a:
    "The alien seems… nervous? Angry? Insulted? It’s tough to tell. The helmet’s in the way and you have no idea if your human interpretations of facial expressions apply to this alien. That thought makes a nervous giggle burst up inside of you. An alien!"

    a0 "You can call me Alex. {nw}"
    a "You can call me Alex. This is my ship. I am here to observe the social interactions between the people of this town to see if humans are capable of conflict resolution. Your presence is harming the accuracy of our data. Please follow me. I will take you home."

    menu:
        "Alright, I don’t want any trouble.":
            jump alien_talk_b_1_2
        "Wait, you’re experimenting on us? That’s so cliché.":
            pass

    a "Do not insult that which you do not understand. We are doing important work."

    menu:
        "Okay, I’m getting bad vibes here. I’ll leave.":
            jump narration_2
        "You’re right, I don’t understand. Explain it to me.":
            jump alex_2

label narration_2:
    "The alien looks relieved, but again, you can’t be 100% sure. The only thing you’re certain of is that Alex definitely doesn’t want you to be here. Those suspicions are immediately confirmed when you notice another alien sneak up behind you. A second later, you’re no longer worried at all. Why were you here again? You don’t remember."
    jump restart_loop

label alex_2:
    a "We are here to see if your planet is ready to join our galactic federation of planets. You have been chosen as a test subject. We are observing your ability to peacefully resolve a conflict. When you fail, wipe your memory and make you try again."

    menu:
        "That seems like an ill-conceived experiment doomed to fail.":
            jump alex_a3
        "Wait, you wipe my memory? Have I been here before?":
            jump narration_a3

label alex_a3:
    a "That would be a hurtful statement if I were sensitive to human emotions. Why would you say such a thing?"

    menu:
        "Your experiment is cruel and inhumane!":
            jump ending4
        "I can’t learn and grow if you wipe my memory!":
            jump narration_a4

label narration_a4:
    "Alex contemplates your words. As the alien considers your argument, you look around to see if anyone is trying to sneak up behind you to wipe your mind. Another alien catches your eye, but it doesn’t look like you’re about to get zapped with some kind of mind-wiping device."

    a "We did not consider this perspective. Your logic is sound. We will release you. Do not make us regret it. Go out and grow."
    jump ending1

label narration_b:
    "The alien seems calmed by your willingness to answer questions. You can’t be certain, though. The facial expressions seem similar to yours, but this is an alien."

    a "Of course. Curiosity is only natural. You can call me Alex. Would you like a tour?"

    menu:
        "Yes, please!":
            jump narration_B1
        "Wait, I thought you said I shouldn’t be here?":
            jump alex_b2

label narration_B1:
    "A wall slides away to reveal a door. Alex guides you through a smooth hallway. You wonder what they use for electricity. The walls are humming and you can smell a scent you can only describe as energetic. You are led into a small, warmly lit room where Alex invites you to sit down. "

    a "Just wait here a moment, Payton. I will take care of you."

label alien_talk_b_1_2:
    "Wait, did you tell Alex your name? You don’t remember. You don’t remember."
    jump restart_loop

label restart_loop:
    # play loop restart music
    jump start_of_loop

label ending1:
    scene bg park ufo with fade
    "You stumble out of the UFO on shaky legs. "
    "You like to think you have an open mind when it comes to things the world isn’t ready to believe, but this has surpassed all expectations. "
    scene bg park with dissolve
    "You’re not ready to think about the implications yet, but you are ready to make some dinner and talk about the argument with Rain."
    scene bg livingroom
    show rain neutral at right
    show peyton neutral at left
    with dissolve
    "When she suggests putting on an episode of X-Files in the background while you eat, you suggest Jurassic Park instead."
    show rain happy
    show peyton happy
    "Over dinner and a movie you both know by heart, you talk things out in a non-confrontational way. "
    "You promise to take more notes so you don’t forget as much, while Rain promises to try harder to address frustrations before they become insurmountable problems. "

    scene bg bedroom with dissolve
    "You go to bed satisfied and exhilarated. "
    "Aliens?! "
    "Right now, though, you’re just happy you didn’t have to go to bed angry. {w}You’ll deal with the world-shattering implications of this discovery tomorrow."
    scene black with fade
    "{b}ENDING 1{/b}"
    return

label ending2:
    r happy "Thank you for that. "
    show rain neutral eyecontact
    extend "I have to go now, but it's a weight off my mind."
    show rain happy
    hide rain with dissolve
    "{b}ENDING 2{/b}"
    return

label ending3:
    pass

label ending4:
    pass

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
    show farah neutral at right:
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
    jump memory_game

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
