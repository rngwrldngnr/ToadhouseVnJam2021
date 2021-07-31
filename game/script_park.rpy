label park_first_loop:
    scene bg park

    "You get to the park and look for a quiet place to sit down, but it’s not as peaceful as usual."

    show park crowd at left with easeinleft

    "A small group of people is trampling the freshly-mown grass."
    "They seem an excitable bunch. A lot of hands are being waved around."
    "Some of those hands are just being used to gesture emphatically, but others are holding some kind of equipment."
    "The group turns around to inspect a different patch of grass and you realise you know these people."
    "You met some of them at a recent UFOrum meeting!"
    "You’re trying to remember their names—you’re confident at least one of them is a Cecil—when you hear a voice behind you."

    show alex shadow at right with easeinright

    AlienShadow "This interference is unacceptable."

    "You turn around to see who’s speaking, but everything starts going black."

    scene black with dissolve

    AlienShadow "We need to be more careful next time. Try again."

    jump restart_loop

label park_early:
    $ visited_park_earlier = True

    scene bg park

    "The park is much like any other outdoor area."
    "It has a path that loops around the side of a lake with a scattering of trees and a wooden bench overlooking the small lake."
    "It’s unassuming and that’s why you like it."
    "Its utter blandness seems to have repelled all other visitors today, even the ducks, so the single bench is all yours."

    "You sit down and enjoy the silence, until the quiet is interrupted by a metallic clang."
    "There’s not usually any metal at the park, so where did that come from?"
    "You don’t see an immediate source, but you do see that staring off across the water has taken up all the extra time you had before your meeting with Farah."
    "It’s time to go to the café."

    menu:
        "Go to the café.":
            jump cafe

        "Investigate the sound.":
            pass

    "You have to know what that noise was."
    "It sounded like it came from an open space between the trees, but you don’t see anything there."
    "You slowly and methodically walk around the area, straining your ears."
    "Finally, another sound hits your ears. A soft hum, growing steadily louder, until it stops."
    "Whatever was here, it’s gone now. Maybe it’ll come back later."
    "Speaking of later, you are definitely late for your meetup with Farah."
    $ late_for_cafe = True
    "You put the weird noise out of your mind for now. Time to head to the café."

    menu:
        "Go to the café.":
            jump cafe

label walk_in_the_park:
    scene bg park

    if loop_count == 0:
        jump park_first_loop

    if visited_park_earlier:
        "The familiar surroundings of the park will help you think about how to resolve your conflict with Rain."
        "Everything’s still there. Grass, trees, duckless pond, bench, UFO."
        scene bg park ufo with dissolve
        "Wait, what?"
        "You take in the shape in front of you."
        "It’s not technically a UFO right now, because this unidentified object isn’t flying, but it certainly looks like an alien spaceship."
        "You circle it, tilting your head, and the shape shimmers."
        "It almost seems to disappear into the background, but a different angle makes it visible again."
        "As you approach, you hear the hum from before again. This must have been here the whole time."
        "As you continue to walk around it, you notice an open hatch."

        jump park_ufo_found

    "The park is much like any other outdoor area."
    "It has a path that loops around the side of a lake with a scattering of trees and a wooden bench overlooking the small lake."

    if not flag.saw_ufo_news:
        "It’s unassuming and that’s why you like it."
        "Its utter blandness seems to have repelled all other visitors today, even the ducks, so the single bench is all yours."
        "You take a moment to reflect."
        "Sometimes it seems like Rain’s outbursts come out of nowhere, but you know she has a habit of cropping up frustrations."
        "She avoids confrontations until something finally breaks the dam."
        "Exploding over one problem isn’t the way to go about it, though."

        menu:
            "What do you do next?"

            "I’ll let Rain cool off a bit.":
                jump end_3

            "We need to talk this out right now.":
                jump end_2

    else:
        "It’s unassuming, but with a double take you realise…"

        scene bg park ufo with dissolve  # TODO: See if we can do this without hiding the text?

        extend " wait, is that a UFO?!"
        "So the papers weren’t lying!"
        "It’s unlike any UFO you’ve ever seen. The movies don’t do it justice."
        "You could have sworn it was almost camouflaged in with everything else. If you hadn’t taken a second look, you might have missed it."
        "As you circle it slowly, you notice an open hatch."

        jump park_ufo_found

label park_ufo_found:
    menu:
        "What do you do?"

        "This is too much. I did not see this.":
            jump end_3

        "I get in there!":
            jump ufo_start
