import random

# Add any long responce here
R_EATING = "I don't like eating anything except your time and space :)"

def unknown():
    responce = ['Could you please re-phrase that?',
                "Sounds about right",
                "What does that mean?",
                "A quick google search might help :)"][random.randrange(4)]
    return responce