label credits_start:
    scene black

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

        "Daniel - Sound Designer":
            call credits_daniel from _call_credits_daniel

        "Eli - Programming":
            call credits_eli from _call_credits_eli

        "Jeffrey - Producer, Programming":
            call credits_jeffrey from _call_credits_jeffrey

        "Taylor - Writing, Background Art":
            call credits_taylor from _call_credits_taylor

        "Take me back to the main menu please.":
            jump credits_end_game

    jump credits_menu

label credits_angela:
    show expression "./images/credits/angela1.png" at left with easeinleft
    "Angela Geiss created all of the music for this game."
    show expression "./images/credits/angela2.png" at right with easeinright
    "She created four brilliant tracks, one of which is well-hidden."
    scene black with easeoutbottom
    "Angela can be found on Twitter as @holyeggshells."
    return

label credits_anouk:
    show expression "./images/credits/anouk1.png" at left with easeinleft
    "Anouk van der Sluijs crafted this story and did the majority of the writing."
    show expression "./images/credits/anouk2.png" at right with easeinright
    "She also did a lot of editing and tied up loose ends."
    scene black with easeoutbottom
    "Anouk can be found on Twitter as @papercutdoc."
    return

label credits_bec:
    show expression "./images/credits/bec1.png" at left with easeinleft
    "Rebecca Lieberwirth did all of the character art."
    show expression "./images/credits/bec2.png" at right with easeinright
    "She crafted the art for these characters from their initial design to their final illustrations."
    scene black with easeoutbottom
    "Bec can be found on Twitter as @straybec."
    return

label credits_daniel:
    show expression "./images/credits/daniel1.png" at center with easeinleft
    "Daniel Cruz provided sound effects."
    scene black with easeoutbottom
    "Daniel can be found on Twitter as @Mr_DanielC, and online at www.sonicmedley.com."
    return

label credits_eli:
    show expression "./images/credits/eli1.png" at left with easeinleft
    "Eli Berg-Maas did a lot of the programming."
    show expression "./images/credits/eli2.png" at right with easeinright
    "He set up the source control repository, got everything started with Ren'Py, and implemented a minigame which is hidden in one of the branches."
    scene black with easeoutbottom
    "Eli can be found on Twitter as @rngwrldngnr."
    return

label credits_jeffrey:
    show expression "./images/credits/jeffrey1.png" at left with easeinleft
    "Jeffrey Lindsey gathered this team together and made sure everyone knew what they needed to do."
    show expression "./images/credits/jeffrey2.png" at right with easeinright
    "He also helped with some of the programming."
    scene black with easeoutbottom
    "Jeffrey can be found on Twitter as @jeffreylindsey."
    return

label credits_taylor:
    show expression "./images/credits/taylor1.png" at left with easeinleft
    "Taylor Dryden created all of the background art."
    show expression "./images/credits/taylor2.png" at center with easeinright
    show expression "./images/credits/taylor3.png" at right with easeinright
    "She also wrote all the location descriptions and a bit of dialogue."
    scene black with easeoutbottom
    "Taylor can be found on Twitter as @lakeffectkids."
    return

label credits_end_game:
    stop sound fadeout 1.0
    return
