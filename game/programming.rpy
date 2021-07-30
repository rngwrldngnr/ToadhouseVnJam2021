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
