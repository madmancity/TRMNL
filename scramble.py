# LCR

# Plaintext Scrambling Functions
import random
# Function that generates a sequence composed of the numbers 0-11 in random order, used to scramble the plaintext
def retlist():
    # Create two blank lists
    numbersmason = []
    seq = []
    # Put numbers 0-11 into numbers list
    for i in range(0, 12):
        numbersmason.append(i)
    # Seed sequence list with randomly chosen numbers
    for i in range(0, 12):
        # Choose a random number from numbers list
        cho = random.choice(numbersmason)
        # Add it to end of sequence
        seq.append(cho)
        # Remove that number from numbers list so it isn't put into the list twice
        numbersmason.remove(cho)
    # Return the sequence
    return seq

# Scrambling Function
def scramble(seq, string):
    # Convert string to list for easier processing
    listring = list(string)
    # Create empty list to hold scrambled characters
    newstring = []
    # Fill newstring with placeholder characters
    for i in range(0, 12):
        newstring.append("X")
    # Fill spot i in newstring with the character in listring that is at the index corresponding to the number at
    # spot i in seq
    # I.e. if plaintext was UAL427BOSORD and the first number in seq was 5,
    # the first character in newstring would be 7, which is at index 5 in the plaintext
    for i in range(0, 12):
        newstring[i] = listring[seq[i]]
    # Convert scrambled list to string
    scrambled = ''.join(newstring)
    return scrambled

# Descrambling Function, essentially a reverse of the scrambling function
def descramble(seq, string):
    # Convert string to list for easier processing
    listring = list(string)
    # Create empty list to hold descrambled characters
    newstring = []
    # Fill newstring with placeholder characters
    for i in range(0, 12):
        newstring.append("X")
    # Fill the spot in newstring indicated by the ith number in seq with the ith character in listring
    # I.e. if listring was 470LBU2RAOSD, and the first number in seq was five,
    # the fifth character in newstring would be 4
    for i in range(0, 12):
        newstring[seq[i]] = listring[i]
    # Convert descrambled to a string
    descrambled = ''.join(newstring)
    return descrambled
