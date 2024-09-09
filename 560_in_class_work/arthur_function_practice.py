def message ():
    """this is a docstring and really it's just a comment"""
    print ('I am Arthur')
    print ('King of the Britons')
message ()

#you gotta make sure the second message is NOT indented! this is a void function

def message (king_name):
    print ('I am', king_name)
    print ('King of the Britons')
message ('Henry VIII')

#now you have a parameter which allows me to add any king I like with 'king_name'. The variable is added in the code in the first print line, and then in the last message line I call the message function and pass the argument (this is a lot of terms)

def message (ruler_name, kingdom):
    print ('I am', ruler_name)
    print ('King of the', kingdom)
message ('Mufasa', 'Jungle')

# these parameters are POSITIONAL. They go in the order you put them in (remember this for mad libs)

#now we're gonna deal with default values
def message (pharoah_name, land = 'Egypt'):
    print ('I am', pharoah_name)
    print ('Pharoah of', land)
message ('Tut')
message ('Ramesses')
message ('Hatshepsut')
#so now it uses Egypt for all the kingdoms, and I can put in multiple names for the pharoah and it'll output all them very cool

