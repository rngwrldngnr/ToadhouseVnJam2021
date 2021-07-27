# The script of the game goes in this file.

default inventory = dict()
default knowledgeBase = dict()

default schedule.rawTime = 497
default schedule.clock_time = "08:17 AM"

default inv.charge = False
default inv.has_key = False
default knows_key_location = False
default visited_park_earlier = False
default late_for_cafe = False
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

    # Uncomment this to quickly jump to certain parts of the game.
    # Don't forget to comment the line back before committing!
    #jump start_debug

label start_of_loop:
    jump bedroom_start

label start_debug:
    menu:
        "Normal start":
            jump start_of_loop

        "Cafe on time":
            jump cafe

        "UFO in park":
            $ flag.saw_ufo_news = True
            jump walk_in_the_park

        "Rain talk":
            jump livingroom

        "End 1":
            jump end_1
