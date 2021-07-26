label ufo_start:
    scene bg ufo interior

    "You’re wary as you peer inside of the UFO."
    "You’re not sure what to expect, but you’ve seen enough horror movies to get a few ideas."
    "From the looks of it, the walls are lined with screens, buttons, and keyboards and something that almost comically looks like a video game joystick."

    show alien neutral at center with dissolve:
        zoom .55
        ypos 1.65

    "And is that a real alien?!"

    Alien "Excuse me. You shouldn’t be here."
    Alien "How did you get here? What are you doing?"

    menu:
        "I could ask you the same questions.":
            Payton "I could ask you the same questions."
            jump ufo_narration_a

        "The door was open. I thought I’d take a look.":
            Payton "The door was open. I thought I’d take a look."
            jump ufo_narration_b

label ufo_narration_a:
    "The alien seems…"
    extend " nervous?"
    extend " Angry?"
    extend " Insulted?"

    "It’s tough to tell."
    "The helmet’s in the way and you have no idea if your human interpretations of facial expressions apply to this alien."
    "That thought makes a nervous giggle burst up inside of you. An {i}alien!{/i}"

    Alien "You can call me Alex."

    Alex "This is my ship."
    Alex "I am here to observe the social interactions between the people of this town to see if humans are capable of conflict resolution."
    Alex "Your presence is harming the accuracy of our data."
    Alex "Please follow me. I will take you home."

    menu:
        "Alright, I don’t want any trouble.":
            Payton "Alright, I don’t want any trouble."
            jump ufo_narration_b1_2

        "Wait, you’re experimenting on us? That’s so cliché.":
            Payton "Wait, you’re experimenting on us? That’s so cliché."
            pass

    Alex "Do not insult that which you do not understand."
    Alex "We are doing important work."

    menu:
        "Okay, I’m getting bad vibes here. I’ll leave.":
            Payton "Okay, I’m getting bad vibes here. I’ll leave."
            jump ufo_narration_a2

        "You’re right, I don’t understand. Explain it to me.":
            Payton "You’re right, I don’t understand. Explain it to me."
            jump ufo_alex_a2

label ufo_narration_a2:
    "The alien looks relieved, but again, you can’t be 100\% sure."
    "The only thing you’re certain of is that Alex definitely doesn’t want you to be here."
    "Those suspicions are immediately confirmed when you notice another alien sneak up behind you."
    "A second later, you’re no longer worried at all."
    "Why were you here again?"
    # TODO: Fade to black?
    "You don’t remember."
    jump restart_loop

label ufo_alex_a2:
    Alex "We are here to see if your planet is ready to join our galactic federation of planets."
    Alex "You have been chosen as a test subject."
    Alex "We are observing your ability to peacefully resolve a conflict."
    Alex "When you fail, we wipe your memory and make you try again."

    menu:
        "That seems like an ill-conceived experiment doomed to fail.":
            Payton "That seems like an ill-conceived experiment doomed to fail."
            jump ufo_alex_a3

        "Wait, you wipe my memory? Have I been here before?":
            Payton "Wait, you wipe my memory? Have I been here before?"
            jump ufo_narration_a3

label ufo_alex_a3:
    Alex "That would be a hurtful statement if I were sensitive to human emotions."
    Alex "Why would you say such a thing?"

    menu:
        "Your experiment is cruel and inhumane!":
            Payton "Your experiment is cruel and inhumane!"
            jump end_4

        "I can’t learn and grow if you wipe my memory!":
            Payton "I can’t learn and grow if you wipe my memory!"
            jump ufo_narration_a4

label ufo_narration_a4:
    "Alex contemplates your words."
    "As the alien considers your argument, you look around to see if anyone is trying to sneak up behind you to wipe your mind."
    "Another alien catches your eye, but it doesn’t look like you’re about to get zapped with some kind of mind-wiping device."

    Alex "We did not consider this perspective. Your logic is sound."
    Alex "We will release you. Do not make us regret it."
    Alex "Go out and grow."

    jump end_1

label ufo_narration_a3:
    "You take a hard look at the smooth steel of the ship around you, willing yourself to remember."
    "A piercing headache is building behind your temples."
    "You look Alex in the eye and for a moment you know exactly how many times you’ve been here before."
    "A second later, you don’t remember."
    # TODO: Fade to black?
    "You don’t remember."
    jump restart_loop

label ufo_narration_b:
    "The alien seems calmed by your willingness to answer questions."
    "You can’t be certain, though. The facial expressions seem similar to yours, but this is an alien."

    Alien "Of course. Curiosity is only natural."
    Alien "You can call me Alex."

    menu:
        Alex "Would you like a tour?"

        "Yes, please!":
            Payton "Yes, please!"
            jump ufo_narration_b1

        "Wait, I thought you said I shouldn’t be here?":
            Payton "Wait, I thought you said I shouldn’t be here?"
            jump ufo_alex_b2

label ufo_narration_b1:
    "A wall slides away to reveal a door."
    "Alex guides you through a smooth hallway."
    "You wonder what they use for electricity."
    "The walls are humming and you can smell a scent you can only describe as energetic."
    "You are led into a small, warmly lit room where Alex invites you to sit down. "

    Alex "Just wait here a moment, Payton. I will take care of you."

    jump ufo_narration_b1_2

label ufo_narration_b1_2:
    "Wait, did you tell Alex your name? You don’t remember."
    # TODO: Fade to black?
    "You don’t remember."
    jump restart_loop

label ufo_alex_b2:
    Alex "Your short-term memory is still good."
    Alex "Excellent."
    Alex "Not to worry, you will be out of here soon enough."
    Alex "We have no reason to hurt you."

    "You don’t know if that was meant to be reassuring, but if it was, it failed."
    "You turn around, looking for the exit, but the door you came in through is no longer there."
    "A soft humming noise is in the air now."
    "Maybe the door was in a different place? You don’t remember."
    # TODO: Fade to black?
    "You don’t remember."

    jump restart_loop
