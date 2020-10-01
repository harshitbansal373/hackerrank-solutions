# problem--
# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, S
# .
# Both players have to make substrings using the letters of the string S
#
# .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string
#
# .
#
# For Example:
# String
# = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# Your task is to determine the winner of the game and their score.
#
# Input Format
#
# A single line of input containing the string
# .
# Note: The string will contain only uppercase letters:
#
# .
#
# Constraints
#
#
# Output Format
#
# Print one line: the name of the winner and their score separated by a space.
#
# If the game is a draw, print Draw.
#
# Sample Input
#
# BANANA
#
# Sample Output
#
# Stuart 12

#code is here

def minion_game(string):
    # your code goes here
    s= 0
    k = 0
    for i in range(len(string)):
        if string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O'             or string[i] == 'U':
            k+=len(string)-i
        else:
            s+=len(string)-i
    if s == k:
        print('Draw')
    elif k>s:
        print("Kevin "+ str(k))
    else:
        print("Stuart "+ str(s))
