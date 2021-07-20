label livingroom:
    scene bg livingroom

    if before("8:23 AM"):
        jump livingroom_morning_talkn
    else:
        pass

    "You rush into the living room to grab your stuff."
    "You don’t see your flatmate Rain, but you can still smell the fried eggs she always has for breakfast."
    "She’s left her dirty dishes on the counter, which is unlike her."
    "A closer look at the counter reveals a note from Rain."
    "\“We need to talk.\” {w}Oh boy."
    "You’ll have to worry about that later, though. Time to meet up with Farah."
    jump cafe


label livingroom_morning_talkn:
    "You rush into the living room to grab your stuff."
    "This place brings many memories since the years that you’ve lived here."
    "It’s one of the cosiest areas in your home, and you’ve often fallen asleep on that couch while watching movies."
    "You’re surprised the Monstera plant is still alive, because you don’t have much of a green thumb, but it seems to be doing well."
    "Oh, you’ve left some coffee cups on the table. You should take care of those later."

    show rain neutral:
        zoom .8
        ypos 1.45
    "The TV is on, but the volume is too low to make out what the newsreaders are saying."
    "As you’re patting your pockets to check you have your wallet and keys, {nw}"
    extend "Rain walks past with an empty plate."
    "You can still smell the fried eggs she always has for breakfast and it’s making you peckish."
    "Rain usually has a permanent case of resting happy face, {nw}"
    show rain unhappy
    extend "but right now she doesn’t look cheerful."

    menu:
        "but right now she doesn’t look cheerful."

        "These conversations shouldn’t be rushed. Better take your time to talk tonight.":
            jump livingroom_morning_talk_skip

        "“Hey, Rain. Are you okay?”":
            jump livingroom_morning_talk_start

label livingroom_morning_talk_skip:
    "You seek a moment of eye contact with Rain to give her a reassuring smile and nod. {nw}"
    show rain unhappy eyecontact
    extend "Your flawless comforting technique is not very effective, {nw}"
    extend "but you don’t have time to talk right now. You are meeting Farah at the café."
    jump cafe

label livingroom_morning_talk_start:
    Rain unhappy eyecontact "You mean you really don’t know what’s bothering me?"
    menu:
        "If I did I wouldn’t be asking.":
            jump livingroom_morning_talk_rude
        "I really don’t. Did I do something wrong?":
            jump livingroom_morning_talk_polite

label livingroom_morning_talk_rude:
    Rain annoyed "You’re being awfully rude for what you did last night, {nw}"
    extend "that’s not cool Peyton."

    menu:
        Rain "That's not cool Peyton."
        "What do you mean what I did last night? I don’t remember doing anything!":
            pass
        "I really have no idea what you’re talking about, Rain.":
            pass

    Rain angry "Stop joking around. {w=1.5}"
    extend "I have to go right now, I'm going to be late for my shift. {nw}"
    extend "We can talk about it later."
    jump livingroom_morning_talk_unresolved

label livingroom_morning_talk_polite:
    Rain unhappy eyecontact "Last night you borrowed my laptop without asking me about it. {w=.5}"
    extend "I normally don’t mind but I couldn’t find it this morning, {nw}"
    extend "and I thought I left it at the café until I found it. I was really worried!"

    menu:
        "I was really worried!"

        "I don’t remember doing that at all.":
            "I don’t remember doing that at all. I must have been more tired than I thought, I’m sorry."
            extend "I’ll remember to ask you before borrowing anything of yours again."
            jump end_2

        "Are you sure that I did that?":
            "Are you sure that I did that? Maybe you could have misplaced it before you left."
            pass

    Rain annoyed "I was gone all day yesterday, I couldn’t have done it. When I got home last night you were already asleep, and my laptop was missing."

    menu:
        "My laptop was missing."

        "I didn’t drink last night, and I honestly don’t remember doing it. I’m sorry though, it wasn’t cool to take something of yours without asking.":
            pass

        "Maybe I was sleepwalking and took your laptop, I’m sorry. I would never take something of yours without asking.":
            pass

    jump end_2

label livingroom_morning_talk_unresolved:
    "Rain leaves."
    extend "This is definitely a conversation to pick up again later."
    extend "Then the words BREAKING NEWS and its accompanying sting on the TV do their job of catching your attention."
    extend "Your very bored-looking local newsreader is joined by a frazzled colleague."
    extend "There’s a blurry picture on the screen that’s very similar to the one in the newspaper you picked up yesterday."

    menu:
        "You're late. Leave to meet Farah.":
            jump cafe

        "Turn up the volume to catch what they're saying":
            jump livingroom_ufo_news

define SkepticalAnchor = Character(_("Skeptical Anchor"))
define BelieverAnchor = Character(_("Believer Anchor"))

label livingroom_ufo_news:
    $ flag.saw_ufo_news = True
    SkepticalAnchor "We’ve heard stories about UFOs before, and nothing has ever come of it. What makes this time any different?"

    BelieverAnchor "The amount of people that have witnessed it, and the photos! You can’t deny those photos. These people took the photos of before and after and one minute those things were there, and the next they weren’t."

    SkepticalAnchor "It could be any number of things, a light flare on the camera or a shadow from anything that’s nearby."

    BelieverAnchor "We’ve already ruled out all of those possibilities, our team has gone out there and tried every trick in the book to see if they can recreate these photos and nothing that they tried worked. We could have seen an {i}actual UFO{/i}! Think of all the possibilities that could come from this!"

    "You’re on The UFOrum before the segment is even over."
    extend "The news segment has drawn a few new members to the forum, who are hotly debating the correct pronunciation of “UFOrum”."
    extend "You’d been seeing the same witnesses and pictures pop up, of course, but official news outlets don’t usually take these things that seriously."
    extend "The forum had agreed that this recent evidence was overwhelming, but you had to admit that even the most cautious among you had been disappointed by false hope before."
    extend "Still, this seemed more than a slow news day to you."
    extend "You’re neck-deep in the latest thread and have just reported a rude comment about the red-headed newscaster to the moderators {nw}"
    $ add_minutes(60)
    extend "when you realise a lot of time has passed. Whoops."
    extend "You were supposed to meet Farah for lunch. Time to go."

    $ late_for_cafe = True
    jump cafe
