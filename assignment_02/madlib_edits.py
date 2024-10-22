# This is a mad lib example using functions.

def madlib(adj_1, noun_1, noun_2, verb_1, adv_1, adj_2, noun_3, verb_2, adv_2, verb_3, adj_3):
    '''mad lib function'''    # Docstring must be indented.

    story = f'''
Captain Kirk stood on the {adj_1} bridge of the Starship {noun_1}, staring at \
the {noun_2} on the viewscreen. "Spock, can you {verb_1} the situation?" he \
asked, his voice {adv_1} calm. Spock raised a {adj_2} eyebrow. "It appears the \
{noun_3} is attempting to {verb_2} us," he replied {adv_2} . Without hesitation, \
Kirk turned to Scotty. "We need to {verb_3} the {adj_3} engines, or we'll never escape!" \
'''
    return story

def get_user_input ():
    '''prompt the user for input into the madlib.'''
    adj_1 = input ("Enter adj ")
    noun_1 = input ("Enter noun ")
    noun_2 = input ("Enter noun ") 
    verb_1 = input ("Enter verb ") 
    adv_1 = input ("Enter adv ")
    adj_2 = input ("Enter adj ") 
    noun_3 = input ("Enter: ")
    verb_2 = input ("Enter: ")
    adv_2 = input ("Enter: ")
    verb_3 = input ("Enter: ")
    adj_3 = input ("Enter: ")

    return adj_1, noun_1, noun_2, verb_1, adv_1, adj_2, noun_3, verb_2, adv_2, verb_3, adj_3

# Get user input
user_input = get_user_input ()

print(madlib(*user_input))
