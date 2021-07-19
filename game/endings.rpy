label end_1:
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
    "You go to bed satisfied and exhilarated."
    "Aliens?!"
    "Right now, though, you’re just happy you didn’t have to go to bed angry. {w}You’ll deal with the world-shattering implications of this discovery tomorrow."
    scene black with fade
    "{b}ENDING 1{/b}"

    jump exit_time_loop

label end_2:
    scene black

    "Thankfully, the rest of your day is uneventful."
    "You finally get some long-postponed chores done, but the fight still lingers in the back of your mind."
    "Later, when your flatmate gets back from work, you make dinner, put on Jurassic Park in the background, and properly talk things out."

    "You go to bed glad you took the time to talk."
    "Still, it takes you a while to fall asleep."
    "There’s a strange humming noise outside, but you can’t see where it’s coming from."
    "You’re too tired to deal with it now, though, so you’ll just have to see if it’s still a problem tomorrow."

    jump exit_time_loop

label end_3:
    scene black

    "You decide you need some time to clear your head, so you spend your day wandering around town and doing some long-postponed chores."
    "When you finally get home that evening, you immediately realise you’ve well and truly messed up this time, at least as far as Rain is concerned."
    "She’s had some time to think it over, same as you, and is clearly not ready to let this go yet."
    "Your relationship with Rain has taken a dent. If you could try again, you’d probably do things differently."
    "Going to bed angry never feels great, but sometimes you need to take a moment. You’ll try again tomorrow."

    jump start

label end_4:
    scene black

    "You try to explain how hurtful this experiment truly is, but Alex is not convinced of your emotional argument."
    "As you try to make your case, another alien comes up behind you and calmly tells you you have failed at conflict resolution."
    "The experiment is safe, though! You will get another chance."

    jump start

label exit_time_loop:
    "TODO exit_time_loop"
    jump end_game_credits

label end_game_credits:
    "TODO end_game_credits"
    return

label restart_loop:
    # play loop restart music
    jump start_of_loop
