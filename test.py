# LCR
# Using regex to find flight information
import re

# Function takes an html file, and two cases.
def regex(html_doc, case1, case2):
    # Searching for case1
    x = re.search(case1, html_doc)
    # Group these cases
    x = re.search(case1, html_doc).group()
    # Search these cases for case2
    y = re.search(case2, x)
    # Group the remaining cases
    y = re.search(case2, x).group()
    # Return cases
    return y
