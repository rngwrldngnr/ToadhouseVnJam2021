default key_look_count = 0

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
    "You get up and grab your phone"
    "but not without knocking over one of the many tiny frog statues your family has gifted you since you mentioned to your mum that you thought frogs were neat once ten years ago."
    "Your phone is not plugged in. The battery is dead."
    "You’re supposed to meet your friend soon."

    menu:
        "Lay around waiting for it to charge.":
            jump lay_around_waiting_charge
        "Go get breakfast.":
            jump explore_your_room

label lay_around_waiting_charge:
    "You get back in bed and spend another 45 minutes staring at your dusty ceiling fan."
    $ add_minutes(45)
    "You should really buy one of those dusters on a stick."
    "As you lie there, the front door slams, and some of the dust comes fluttering down."
    $ has_flatmate_left = True
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
    "There’s a small potted plant on the dresser."
    "It looks a little sad. You should remember to water it more often."
    "Right next to it is a small frog statue."
    "On the nightstand is a newspaper with the headline “possible UFO?”"
    "A nice addition to your collection."
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
            call check_dresser

        "The posters.":
            call check_posters from _call_check_posters

        "The small potted plant.":
            call check_potted_plant

        "The outside of the bedroom." if inv.has_key:
            $ add_minutes(1)
            jump livingroom

    jump check_bedroom

label check_bedside_table:
    $ add_minutes(2)
    "You find some hard candies and a stack of faded newspaper clippings about UFOs..."
    if is_key_here(1):
        $ inv.has_key = True
        $ knows_key_location = True
        extend " and {i}there's{/i} your room key!"
    else:
        extend " but no key."

    call bedroom_on_key_search

    return

label check_dresser:
    $ add_minutes(2)
    "You’re going to have to refold all of these clothes now..."
    if is_key_here(2):
        $ inv.has_key = True
        $ knows_key_location = True
        extend " but you’ve {i}found{/i} your room key!"
    else:
        extend " and you didn’t even find the key."

    call bedroom_on_key_search

    return

label check_posters:
    $ add_minutes(2)
    "Some lovely posters of cats and toads."
    "You check to see if the you from last night thought it was funny to tape the key behind a poster, like a hidden message in a mystery novel."
    if is_key_here(3):
        $ inv.has_key = True
        $ knows_key_location = True
        "It seems like you were tired enough to find that sort of shenanigans fun but awake enough to {i}actually do it.{/i} You found the room key!"
    else:
        "Unfortunately it seems those kinds of shenanigans were not on past-you’s mind at the time. No key!"

    call bedroom_on_key_search

    return

label check_potted_plant:
    $ add_minutes(2)
    "You lift up the pot to see if you put the key underneath, but no luck."
    "Just in case, you check inside the pot too."
    if is_key_here(4):
        $ inv.has_key = True
        $ knows_key_location = True
        "Your room key is nestled in the dirt."
    else:
        "Your room key isn’t here."

    call bedroom_on_key_search

    return

label bedroom_on_key_search:
    $ key_look_count = key_look_count + 1

    if key_look_count == 3 and not has_flatmate_left:
        "Outside your room, the front door slams. Sounds like your flatmate has left for the day."
        $ has_flatmate_left = True

    return
