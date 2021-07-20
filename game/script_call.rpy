label call_rain:
    scene bg park

    "You decide you don’t want to let this stew any longer."
    "You have your phone on you."
    "Phone calls are the worst way to communicate, but one of the only ways to talk to your flatmate directly without the risk of your tone of voice being misinterpreted."
    "Time for a call."

    Rain "What is it, Payton? I don’t have time to talk right now."

    menu:
        "Does that mean “I don’t want to talk?” as usual?":
            jump call_rain_a

        "I wanted to talk things out, but it can wait.":
            jump call_rain_b

label call_rain_a:
    Peyton "Does that mean “I don’t want to talk?” as usual?"

    Rain "Yes, but you don’t have to be a dick about it."

    menu:
        "You’re right, I’m sorry. I just want to stop avoiding this.":
            jump call_rain_a1

        "You always avoid confrontation! No wonder we fight.":
            Peyton "You always avoid confrontation! No wonder we fight."
            jump call_narration

label call_rain_a1:
    Peyton "You’re right, I’m sorry. I just want to stop avoiding this."

    Rain "I know, I know, I’m being a dick too."
    Rain "I hate these kinds of conversations, but I don’t want to stay mad."
    Rain "Let’s talk tonight, over dinner."
    Rain "It’s easier for me to talk when there’s food around to focus on."

    menu:
        "Sounds good.":
            Peyton "Sounds good. I’ll make lasagna."
            jump end_2

        "That's not good enough.":
            Peyton "That’s not good enough. You’ll still be distracted."
            jump call_narration

label call_rain_b:
    Peyton "I wanted to talk things out, but it can wait."

    Rain "Good, I’m glad."
    Rain "I do want to talk things out, Payton."
    Rain "It just makes me nervous when we fight."

    menu:
        "Still?":
            Peyton "Still? You’ve known me forever! Get over yourself."
            jump call_narration

        "I know, but we have to meet in the middle.":
            Peyton "I know, but we have to meet in the middle."

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