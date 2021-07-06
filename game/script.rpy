# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Commit test pls ignore - Cyn

define p = Character("Peyton Protagonist")
define r = Character("Rain Roommate")
define a = Character("Alex Alien")
define f = Character("Farah Friendo")

default inventory = dict()
default knowledgeBase = dict()
default schedule.rawTime = 497
default schedule.clockTime = "08:17 AM"
default inv.charge = False
default inv.has_key = False
default knows_key_location = False

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
        hour = 60
        clockMax = 12
        halfDay = hour * clockMax
        if calcTime >= halfDay:
            calcTime - halfDay
            letters = "PM"
        else:
            letters = "AM"
        hours = calcTime / hour
        minutes = calcTime % hour
        if hours == 0:
            hours = clockMax
        schedule.clockTime = "{0:02d}:{1:02d} {2}".format(hours, minutes, letters)

    def add_minutes(numMinutes):
        schedule.rawTime += numMinutes
        update_clock_time()

    def before(clockTimeToCheck):
        hours, minutes, letters = re.split("[: ]", clockTimeToCheck)
        calcTime = (int(hours) * 60) + int(minutes)
        if letters.upper() == "PM":
            calcTime += 12 * 60
        return schedule.rawTime < calcTime

screen clock_screen():
    frame:
        xalign 0 yalign 0
        text "[schedule.clockTime]":
            color "ff0000"
            size 36

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    $ restart_loop()

    "Feel like I barely got any sleep, but it's definitely morning now."

    "Guess I should go and see what the damage is."

    "..."

    "The door's locked."

    "The current time is [schedule.clockTime]."

    show screen clock_screen()

    $ key_location_set = set()

label check_bedroom:

    menu menu_bedroom:
        set key_location_set
        "Where should I look?"

        "Check the bedding" if not knows_key_location:
            $ add_minutes(3)
            "Nothing in the sheets or under the pillow.{w=1.5} Not even some change from the key fairy."
            jump check_bedroom

        "Check under the bed" if not knows_key_location:
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
            jump kitchen

# Sections to jump to from search menu
label check_nightstand:
    $ add_minutes(1)
    p "I found my phone. Unfortunately the battery is dead. I was awake enough to attach it to the charger, but not awake enough to actuall plug the charger into the wall."

    menu:
        "Charge phone":
            $ inv.charge = True
            $ add_minutes(20)
            p "Okay my phone is charged."
            jump menu_bedroom

        "Not right now":
            jump menu_bedroom

label check_closet:
    "The closet is messy, with a piles of dirty close and full bins of unsorted laundry."
    $ add_minutes(5)
    "It takes several minutes to dig through everything, until"
    p "{b}Here{/b}'s the key. Now I can leave. Or I could keep looking around I guess."
    $ inv.has_key = True
    $ knows_key_location = True
    jump menu_bedroom

label kitchen:
    scene bg kitchen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    if before("8:30 AM"):
        show Rain Roommate angry
        r "We need to talk!"
        return

    else:
        " Rain's gone, but there's a note"
        show note
        r "How could you have done this?! Fix it and apologize or one of us is moving out!"
        "What could I have done to upset Rain so badly?"
        "And why do I feel so... woozy?"
        jump start


    # This ends the game.

    return
