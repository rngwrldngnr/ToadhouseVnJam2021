label call_rain:
    scene bg park

    if inv.charge:
        jump call_rain_phone_charged
    else:
        jump call_rain_no_phone

label call_rain_no_phone:
    "You decide you don’t want to let this stew any longer."
    "A text message isn’t enough. This requires a phone call."
    "You dig your phone out of your pocket, psyching yourself up for the conversation, and look at the screen."
    "The black screen."
    "Hold on. Did you forget to charge your phone?"
    "Shit. Well, that ruins your mood entirely."
    "Clearly, this is not the time to talk things out."
    "You’ll just have to see if Rain has calmed down a bit by the time she gets home."

    jump end_3

label call_rain_phone_charged:
    "You decide you don’t want to let this stew any longer."
    "You have your phone on you."
    "Phone calls are your least favourite way to communicate, but it’s the only way to talk to Rain right away without the risk of your tone of voice being misinterpreted."
    "You take a short walk to the park, so you can find a place to sit down and call Rain."

    # TODO: This is where the scene should be changed to the park

    Rain "What is it, Payton? I don’t have time to talk right now."

    menu:
        "Does that mean “I don’t want to talk?” as usual?":
            jump call_rain_a

        "I wanted to talk things out, but it can wait.":
            jump call_rain_b

label call_rain_a:
    Payton "Does that mean “I don’t want to talk?” as usual?"

    Rain "Yes, but you don’t have to be a dick about it."

    menu:
        "You’re right, I’m sorry. I just want to stop avoiding this.":
            jump call_rain_a1

        "You always avoid confrontation! No wonder we fight.":
            Payton "You always avoid confrontation! No wonder we fight."
            jump call_narration

label call_rain_a1:
    Payton "You’re right, I’m sorry. I just want to stop avoiding this."

    Rain "I know, I know, I’m being a dick too."
    Rain "I hate these kinds of conversations, but I don’t want to stay mad."
    Rain "Let’s talk tonight, over dinner."
    Rain "It’s easier for me to talk when there’s food around to focus on."

    menu:
        "Sounds good.":
            Payton "Sounds good. I’ll make lasagna."
            jump end_2

        "That's not good enough.":
            Payton "That’s not good enough. You’ll still be distracted."
            jump call_narration

label call_rain_b:
    Payton "I wanted to talk things out, but it can wait."

    Rain "Good, I’m glad."
    Rain "I do want to talk things out, Payton."
    Rain "It just makes me nervous when we fight."

    menu:
        "Still?":
            Payton "Still? You’ve known me forever! Get over yourself."
            jump call_narration

        "I know, but we have to meet in the middle.":
            Payton "I know, but we have to meet in the middle."

            Rain "You’re right."
            Rain "We’ll have a proper conversation when I get back from work."
            Rain "Are you still okay with having dinner ready when I get back?"
            Rain "If you cook, I’ll do most of the talking."

            jump end_2

label call_narration:
    "You hang up on Rain with no small amount of irritation."
    "She always does this!"
    "You know confrontations are scary, but surely Rain knows you better than this?"
    "It makes you sad and angry."

    jump end_3
