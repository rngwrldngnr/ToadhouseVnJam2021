# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character(_("Protagonist"), color="FFC8C8")
define r = Character(_("Roommate"), color="C8FFC8")
define a = Character(_("Alien"), color="FFFFFF")
define f = Character(_("Friend"), color="C8C8FF")

default inventory = dict()
default knowledgeBase = dict()
default schedule.rawTime = 497
default schedule.clockTime = "08:17 AM"
default inv.charge = False
default inv.has_key = False
default knows_key_location = False

default calc.hour = 60
default calc.clockMax = 12
default calc.halfDay = calc.hour * calc.clockMax

default test.charZoom = .5
default test.level = 1.0

init python:
    import re

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
        schedule.clockTime = "{0:02d}:{1:02d} {2}".format(hours, minutes, letters)

    def add_minutes(numMinutes):
        schedule.rawTime += numMinutes
        update_clock_time()

    def before(clockTimeToCheck):
        hours, minutes, letters = re.split("[: ]", clockTimeToCheck)
        calcTime = (int(hours) * 60) + int(minutes)
        if letters.upper() == "PM":
            calcTime += calc.halfDay
        return schedule.rawTime < calcTime

screen clock_screen():
    frame:
        xalign 0 yalign 0
        text "[schedule.clockTime]":
            color "ff0000"
            font "./gui/fonts/CourierPrime-Regular.ttf"
            size 2 * gui.text_size

# The game starts here.
label start:

    # stop music fadeout 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    $ restart_loop()

    "Feel like I barely got any sleep, but it's definitely morning now."

    "Guess I should go and see what the damage is."

    "..."

    "The door's locked."

    show screen clock_screen()
    "The current time is [schedule.clockTime]."

    $ key_location_set = set()

label check_bedroom:

    menu menu_bedroom:
        set key_location_set
        "Where should I look?"

        "Check the bedding":
            $ add_minutes(4)
            "Nothing in the sheets or under the pillow.{w=1.5} Not even some change from the key fairy."
            jump check_bedroom

        "Check under the bed":
            $ add_minutes(2)
            "Wow! So many childhod memories! {w=1.5}Nothing of material interest though."
            jump check_bedroom

        "Check the nightstand":
            jump check_nightstand

        "Check inside the dresser" if not knows_key_location:
            $ add_minutes(5)
            "A thorough check through the contents finds nothing of note."
            jump check_bedroom

        "Check the closet":
            jump check_closet

        "Check inside the lampshade" if not knows_key_location:
            $ add_minutes(1)
            p "This bit's actually quite clever, I've been able to hide keys by looping the ring around... Nope, nothing here either."
            jump check_bedroom

        "Check your pockets" if not knows_key_location:
            $ add_minutes(1)
            "It's always in the last place you think to look. {w=1.5}Not this time though."
            jump check_bedroom

        "Leave the room" if inv.has_key:
            jump home


# Sections to jump to from search menu
label check_nightstand:
    $ add_minutes(1)
    p "I found my phone. Unfortunately the battery is dead. I was awake enough to attach it to the charger, but not awake enough to actually plug the charger into the wall."

    menu:
        "Charge phone":
            $ inv.charge = True
            $ add_minutes(20)
            p "Okay my phone is charged."

        "Not right now":
            pass

    jump check_bedroom

label check_closet:
    "The closet is messy, with a piles of dirty close and full bins of unsorted laundry."
    $ add_minutes(5)
    "It takes several minutes to dig through everything, until"
    p "{b}Here{/b}'s the key. Now I can leave. Or I could keep looking around I guess."
    $ inv.has_key = True
    $ knows_key_location = True
    jump menu_bedroom

label home:
    scene bg home

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    if not before("8:30 AM"):
        "_ROOMMATE_'s gone, but there's a note"
        show note
        r "How could you have done this?! Fix it and apologize or one of us is moving out!"
        "What could I have done to upset _ROOMMATE_ so badly?"
        "And why do I feel so... woozy?"
        jump start
    else:
        show roommate full_body at center:
            zoom .5
        r "We need to talk!"


    # This ends the game.

    scene bg coffee shop

    "This scene is just for testing sizing and visible portion for the character art"
label change:

    show player_character full_body at left:
        zoom test.charZoom
        ypos test.level
    show roommate full_body at center:
        zoom test.charZoom
        ypos test.level
    show friend full_body at right:
        zoom test.charZoom
        ypos test.level

    "These are currently half scaled. You can raise or lower them, and make the bigger or smaller."

    menu:
        "Higher":
            $ test.level -= .1
        "Lower":
            $ test.level += .1
        "Bigger":
            $ test.charZoom += .05
        "Smaller":
            $ test.charZoom -= .05
        "Exit":
            jump end

    jump change

label end:
    return
