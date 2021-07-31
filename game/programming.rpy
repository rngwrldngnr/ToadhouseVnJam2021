init python:
    import math

    def restart_loop():
        flag.is_phone_charged = False
        flag.found_bedroom_key = False
        flag.visited_park_earlier = False
        flag.late_for_cafe = False
        flag.saw_ufo_news = False

    def is_key_here(location):
        if loops.key_location == location:
            return True
        if loops.key_location == -1 and len(key_location_set) == 4:
            loops.key_location = location
            return True
        return False
