# LCR

# Function to format the string representation of a bytes string back into an actual bytes object
def strip(string):
    # Remove b' prefix
    ct1 = string.lstrip(string[0:2])
    # Remove 's
    ct2 = ct1.strip("'")
    # Remove "s
    ct3 = ct2.strip('"')
    # Return reformatted string
    return ct3
