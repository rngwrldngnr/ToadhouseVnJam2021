label walk_in_the_park:
    scene bg park
    "The park is much like any other outdoor area. It has a path that loops around the side of a lake with a scattering of trees and a singular bench overlooking the small lake. {nw}"

    if not flag.saw_ufo_news:

        extend "It’s unassuming and that’s why you like it. Its utter blandness seems to have repelled all other pedestrians today, so the single bench is all yours. "

        "You take a moment to reflect. Sometimes it seems like Rain’s outbursts come out of nowhere, but you know she has a habit of cropping up frustrations. She avoids confrontations until something finally breaks the dam. Exploding over one problem isn’t the way to go about it, though."

        menu:
            "What do you do next?"

            "I’ll let Rain cool off a bit.":
                jump end_3
            "We need to talk this out properly.":
                jump end_2

    else:

        scene bg park ufo with dissolve
        extend "It’s unassuming, but with a double take you realize… wait, is that a UFO?! So the papers weren’t lying! It’s unlike any UFO you’ve ever seen, the movies don’t do it justice. You could have sworn it was almost camouflaged in with everything else, and that if you hadn't taken a second look you might have completely missed it. As you circle it slowly, you notice an open hatch."

        menu:
            "What do you do?"

            "This is too much. I did not see this.":
                jump end_3
            "I get in there!":
                pass

    scene bg ufo interior
    "You’re wary as you peer inside of the UFO. You’re not sure what to expect, but you’ve seen enough horror movies to get a few ideas. From the looks of it, the walls are lined with screens, buttons, and keyboards and something that almost comically looks like a video game joystick. {nw}"
    show alien neutral at center with dissolve:
        zoom .55
        ypos 1.65
    extend "And is that a real alien?!"

    # conversation between player character and alien. the aliens are shocked to discover their camouflage has failed, but don’t hesitate to share the truth with the player, because they plan to wipe the PC’s mind and restart the loop anyway. the aliens just want to distract the player character long enough to knock them out and restart the loop, but the player character can also try to convince the alien that this is immoral or that they’ve learned their lesson (whichever you prefer). this conversation can end in two ways.
    #
    # either: the aliens aren’t convinced. (END 4)
    # or: the player character convinces the alien. (END 1)

    a0 "Excuse me. You shouldn’t be here. How did you get here? What are you doing?"

    menu:
        "I could ask you the same questions.":
            jump alien_talk_a
        "The door was open. I thought I’d take a look.":
            jump narration_b

label alien_talk_a:
    "The alien seems… nervous? Angry? Insulted? It’s tough to tell. The helmet’s in the way and you have no idea if your human interpretations of facial expressions apply to this alien. That thought makes a nervous giggle burst up inside of you. An alien!"

    a0 "You can call me Alex. {nw}"
    a "You can call me Alex. This is my ship. I am here to observe the social interactions between the people of this town to see if humans are capable of conflict resolution. Your presence is harming the accuracy of our data. Please follow me. I will take you home."

    menu:
        "Alright, I don’t want any trouble.":
            jump alien_talk_b_1_2
        "Wait, you’re experimenting on us? That’s so cliché.":
            pass

    a "Do not insult that which you do not understand. We are doing important work."

    menu:
        "Okay, I’m getting bad vibes here. I’ll leave.":
            jump narration_2
        "You’re right, I don’t understand. Explain it to me.":
            jump alex_2

label alien_talk_b_1_2:
    "Wait, did you tell Alex your name? You don’t remember. You don’t remember."
    jump restart_loop

label narration_2:
    "The alien looks relieved, but again, you can’t be 100% sure. The only thing you’re certain of is that Alex definitely doesn’t want you to be here. Those suspicions are immediately confirmed when you notice another alien sneak up behind you. A second later, you’re no longer worried at all. Why were you here again? You don’t remember."
    jump restart_loop

label alex_2:
    a "We are here to see if your planet is ready to join our galactic federation of planets. You have been chosen as a test subject. We are observing your ability to peacefully resolve a conflict. When you fail, wipe your memory and make you try again."

    menu:
        "That seems like an ill-conceived experiment doomed to fail.":
            jump alex_a3
        "Wait, you wipe my memory? Have I been here before?":
            jump narration_a3

label alex_a3:
    a "That would be a hurtful statement if I were sensitive to human emotions. Why would you say such a thing?"

    menu:
        "Your experiment is cruel and inhumane!":
            jump end_4
        "I can’t learn and grow if you wipe my memory!":
            jump narration_a4

label narration_a4:
    "Alex contemplates your words. As the alien considers your argument, you look around to see if anyone is trying to sneak up behind you to wipe your mind. Another alien catches your eye, but it doesn’t look like you’re about to get zapped with some kind of mind-wiping device."

    a "We did not consider this perspective. Your logic is sound. We will release you. Do not make us regret it. Go out and grow."
    jump end_1

label narration_a3:
    "TODO narration_a3"

label narration_b:
    "The alien seems calmed by your willingness to answer questions. You can’t be certain, though. The facial expressions seem similar to yours, but this is an alien."

    a "Of course. Curiosity is only natural. You can call me Alex. Would you like a tour?"

    menu:
        "Yes, please!":
            jump narration_B1
        "Wait, I thought you said I shouldn’t be here?":
            jump alex_b2

label narration_B1:
    "A wall slides away to reveal a door. Alex guides you through a smooth hallway. You wonder what they use for electricity. The walls are humming and you can smell a scent you can only describe as energetic. You are led into a small, warmly lit room where Alex invites you to sit down. "

    a "Just wait here a moment, Payton. I will take care of you."

    jump restart_loop

label alex_b2:
    "TODO alex_b2"
