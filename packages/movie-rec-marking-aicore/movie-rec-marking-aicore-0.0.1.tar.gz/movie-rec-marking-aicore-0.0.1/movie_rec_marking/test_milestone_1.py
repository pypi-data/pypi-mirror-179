def check_length(selected_option):
    # Check that the length of the movie list is correct
    if selected_option != 250:
        print("The length of the movie list is incorrect, remember that the list of movies is in the variable called 'movies'")
        print('Please, try again, and don\'t continue until you get the correct length')
        return False
    else:
        print('Great! The length of the movie list is correct - 250')
        print('You can continue to the next task')
        return True
