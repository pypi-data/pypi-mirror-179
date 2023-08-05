# Hangman Marking System

> This is the marking system for the Hangman project. To learn more about the marking system, check out the [marking system README](../README.md).

This file contains just the messages left to the user when the tests fail. The tests are defined in the [marking system package](https://pypi.org/project/hangman-marking-aicore/).

## Table of contents

- [Hangman Marking System](#hangman-marking-system)
  - [Table of contents](#table-of-contents)
  - [Messages](#messages)
    - [Milestone 1](#milestone-1)
    - [Milestone 2](#milestone-2)
    - [Milestone 3](#milestone-3)
    - [Milestone 4](#milestone-4)
    - [Milestone 5](#milestone-5)

## Messages

Each milestone has multiple tasks, and each task has multiple assertions. Each assertion leaves a feesback so the user knows what is wrong with their code.

This section includes the messages left by milestone.

> Tests use AST in order not to run the code so it avoids potential errors such as infinite loops.

### Milestone 1

Milestone 1 consists of creating the repository, so if the action runs, that means the repository was created correctly. Thus, no need for feedback.

### Milestone 2

The tests in this milestone are split into two files:

- `test_milestone2_p1.py`: Checks the presence of `milestone_2.py`
- `test_milestone2_p2.py`: Checks the code in `milestone_2.py`. This file has multiple tests, each one checking a different task.
    - Task 1: Define the list of possible words:
        - Assertion 1: Check that the variable `word_list` is defined
            - Message: `The word_list variable is not defined, if you have defined it, make sure the name is correct and it is in milestone_2.py`
        - Assertion 2: The list of possible words is a list
            - Message: `The word_list variable is not a list`
        - Assertion 3: The list of possible words has at least 5 words
            - Message: `The word_list variable needs to have at least 5 words in it`
    - Task 2: Choose a random word from the list. _At this point, if the first test didn't pass, the tests here will fail, but it won't matter for the system_
        - Assertion 1: Checks that the `random` module is imported
            - Message: `The random module is not imported in milestone_2.py. Make sure you import it to pick a random word from the list`
        - Assertion 2: Checks that the `random.choice` function is called
            - Message: `The random.choice function is not called in milestone_2.py. Use it to pick a random word from the list`
        - Assertion 3: Check if the output is assigned to the `word` variable
            - Message: You have not assigned the output of the random.choice function to the word variable. If you have assigned the output to a variable, make sure the name of the variable is "word"
        - Assertion 4: Check if the user is using the print function
            - Message: You have not used the print function to print the word to the user. Use it to print the word to the user
    - Task 3: Ask the user for an input
        - Assertion 1: Check if the user has assigned the output of the input function to the guess variable
            - Message: You have not assigned the output of the input function to the guess variable. If you have assigned the output to a variable, make sure the name of the variable is "guess"
        - Assertion 2: Check if the user has called the input function
            - Message: You have not used the input function to ask the user for an input. You can call it by typing input("Your message "). If you have called it, make sure you have assigned it to a variable
    - Task 4: Check that the input is a single character
        - Assertion 1: Check if the user checks whether the guess has a length of 1
            - Message: You have not checked whether the guess has a length of 1. Use the len function to check the length of the guess, and use "==" to check if it is equal to 1. If you have done it, make sure it is included in an if statement
        - Assertion 2: Check if the user checks whether the guess is a letter
            - Message: You have not checked whether the guess is a letter. Use the isalpha function to check if the guess is a letter, and use "==" to check if it is equal to True. If you have done it, make sure it is included in an if statement
    - Task 5: Start documenting your experience
        - Assertion 1: Check if the user has created a file called `README.md`
            - Message: You should have a README.md file in your project folder
        - Assertion 2: Check if the `README.md` file has at least 500 characters
            - Message: The README.md file should be at least 500 characters long

### Milestone 3

Same as milestone 2, the tests are split into two files:

- `test_milestone3_p1.py`: Checks the presence of `milestone_3.py`
- `test_milestone3_p2.py`: Checks the code in `milestone_3.py`:
    - Task 1: Iteratively check if the input is a valid guess
        - Assertion 1: Check if the code has a `while` loop
            - Message: You should use a while loop to ask the user for a letter
        - Assertion 2: Check if the `while` loop has a True condition
            - Message: You should use True as the condition for the while loop
        - Assertion 3: Check if there is a break keyword in the `while` loop
            - Message: You should use "break" to exit the while loop when the user enters a valid letter
        - Assertion 4: Check if the `while` loop has an if statement
            - Message: You should have at least one if statement inside the while loop to check that the entered input is a single letter
    - Task 2: Check whether the guess is in the word
        - Assertion 1: Check if the user has used the `in` keyword
            - Message: You should use an if statement to check if the letter entered by the user is in the word. Remember that the input should be stored in a variable called "guess" and the randomly picked word should be stored in a variable called "word". You can use the "in" operator to check if a character is in a string. If you think you have done it correctly, remember to use the right indentation for the if statement and just a single space between the "if" keyword and the condition
        - Assertion 2: Check that the user has an `else` statement
            - Message: The if statement should have an else statement associated with it and placed after it
        - Assertion 3: Checks that the user prints something out when the guess is in the word:
            - Message: You should print a message when the letter is in the word, therefore, inside the if statement you should have a print function
        - Assertion 4: Checks that the user prints something out when the guess is not in the word:
            - Message: You should print a message when the letter is not in the word, therefore, inside the else statement you should have a print function
    - Task 3: Create functions to run the checks
        - Assertion 1: Check if the user has created a function called `ask_for_input`
            - Message: You should define a function called "ask_for_input"
        - Assertion 2: Check if the user has created a function called `check_guess`
            - Message: You should define a function called "check_guess"
        - Assertion 3: Check if the user has included a parameter in the `check_guess` function
            - Message: You have to include a parameter for the check_guess function. You can do it by adding a variable within the parentheses

### Milestone 4

Same as milestone 2, the tests are split into two files:
- `test_milestone4_p1.py`: Checks the presence of `milestone_4.py` and the pressence of the Hangman class
- `test_milestone4_p2.py`: Checks the code of `milestone_4.py`:
    - Task 1: Create the class
        - Assertion 1: Check if word_list is defined as an attribute and its value is correct
            - Message: You have not defined the word_list attribute in your Hangman class
        - Assertion 2: Check if the `word` attribute is defined and its value is correct
            - Message: You have not defined the word attribute in your Hangman class. Remember that an attribute has to be preceded by "self"
        - Assertion 3: Check that the `word` is a random word from the `word_list`
            - Message: The word attribute should be set to a random word from the word_list attribute
        - Assertion 4: Check if `word_guessed` is defined
            - Message: You have not defined the word_guessed attribute in your Hangman class. Remember that an attribute has to be preceded by "self"
        - Assertion 5: Check if `word_guessed` has the right value
            - Message: The word_guessed attribute should be a list of underscores with the same length as the word attribute'
        - Assertion 6: Check if num_letters is defined
            - Message: You have not defined the num_letters attribute in your Hangman class. Remember that an attribute has to be preceded by "self"
        - Assertion 7: Check if num_letters has the right value
            - Message: The num_letters attribute should be the number of UNIQUE letters in the word attribute. You can check the unique letters in a string by converting the string to a set
        - Assertion 8: Check if num_lives is defined
            - Message: You have not defined the num_lives attribute in your Hangman class
        - Assertion 9: Check if num_lives has the right value
            - Message: The num_lives attribute should be set to the value of the num_lives argument passed to the __init__ method
        - Assertion 10: Check if list_of_guesses is defined
            - Message: You have not defined the list_of_guesses attribute in your Hangman class. Remember that an attribute has to be preceded by "self"
        - Assertion 11: Check if list_of_guesses has the right value
            - Message: The list_of_guesses attribute should be an empty list
    - Task 2: Create methods for running the checks (This test is decorated, so if it takes too long to run, it raises an issue)
        - Assertion 1: Check if  a method called 'check_guess' exists
            - Message: You have not defined a method called "check_guess" in your Hangman class. Remember that, in order to define a method, you have to use the "def" keyword followed by the method name
        - Assertion 2: Check that the check_guess method has the correct number of parameters (2)
            - Message: The check_guess method should have 2 parameters: self and guess. Additionally, make sure you have defined the parameters in the correct order
        - Assertion 3: Check that the first parameter of the check_guess method is self
            - Message: The first parameter of the check_guess method should be "self"
        - Assertion 4: Check that the check letter prints the right message when the guess is in the word
            - Message: The check_guess method should print "Good guess! {guess} is in the word.". If you think you have defined the method correctly, make sure you are printing the correct string (same whitespace, capitalization, etc.)
        - Assertion 5: Check that the ask_for_inpit method exists
            - Message: You have not defined a method called "ask_for_input" in your Hangman class. Remember that, in order to define a method, you have to use the "def" keyword followed by the method name
        - Assertion 6: Check that the ask_for_input method has the correct number of parameters (1)
            - Message: The ask_for_input method should have 1 parameter: self.
        - Assertion 7: Check that the ask_for_input method calls the check_guess method
            - Message: The ask_for_input method should call the check_guess method with the user input as the guess parameter. If you think you have defined the method correctly, make sure you are calling the check_guess method with the correct parameter, and that you are printing "Good guess! {guess} is in the word."
        - Assertion 8: Check that the code checks that a letter was already tried
            - Message: The ask_for_input method should print "You already tried that letter!" if the user tries a letter that has already been guessed. If you think you have defined the method correctly, make sure you are printing the correct string (same whitespace, capitalization, etc.)
        - Assertion 9: Checks that the list of guesses attribute is updated after each input
            - Message: The list_of_guesses attribute should be updated after each guess. Make sure you are appending the guess to the list_of_guesses attribute
        - If the test takes more than 10 seconds, most likely there is an infinite loop in the code. In this case, the test raises an issue:
            - Message: The ask_for_input method is taking too long to run. Make sure you don\'t have an infinite loop in your code
    - Task 3: Define what happens if the letter is in the word
        - Assertion 1: Check the number of lives is not updated if the letter is in the word
            - Message: The num_lives attribute should not change if the user guesses a letter that is in the word
        - Assertion 2: Check that the list of guesses is updated after each guess
            - Message: The list_of_guesses attribute should be updated after each guess. Make sure you are appending the guess to the list_of_guesses attribute
        - Assertion 3: Check that the word_guessed attribute is updated if the letter is in the word
            - Message: The word_guessed attribute should be updated after each correct guess. Make sure you are updating the correct index of the list, and if there are repeated letters, you are updating all of them
        - Assertion 4: Check that the num_letters attribute is updated if the letter is in the word
            - Message: The num_letters attribute should be updated after each correct guess. It should be decreased by 1 if you guess a letter correctly. Make sure you are updating the attribute correctly
    - Task 4: Define what happens if the letter is not in the word
        - Assertion 1: Check that the user prints 2 lines if the letter is not in the word
            - Message: Your Hangman class should print at least 2 different lines when the user guess a letter incorrectly. These are "Sorry, {letter} is not in the word.", and "You have {num_lives} lives left.". Additionally, make sure that you print them in the right order
        - Assertion 2: Check that the user prints 'Sorry, z is not in the word.' if the letter is not in the word
            - Message: The first line printed when the user guesses a letter incorrectly should be "Sorry, {letter} is not in the word.". Make sure you are printing the correct string (same whitespace, capitalization, etc.)
        - Assertion 3: Check that the user prints 'You have {x} lives left.' if the letter is not in the word
            - Message: The second line printed when the user guesses a letter incorrectly should be "You have {num_lives} lives left.". Make sure you are printing the correct string (same whitespace, capitalization, etc.)
        - Assertion 4: Check that the num_lives attribute is updated if the letter is not in the word
            - Message: The num_lives attribute should be decreased by 1 if the user guesses a letter that is not in the word
        - Assertion 5: Check that the list of guesses is updated after each guess
            - Message: The list_of_guesses attribute should be updated after each guess. Make sure you are appending the guess to the list_of_guesses attribute'

    - Task 5: Update your documentation
        - Assertion 1: Check the pressence of a README.md file
            - Message: You should have a README.md file in your project folder
        - Assertion 2: Check that the README is at least 1500 characters long
            - Message: The README.md file should be at least 1500 characters long
### Milestone 5

There are two test files for this milestone:
- `test_milestone5_p1.py`: Checks the presence of `milestone_5.py`, the pressence of the class and the pressence of the play function
- `test_milestone5_p2.py`: Checks the functionality of the play function
    - Task 1: Code the logic of the game
        - Assertion 1: Check if the script prints a congratulation message upon winning the game:
            - Message: The play_game function should print "Congratulations. You won the game!" when the user wins the game. If you are not sure what is wrong, try to run the play_game function with the word "banana" and the following inputs: "b", "a", "n"
        - Assertion 2: Check if the script prints a game over message upon losing the game:
            - Message: The play_game function should print "You lost!" when the user loses the game. If you are not sure what is wrong, try to run the play_game function with the word "banana" and the following inputs: "z", "w", "x", "y", "c"
        - If the code takes too long to run, the test raises an issue:
            - Message: Your code is taking too long to run. Make sure you are not using infinite loops. If there are no infinite loops, try to set the number of lives to a number lower than 5
    - Task 2: Document your experience
        - Assertion 1: Check the pressence of a README.md file
            - Message: You should have a README.md file in your project folder
        - Assertion 2: Check that the README is at least 2000 characters long
            - Message: The README.md file should be at least 2000 characters long