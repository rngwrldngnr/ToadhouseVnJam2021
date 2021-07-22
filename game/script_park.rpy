label walk_in_the_park:
    scene bg park

    "The park is much like any other outdoor area."
    "It has a path that loops around the side of a lake with a scattering of trees and a singular bench overlooking the small lake."

    if not flag.saw_ufo_news:
        "It’s unassuming and that’s why you like it."
        "Its utter blandness seems to have repelled all other pedestrians today, so the single bench is all yours."
        "You take a moment to reflect."
        "Sometimes it seems like Rain’s outbursts come out of nowhere, but you know she has a habit of cropping up frustrations."
        "She avoids confrontations until something finally breaks the dam."
        "Exploding over one problem isn’t the way to go about it, though."

        menu:
            "What do you do next?"

            "I’ll let Rain cool off a bit.":
                jump end_3
            "We need to talk this out properly.":
                jump end_2

    else:
        scene bg park ufo with dissolve

        "It’s unassuming, but with a double take you realize… wait, is that a UFO?!"
        "So the papers weren’t lying!"
        "It’s unlike any UFO you’ve ever seen, the movies don’t do it justice."
        "You could have sworn it was almost camouflaged in with everything else, and that if you hadn't taken a second look you might have completely missed it."
        "As you circle it slowly, you notice an open hatch."

        menu:
            "What do you do?"

            "This is too much. I did not see this.":
                jump end_3
            "I get in there!":
                jump ufo_start
