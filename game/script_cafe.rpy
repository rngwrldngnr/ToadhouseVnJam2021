label cafe:
    scene bg cafe with dissolve

    "Upon entering the café, the first thing you notice is the smell of the coffee beans."
    "It’s such a relaxing smell, with an undertone of pastries and other sweets."
    "The café has a lot of earth tones with soft lighting and a large landscape painting on the back wall to bring a relaxing atmosphere to it."
    "It’s mostly quiet. A few other patrons are talking and you can hear the blender mixing some sort of icy drink."

    if flag.late_for_cafe:
        show farah neutral right with easeinright
    else:
        show farah smile right with easeinright

    "Farah waves at you from their seat."
    "They’ve picked out a nice table by the window and are already cradling a huge mug of a hot drink you’d bet is decaffeinated."
    "You indicate nonverbally that you’ll grab your standard chai latte before you join them."
    "You avoid the croissants—this place hasn’t realised yet that there is such a thing as too flakey—but you go for a sandwich and quickly join your friend."

    if flag.late_for_cafe:
        jump cafe_late
    else:
        jump cafe_on_time

label cafe_on_time:
    Farah "Payton, how’s it going?"
    Farah "I got here before you and it felt rude not to order, but I promise the caffeine in this decaf latte has barely hit my bloodstream."
    Farah "How have you been?"

    menu:
        "I’m alright, how about you?":
            jump cafe_no_rain

        "I think Rain and I had a fight last night?":
            jump cafe_about_rain

label cafe_no_rain:
    Payton "I’m alright, how about you?"

    Farah "I’ve got a Payton, I’ve got a coffee."
    Farah "Right now is looking good to me."

    "You’re inclined to agree."
    "No use ruining this moment by worrying about Rain."
    "You came here to catch up with Farah."

    hide farah
    show farah cat pics with easeinright

    "You ask them about their new cat and spend the rest of your time together slowly sipping your massive drink and looking at pictures of a small cat trying to use a bigger, much older cat as a pillow."

    hide farah with dissolve

    "When you finally can’t justify taking up a table any longer without ordering another drink, it’s time to go."
    "You still haven’t figured out what to do about Rain, but maybe a walk in the park will help."

    menu:
        "Take a walk.":
            jump walk_in_the_park

label cafe_about_rain:
    Payton "I think Rain and I had a fight last night?"

    show farah neutral right

    Farah "You think? You don’t remember?"
    Farah "What’s wrong?"

    menu:
        "Rain is upset about something I don’t remember doing.":
            Payton "Rain is upset about something I don’t remember doing."
            jump farah_b1

        "I’m okay. I’d rather talk about something else right now.":
            Payton "I’m okay. I’d rather talk about something else right now."
            jump farah_b2

label farah_b1:
    show farah neutral right

    Farah "I know your memory is spotty sometimes, but that’s a lot to forget."
    Farah "Rain actually texted me about it."
    Farah "She talks things through with me sometimes before confronting a problem."

    show farah smile right

    Farah "Would you like to talk about it too?"

    menu:
        "She talked to you before she talked to me?!":
            Payton "She talked to you before she talked to me?!"
            jump farah_b3

        "Yeah, that might help.":
            Payton "Yeah, that might help."
            jump farah_narration

label farah_b2:
    Farah "Yeah, of course."

    show farah smile right

    Farah "We’re here to have coffee and take a break."
    Farah "Want to see a picture of my cats?"

    hide farah
    show farah cat pics with easeinright

    "Farah shows you the world’s cutest pictures of their cats."
    "You’d already seen most of them on social media and you’re about to point that out, but for once you catch yourself before you say it."
    "The pictures are adorable. You don’t mind seeing them again."

    hide farah with dissolve

    "After you’ve both finished your drinks, you say your goodbyes and head out the door."
    "You still haven’t had a chance to think about the argument with Rain, though."
    "You need some more time to clear your head."

    menu:
        "A walk in the park is just what you need."

        "Take a walk in the park.":
            jump walk_in_the_park

label farah_b3:
    show farah exasperated right

    Farah "Rain is one of my closest friends, Payton, of course we talk!"
    Farah "I know she’s mad at you, but you don’t have to take it out on me."

    show farah neutral right

    Farah "Look, I know you’re upset, but do you think you can set it aside for an hour so we can spend some time together?"
    Farah "You can pick it up with Rain later."

    Payton "You’re right. I didn’t come here to get upset at you."

    show farah smile right

    Payton "I came here for a hot beverage and some time with a friend."

    hide farah
    show farah cat pics with easeinright

    "You feel a little uncomfortable for a moment, but by the time you wave goodbye, you’ve managed to turn the mood around and were even graced with an extra cute picture of Farah’s new cat."

    hide farah with dissolve

    "You definitely need some more time to think about your argument with Rain, though. Maybe a walk in the park will help."

    menu:
        "Take a walk.":
            jump walk_in_the_park

label farah_narration:
    "Farah listens while you share your side of the story."
    "There isn’t much to share, because you don’t remember what you could have done to upset Rain, but it’s still good to talk."

    hide farah
    show farah cat pics with easeinright

    "After a bit, the conversation pivots to Farah’s cats and their new homemade scratching pole."

    hide farah with dissolve

    "You have a cosy time together and almost forget to drink your coffee before it gets cold."
    "Farah also gives you something to think about."
    "If Rain has discussed this with Farah, it must really bother her a lot."
    "When you finally finish your drinks and say your goodbyes, you decide to walk to the park and find a quiet spot."

    menu:
        "What’s the next best step? Should you take some time to process everything or call Rain to talk things out right away?"

        "Take a walk in the park.":
            jump walk_in_the_park

        "Call Rain.":
            jump call_rain

label cafe_late:
    show farah exasperated right

    Farah "Payton, I’ve practically finished my coffee already. You’re so late, what happened?"

    menu:
        "Ugh, the world hates me today. Everything’s going wrong.":
            jump cafe_complain

        "I’m sorry. I think Rain and I had a fight last night?":
            jump cafe_rain_late

label cafe_complain:
    show farah neutral right

    Farah "Ah, that sucks."
    Farah "Next time the world hates you, though, could you shoot me a message so I know I can sleep in a little longer?"

    show farah smile right

    "The conversation quickly devolves into jokes about setting up an app that automatically texts your friends to cancel when the stars aren’t in position for your hangout."
    "Your friends won’t always be in the mood to help you figure out your stuff, but Farah is always up for a decaf latte and a terrible pun."
    "When you’re both ready to go home, you still need some time to think things through, so you head to the park."

    menu:
        "Take a walk.":
            jump walk_in_the_park

label cafe_rain_late:
    show farah neutral right

    Farah "Yeah, she told me. I hope you two work things out."

    menu:
        "Wait, she told you we had a fight?":
            show farah exasperated right

            Farah "I’ve known Rain my whole life, of course she tells me when she’s upset."

            show farah neutral right

            Farah "Listen, I love you, but we’ve already lost some valuable hangout time, so I don’t want to play mediator right now."
            Farah "Can we just enjoy our coffee?"
            pass

        "I’ll talk to Rain later. I just need a break.":
            pass

    show farah neutral right

    "You came here to spend time with Farah, so that’s exactly what you do."

    hide farah
    show farah cat pics with easeinright

    "Farah tells you all about their new cat and how it’s getting along with their old cat."
    "A break is exactly what you needed."

    hide farah with dissolve

    "After you and Farah have exhausted every cat-related line of conversation for the week, they head home and you go for a walk in the park."

    menu:
        "To the park!":
            jump walk_in_the_park
