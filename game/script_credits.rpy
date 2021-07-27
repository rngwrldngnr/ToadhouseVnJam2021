label credits_start:
    scene black

    "The screen fades to black, the music starts to swell."
    "The credits appear, but not quite in the traditional way."

label credits_menu:
    menu:
        "Who do you want to know about?"

        "Angela - Music":
            call credits_angela

        "Anouk - Writing":
            call credits_anouk

        "Bec - Character Art":
            call credits_bec

        "Eli - Programming":
            call credits_eli

        "Jeffrey - Producer, Programming":
            call credits_jeffrey

        "Sonic_Meledy - Sound Effects":
            call credits_sonic_meledy

        "Taylor - Writing, Background Art":
            call credits_taylor

        "Take me back to the main menu please.":
            return

    jump credits_menu

label credits_angela:
    "Angela Geiss created all of the music for this game."
    "She created four brilliant tracks. One of which is well hidden."
    "She can be found on Twitter as @holyeggshells."
    return

label credits_anouk:
    "Anouk crafted this story and did the majority of the writing."
    "She also did a lot of editing and tying up loose ends."
    return

label credits_bec:
    "Rebecca Lieberwirth, also known as Bec, did all of the character art."
    "She crafted the art for these characters from their initial design to their final illustrations."
    "She can be found on Twitter as @straybec."
    return

label credits_eli:
    "Eli did the majority of the programming."
    "He even implemented a minigame, which ultimately didn't make it into the final release, but is still worth mentioning."
    return

label credits_jeffrey:
    "Jeffrey Lindsey gathered this team together, and made sure everyone knew what they needed to do."
    "He also helped with some of the programming."
    return

label credits_sonic_meledy:
    "Sonic_Meledy provided sound effects."
    return

label credits_taylor:
    "Taylor created all of the background art."
    "She also wrote the majority of the character dialogs."
    return
