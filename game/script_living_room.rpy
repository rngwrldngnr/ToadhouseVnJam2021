label livingroom:
    scene bg livingroom with dissolve

    if not flag.has_flatmate_left:
        jump livingroom_morning_talkn
    else:
        pass

    "You rush into the living room to grab your stuff."
    "You don’t see your flatmate Rain, but you can still smell the fried eggs she always has for breakfast."
    "You just missed her."
    "She’s left her dirty dishes on the counter, which is unlike her."
    "A closer look at the counter reveals a note from Rain."
    "“We need to talk.”"
    "Oh boy."
    "Rain never “needs to talk” unless something is very wrong."
    "Did you do something to upset her?"
    "You’ll have to worry about that later. It’s time to meet up with Farah."

    jump cafe

label livingroom_morning_talkn:
    "You rush into the living room to grab your stuff."
    "This place holds a lot of memories of the years that you’ve lived here."
    "It’s one of the cosiest areas in your home and you’ve often fallen asleep on that couch while watching movies."
    "You’re surprised the Monstera plant is still alive, because you don’t have much of a green thumb, but it seems to be doing well."
    "Oh, you’ve left some coffee cups on the table. You should take care of those later."
    "The TV is on, but the volume is too low to make out what the newsreaders are saying."
    "As you’re patting your pockets to check you have your wallet, phone, and keys, Rain walks past with an empty plate."

    show rain sad right with easeinright

    "You can still smell the fried eggs she always has for breakfast and it’s making you peckish."
    "Rain usually has a permanent case of resting happy face, but right now she doesn’t look cheerful."

    menu:
        "but right now she doesn’t look cheerful."

        "These conversations shouldn’t be rushed. Better take your time to talk tonight.":
            jump livingroom_morning_talk_skip

        "“Hey, Rain. Are you okay?”":
            jump livingroom_morning_talk_start

label livingroom_morning_talk_skip:
    "You seek a moment of eye contact with Rain to give her a reassuring smile and nod."

    show rain frustrated right

    "Your flawless comforting technique is not very effective"
    "but you don’t have time to talk right now. You are meeting Farah at the café."

    "As you leave the house, you check your watch and realise it’s earlier than you expected."
    "Strange, you thought finding your key had taken a lot longer."
    "Your walk to the café takes you right past the park, so you could easily take a little walk to pass the time."
    "Farah is usually early too, though, so you could also just go straight to the café."

    menu:
        "Take a walk in the park.":
            "You’ve got time, so you decide to stretch your legs and get some fresh air."
            jump park_early

        "Go to the café early.":
            jump cafe

label livingroom_morning_talk_start:
    show rain frustrated right

    Rain "You mean you really don’t know what’s bothering me?"

    menu:
        "If I did I wouldn’t be asking.":
            jump livingroom_morning_talk_rude

        "I really don’t. Did I do something wrong?":
            jump livingroom_morning_talk_polite

label livingroom_morning_talk_rude:
    show rain angry right

    Rain "You’re being awfully rude for what you did last night."
    Rain "That’s not cool, Payton."

    menu:
        Rain "That’s not cool, Payton."
        
        "I don’t remember doing anything last night!":
            pass
        "I’m sorry, I have no idea what you’re talking about, Rain.":
            pass

    Rain "Forget it, Payton. It wouldn’t be the first time you forgot something."
    Rain "I’m going to be late for work."
    Rain "We’ll talk about it later."

    jump livingroom_morning_talk_unresolved

label livingroom_morning_talk_polite:
    show rain sad right

    Rain "Last night you borrowed my laptop without asking!"
    Rain "I normally don’t mind, but I couldn’t find it this morning."
    Rain "I thought someone took it from my bag at the café yesterday until I saw it sticking out from under the pillows on the couch. Your notebook was on top."
    Rain "I was really worried!"

    menu:
        Rain "I was really worried!"

        "I must have forgotten I took it. I’m sorry.":
            Payton "I must have forgotten I took it. I’m sorry."
            jump end_2

        "Maybe you misplaced it.":
            Payton "Maybe you misplaced it. You need to be more careful."
            pass

    Rain "You know how meticulous I am about my stuff. I always keep it in the same place."
    Rain "Besides, your notebook was right there!"

    Payton "You know my memory sucks. It’s not my fault!"
    Payton "I know I’m forgetful, but you don’t have to yell at me."
    Payton "I told you I kept forgetting to buy a new laptop battery."
    Payton "You could have reminded me, but instead you’re just blaming me!"

    Rain "I didn’t mind your forgetfulness when you forgot to do the dishes yesterday, or that time I had to go home on my lunch break because you locked yourself out of the house, but taking someone’s laptop without asking is not the same thing!"

    Payton "Fine, I’m sorry!"
    Payton "I’d promise not to do it again, but I’d probably forget that too!"

    Rain "I don’t want to have this conversation anymore."
    Rain "I’m leaving now. I’m already late for work because of you."

    jump end_3

label livingroom_morning_talk_unresolved:
    hide rain with easeoutleft

    "Rain leaves."
    "This is definitely a conversation to pick up again later."
    "Then the words BREAKING NEWS and its accompanying sting on the TV do their job of catching your attention."
    "Your very bored-looking local newsreader is joined by a frazzled colleague."
    "There’s a blurry picture on the screen that’s very similar to the one in the newspaper you picked up yesterday."

    menu:
        "You’re late. Leave to meet Farah.":
            jump cafe

        "Turn up the volume to catch what they’re saying":
            jump livingroom_ufo_news

label livingroom_ufo_news:
    $ flag.saw_ufo_news = True

    SkepticalAnchor "We’ve heard stories about UFOs before, and nothing has ever come of it."
    SkepticalAnchor "What makes this time any different, Fox?"

    BelieverAnchor "The number of witnesses, Dana, and the videos!"
    BelieverAnchor "You can’t deny those videos."
    BelieverAnchor "They show an unidentified flying object appearing and the next second it’s gone!"

    SkepticalAnchor "It could be any number of things!"
    SkepticalAnchor "A light flare on the camera or a shadow from something moving nearby."
    SkepticalAnchor "The footage was probably doctored!"

    BelieverAnchor "We’ve already ruled out all of those possibilities!"
    BelieverAnchor "Our team has gone out there and tried every trick in the book to see if they could recreate the effect and nothing worked."
    BelieverAnchor "We could have seen an {i}actual UFO{/i}!"
    BelieverAnchor "Think about the implications!"

    "You’re on The UFOrum before the segment is even over."
    "The news segment has drawn a few new members to the forum, who are hotly debating the correct pronunciation of “UFOrum”."
    "You’d been seeing the same witnesses and pictures pop up, of course, but official news outlets don’t usually take these things that seriously."
    "The forum had agreed that this recent evidence was overwhelming, but you had to admit that even the most cautious among you had been disappointed by false hope before."
    "Still, this seemed more than a slow news day to you."
    "You’re neck-deep in the latest thread and have just reported a rude comment about the red-headed newscaster to the moderators when you realise a lot of time has passed. Whoops."
    "You were supposed to meet Farah for coffee. Time to go."

    $ flag.late_for_cafe = True
    jump cafe
