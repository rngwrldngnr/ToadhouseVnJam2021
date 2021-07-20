label bedroom_start:
    scene bg bedroom

    $ restart_loop()

    # Note: this music track is played as a sound so that it doesn't loop.
    play sound "./audio/Toadhouse__ReplayRespawn__00.mp3"

    "A bright light wakes you up. For half a second, you’re disoriented."
    "You were having a very realistic dream. Then your surroundings sink in."
    "All cool, just your room."
    "The sun is stabbing through a gap in the curtains and poking you in the face."
    "Your alarm clock tells you it’s August 1st, [schedule.clock_time]."
    show screen clock_screen()
    "When did you go to bed last night?"
    "You don’t remember, but you do remember agreeing to have coffee with a friend this morning."

    menu:
        "Get up.":
            jump get_up
        "Grab your phone and catch up on social media.":
            jump grab_your_phone

label get_up:
    "You drag yourself out of bed, throw on some clothes, and take three entire steps to the door."
    "It's locked."
    "They key is not in the lock."
    "Weird, but not a cause for immediate panic. Probably."
    "Each bedroom got its own lock when this building was turned into a flatshare and you lock the door sometimes when you don’t want to be disturbed."
    "Maybe you did it on autopilot last night."
    "Better find that key."
    jump explore_your_room

label grab_your_phone:
    $ add_minutes(1)
    "You get up and grab your phone, {w=.5}"
    extend "but not without knocking over one of the many tiny frog statues your family has gifted you since you mentioned to your mum that you thought frogs were neat once ten years ago."
    "Your phone is not plugged in. The battery is dead. {nw}"
    extend "You’re supposed to meet your friend soon."

    menu:
        "Lay around waiting for it to charge.":
            jump lay_around_waiting_charge
        "Go get breakfast.":
            jump explore_your_room

label lay_around_waiting_charge:
    "You get back in bed and spend another 45 minutes staring at your dusty ceiling fan."
    $ add_minutes(45)
    "You should really buy one of those dusters on a stick."
    "Your phone isn’t fully charged, but it will be useful in an emergency."
    "If you don’t leave now, you will definitely be late. Time to get up."
    $ inv.charge = True
    jump explore_your_room

# Note: -1 means the location will be set to the last place checked on the first loop.
default loops.key_location = -1

label explore_your_room:
    $ add_minutes(1)
    "You take a good look around the room."
    "There are the cat in space and frog with the toadstool posters that you thought would add a little bit of character to your room."
    "The sheets are lavender with a purple duvet to match."
    "On top of the dresser is your house key!"
    extend " You were afraid that you had lost it, but it’s right next to a small frog statue."

    "On the nightstand is a newspaper with the headline “possible UFO?”"
    extend "A  nice addition to your collection."
    "Candy and wrappers are scattered over the top."
    "You’ll get to throwing those out later. But where is the key?"

#    if loops.key_location == 0:
#        show dog_coding at top
#        menu dev_choose_how_to_find_key:
#            ProgrammerPooch "You can test the different ways we've talke about finding the key."
#
#            "Randomly placed key (same position in loops)":
#                $ loops.key_location = renpy.random.randint(1,4)
#            "Key in whatever place is checked last (same position in loops)":
#                $ loops.key_location = -1
#            "Put the key in the bedside table (for testing routes)":
#                $ loops.key_location = 1
#            # "Key must be found with minigame (leave through window until you win)":
#        hide dog_coding

    $ key_location_set = set()
    menu check_bedroom:
        set key_location_set
        "Time to take a closer look at..."

#        "Your memory of last night (doesn't work yet)": #if loops.key_location == 5:
#            call memory_game(["Key", "Alien", "Phone"])

        "The bedside table.":
            call check_bedside_table from _call_check_bedside_table

        "The dresser drawers.":
            call check_drawers from _call_check_drawers

        "The posters.":
            call check_posters from _call_check_posters

        "The key on the dresser.":
            call check_dresser from _call_check_dresser

        "The outside of the bedroom." if inv.has_key:
            $ add_minutes(1)
            jump livingroom

    jump check_bedroom

label check_bedside_table:
    $ add_minutes(2)
    "You find some hard candies {nw}"
    extend "and a stack of faded newspaper clippings about UFOs, {nw}"
    if is_key_here(1):
        $ inv.has_key = True
        $ knows_key_location = True
        extend "and {i}there's{/i} your room key!"
    else:
        extend "but no key."

    return

label check_drawers:
    $ add_minutes(2)
    "You’re going to have to refold all of these clothes now, {nw}"
    if is_key_here(2):
        $ inv.has_key = True
        $ knows_key_location = True
        extend "but you’ve {i}found{/i} your room key!"
    else:
        extend "and you didn’t even find the key."

    return

label check_posters:
    $ add_minutes(2)
    "Some lovely posters of cats and toads."
    "You check to see if the you from last night thought it was funny to tape the key behind a poster, like a hidden message in a mystery novel, "
    if is_key_here(3):
        $ inv.has_key = True
        $ knows_key_location = True
        extend "and it seems like you were tired enough to find that sort {nw}"
        extend "of shenanigans fun but awake enough to {i}actually do it.{/i} {p}"
        extend "You found the room key!"
    else:
        extend "but unfortunately it seems those kinds of shenanigans were {nw}"
        extend "not on past-you’s mind at the time. "
        extend "No key!"

    return

label check_dresser:
    $ add_minutes(2)
    "That’s your house key. That’ll be useful once you reach the front door. {nw}"
    if is_key_here(4):
        $ inv.has_key = True
        $ knows_key_location = True
        extend "Despite it not being the normal place you keep it, {nw}"
        extend "your {i}room key{/i} is on this keyring! {w}You slip it off and pocket both."
    else:
        extend "Not your room key."

    return
