#this is a mad lib example using functions

def madlib(adj_1, noun_1, noun_2, verb_1, adv_1, adj_2, noun_3, verb_2, adv_2, verb_3, adj_3):
    '''mad lib function'''            #docstring must be indented

    story = f'''
Captain Kirk stood on the {adj_1} bridge of the Starship {noun_1}, staring at the {noun_2} on the viewscreen. "Spock, can you {verb_1} the situation?" he asked, his voice {adv_1} calm. Spock raised a {adj_2} eyebrow. "It appears the {noun_3} is attempting to {verb_2} us," he replied {adv_2} . Without hesitation, Kirk turned to Scotty. "We need to {verb_3} the {adj_3} engines, or we'll never escape!"
'''
    return story
output_story = madlib('shiny', 'Python', 'zucchini', 'assess', 'impressively', 'Vulcan', 'gourd', 'mate with', 'calmly', 'reverse', 'polarity of the')
print (output_story)