label end_1:
    scene bg park ufo with fade

    "You stumble out of the UFO on shaky legs."
    "You like to think you have an open mind when it comes to things the world isn’t ready to believe, but this has surpassed all expectations."

    scene bg park with dissolve

    "You’re not ready to think about the implications yet, but you are ready to go home, make some dinner, and talk about the argument with Rain."

    scene bg livingroom
    show rain neutral right at right
    show payton neutral left at left
    with dissolve

    "When she suggests putting on an episode of X-Files in the background while you eat, you suggest Jurassic Park instead."

    show rain smile right
    show payton smile left

    "Over dinner and a movie you both know by heart, you talk things out in a non-confrontational way."
    "You promise to take more notes so you don’t forget as much, while Rain promises to try harder to address frustrations before they become insurmountable problems."

    scene bg bedroom with dissolve

    "You go to bed satisfied and exhilarated."
    "Aliens?!"
    "Right now, though, you’re just happy you didn’t have to go to bed angry."

    play music "./audio/Toadhouse__OpenTheme_02.mp3"

    "You’ll deal with the world-shattering implications of this discovery tomorrow."

    scene black with fade

    jump exit_time_loop

label end_2:
    scene black

    "Thankfully, the rest of your day is uneventful."
    "You finally get some long-postponed chores done, but the fight still lingers in the back of your mind."

    scene bg livingroom
    show rain smile right at right
    show payton smile left at left
    with dissolve

    "Later, when your flatmate gets back from work, you make dinner, put on Jurassic Park in the background, and properly talk things out."

    scene bg bedroom with dissolve

    "You go to bed glad you took the time to talk."
    "You can only imagine how this could have escalated. Today would have ended very differently."
    "Still, it takes you a while to fall asleep."
    "There’s a strange humming noise outside, but you can’t see where it’s coming from."

    play music "./audio/Toadhouse__OpenTheme_02.mp3"

    "You’re too tired to deal with it now, though, so you’ll just have to see if it’s still a problem tomorrow."

    jump exit_time_loop

label end_3:
    scene black

    "You decide you need some time to clear your head, so you spend your day wandering around town and doing some long-postponed chores."

    scene bg livingroom
    show rain angry right at right
    show payton neutral left at left
    with dissolve

    "When you finally get home that evening, you immediately realise you’ve well and truly messed up this time, at least as far as Rain is concerned."
    "She’s had some time to think it over, same as you, and is clearly not ready to let this go yet."
    "Your relationship with Rain has taken a dent. If you could try again, you’d probably do things differently."

    scene bg bedroom with dissolve

    "Going to bed angry never feels great, but sometimes you need to take a moment. You’ll try again tomorrow."

    jump restart_loop

label exit_time_loop:
    jump credits_start

label restart_loop:
    # TODO: play loop restart music?
    $ loop_count = loop_count + 1
    jump start_of_loop
