# Prime loop
menu_option = ''

# Outer loop continues looping until user inputs 'q'
while menu_option != 'e':
    # Prints menu options
    print('''
    Menu:
    a: browse sewing classes
    b: view fabric collection
    e: exit
    ''')
    menu_option = input('enter a letter to continue to your desired information: ')

    if menu_option == 'a':
        print('Classes are organized by age, skill level, and project type!')
    elif menu_option =='b':
        quilt_or_clothe = input ('Do you prefer quilting or sewing clothes? Select q for quilting and c for clothing: ')
        if quilt_or_clothe == 'q':
            print("Welcome! Please browse our extensive collection of cottons and batiks for your next quilt!")
        else:
            print("Welcome! Please browse our collection of cottons, special occasion fabrics, and speciality prints")
    