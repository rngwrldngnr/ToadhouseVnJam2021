# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rami Roommate")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    "Feel like I barely got any sleep, but it's definitely morning now."

    "Guess I should go and see what the damage is."

    "..."

    "The door's locked."

    default key_location_set = set()

label key_search:

    menu:
        set key_location_set
        "Where did I leave my key?"

        "Check under the pillow":
            "Nothing"
            jump key_search

        "Check all the sheets and bedding":
            "Nothing"
            jump key_search

        "Check under the bed":
            "Nothing"
            jump key_search

        "Check inside the dresser":
            "Nothing"
            jump key_search

        "Check behind and under the dresser":
            "Nothing"
            jump key_search

        "Check inside the lampshade":
            "Nothing"
            jump key_search

        "Check your pockets":
            "Nothing"
            jump key_search

    "Unfortunately that's all the locations I can think of. It's possible I'm locked in."

    menu:
        "...time to get serious."

        "Break down the door":
            jump thud

        "Abseil":
            jump abseil

label thud:

    "That could have perhaps gone better."

    "Still, you're out."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Rami Roommate angry

    # These display lines of dialogue.

    r "You've created a new Ren'Py game."

    r "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
