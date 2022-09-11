"""This is a guessing game in which you get three tries to guess a secret number that is between 1 and 20. You start out with 3 lives and a secret you have to guess. With each wrong guess, the program tells you if your guess was too high or too low and you lose a life. If you guess correctly, you are congratulated and the secret number is revealed. If you guess incorrectly three times in a row, you are informed that you lost, the secret number is revealed and the program wishes you, "Better luck next time!".

Following is what you need to do:

    To create this secret, we'll use the random number module. See this week's exercises for how to import the random module to use the randint() function.
    Display a message to "Guess the secret number".
    Initialize a num_lives variable to 3.
    Create a while loop with a condition of num_lives > 3.
    Inside the while loop:
        Query the user using the input() function for a guess between 1 and 20.
        Convert that number to an integer using the int() function.
        Use an if-elif-else construct to determine if the guess is greater than the secret, less than the secret or equal to the secret. If the guess is greater than the secret, let the user know and decrement the num_lives variable.
        If the guess is not greater than the secret, then use an elif to check if the guess is less than the secret. If that's the case, let the user know and decrement the num_lives variable.
        If the guess is neither greater than the secret nor less than the secret, then the only remaining possibility is that the guess is equal to the secret. This is the else case. Congratulate the user and display a message that includes both the secret number. Use the break statement to exit the while loop.
        The while loop should exit after three incorrect guesses or a correct guess (via the break statement).
    After the while loop, use an if statement to determine if there are any lives remaining. If not, then display a message letting the user know that she/he lost, reveal the secret number and wish the user better luck next time.
"""