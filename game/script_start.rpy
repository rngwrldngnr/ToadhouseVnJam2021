﻿# The script of the game goes in this file.

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
label start_of_loop:
    jump bedroom_start
