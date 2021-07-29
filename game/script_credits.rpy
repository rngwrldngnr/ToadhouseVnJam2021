label credits_start:
    scene black

    # TODO: Music

    "The screen fades to black, the music starts to swell."
    "The credits appear, but not quite in the traditional way."

label credits_menu:
    menu:
        "Who do you want to know about?"

        "Angela - Music":
            call credits_angela from _call_credits_angela

        "Anouk - Writing":
            call credits_anouk from _call_credits_anouk

        "Bec - Character Art":
            call credits_bec from _call_credits_bec

        "Eli - Programming":
            call credits_eli from _call_credits_eli

        "Jeffrey - Producer, Programming":
            call credits_jeffrey from _call_credits_jeffrey

        "Daniel - Sound Designer":
            call credits_daniel from _call_credits_daniel

        "Taylor - Writing, Background Art":
            call credits_taylor from _call_credits_taylor

        "Take me back to the main menu please.":
            return

    jump credits_menu

label credits_angela:
    "Angela Geiss created all of the music for this game."
    "She created three brilliant tracks, one of which is well-hidden."
    "Angela can be found on Twitter as @holyeggshells."
    return

label credits_anouk:
    "Anouk van der Sluijs crafted this story and did the majority of the writing."
    "She also did a lot of editing and tied up loose ends."
    "Anouk can be found on Twitter as @papercutdoc."
    return

label credits_bec:
    "Rebecca Lieberwirth did all of the character art."
    "She crafted the art for these characters from their initial design to their final illustrations."
    "Bec can be found on Twitter as @straybec."
    return

label credits_eli:
    "Eli did the majority of the programming."
    # TODO: Update this, because the minigame is in the game now.
    "He even implemented a minigame, which ultimately didn't make it into the final release, but is still worth mentioning."
    return

label credits_jeffrey:
    "Jeffrey Lindsey gathered this team together and made sure everyone knew what they needed to do."
    "He also helped with some of the programming."
    "Jeffrey can be found on Twitter as @jeffreylindsey."
    return

label credits_daniel:
    "Daniel Cruz provided sound effects."
    "Daniel can be found on Twitter as @Mr_DanielC, and online at www.sonicmedley.com."
    return

label credits_taylor:
    "Taylor Dryden created all of the background art."
    "She also wrote all the location descriptions and a bit of dialogue."
    "Taylor can be found on Twitter as @lakeffectkids."
    return
