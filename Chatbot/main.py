import re
import long_responces as long

def message_probability(user_message, recognised_words, single_responce=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user's message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_responce:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def responce(bot_responce, list_of_words, single_responce=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_responce] = message_probability(message, list_of_words, single_responce, required_words)

    # Just some examples
    # Responces ----------------------------------------------------------------------------------------------
    responce('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo', 'yo'], single_responce=True)
    responce('I\'m doing fine, how are you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    responce('Thank you!, ILU too <3', ['i', 'love', 'you'], required_words=['love'])
    responce(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_responce(user_input):
    split_message = re.split(r'\s+|[,;!?.-]\s*', user_input.lower())
    responce = check_all_messages(split_message)
    return responce


# Testing the responce system
while True:
    print('Bot: ' + get_responce(input('You: ')))