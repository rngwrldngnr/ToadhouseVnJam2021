label test_cafe:
    scene bg cafe

    "This scene is just for testing sizing and visible portion for the character art"
label change:

    show payton neutral at left:
        zoom test.charZoom
        ypos test.level
    show rain neutral at center:
        zoom test.charZoom
        ypos test.level
    show farah neutral at right:
        zoom test.charZoom
        ypos test.level

    "These are currently [test.charZoom] scale. You can raise or lower them, and make the bigger or smaller."

    menu:
        "Higher":
            $ test.level -= .1
        "Lower":
            $ test.level += .1
        "Bigger":
            $ test.charZoom += .04
        "Smaller":
            $ test.charZoom -= .04
        "Exit":
            jump end

    jump change

init python:
    import math

    def restart_loop():
        inv.charge = False
        inv.has_key = False
        visited_park_earlier = False
        late_for_cafe = False
        flag.saw_ufo_news = False

    def is_key_here(location):
        if loops.key_location == location:
            return True
        if loops.key_location == -1 and len(key_location_set) == 4:
            loops.key_location = location
            return True
        return False
