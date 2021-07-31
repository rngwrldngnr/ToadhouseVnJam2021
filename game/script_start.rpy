# This starts at 0, and gets incremented each time the game loops back to the beginning.
default loop_count = 0

default flag.is_phone_charged = False
default flag.found_bedroom_key = False
default flag.has_flatmate_left = False
default flag.visited_park_earlier = False
default flag.late_for_cafe = False
default flag.saw_ufo_news = False

default minigame.cards_per_turn = 2

# The game starts here.
label start:

    stop music fadeout 1.0

    # Uncomment this to quickly jump to certain parts of the game.
    # Don't forget to comment the line back before committing!
    #jump start_debug

label start_of_loop:
    $ flag.has_flatmate_left = False

    $ restart_loop()

    # Note: this music track is played as a sound so that it doesn't loop.
    play sound "./audio/Toadhouse__ReplayRespawn__00.mp3"

    jump bedroom_start

label start_debug:
    menu:
        "Normal start":
            jump start_of_loop

        "Call Rain":
            $ loop_count = 1
            $ flag.is_phone_charged = True
            jump call_rain

        "UFO in park":
            $ flag.saw_ufo_news = True
            jump walk_in_the_park

        "UFO start":
            jump ufo_start

        "Rain talk":
            jump livingroom

        "End 1":
            jump end_1
