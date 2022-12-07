# LCR
# Main Functions, data, and tkinter GUI
import tkinter as tk
from scramble import retlist, scramble, descramble
from strip import strip
from test import regex
from crypt import encrypt
from crypt import decrypt
from byteify import tobyte
from tkinter import filedialog
import webbrowser
import requests


# IATA and ICAO code arrays with corresponding indices
iata = ['6E','AA','AC','AF','AI','AM','AS','AY','AZ','B6','BA','CA','CI','CZ','DL','EI','EK','EY','FR','G4','HA','IB',
        'JL','KE','KL','LA','LD','LH','LX','LY','MH','MS','MU','NH','NK','NZ','QF','QR','RK','SA','SK','SQ','SU','TG','TK','UA','VN','VS','W6','WS']
icao = ['IGO','AAL','ACA','AFR','AIC','AMX','ASA','FIN','AZA','JBU','BAW','CCA','CAL','CSN','DAL','EIN','UAE','ETD','RYR','AAY','HAL','IBE',
        'JAL','KAL','KLM','LAN','AHK','DLH','SWR','ELY','MAS','MSR','CES','ANA','NKS','ANZ','QFA','QTR','RKH','SAA','SAS','SIA','AFL','THA','THY',
        'UAL','HVN','VIR','WZZ','WJA']

# Function that reformats the ciphertext string to bytes, then sends it to be decrypted
def tokenize(event):
    # Prompt user to select file from system
    filename = filedialog.askopenfilename()
    # Open file for reading
    f = open(filename, "r")
    # Set ciptxt equal to the contents of the file
    ciptxt = f.read()
    # Strip the unnecessary parts of the string (b', etc.)
    stripped = strip(ciptxt)
    # Encode string to bytes object
    ciphertxt = stripped.encode('latin-1').decode('unicode_escape').encode('latin-1')
    # Decrypt ciphertext to get scrambled plaintext
    plain = decrypt(ciphertxt)
    # Update label to display scrambled plaintext
    decryptlabel.config(text=plain)
    # Button that prompts user to enter descrambler file (a list of integers formatted as a txt file)
    unscramble = tk.Button(text="Upload descrambler file", command=upload, font=('Helvetica', 12))
    unscramble.grid(column=2, row=8)

# Function that processes user file input and descrambles flight info
def upload(event=None):
    # Prompt user to enter descrambler file
    filename = filedialog.askopenfilename()
    # Open file for reading
    f = open(filename, "r")
    # Format file content to a string
    data = f.readlines()
    # Create list to hold sequence (lists used to avoid confusion between 1s and 11s)
    sequence = []
    # Initiate Counter
    i = 0
    # Iterate through lines
    for line in data:
        i += 1
        # Append contents of each line to sequence list
        sequence.append(line.strip())
    # For loop to reformat list of strings as list of ints
    for i in range(0, 12):
        sequence[i] = int(sequence[i])
    # Retrieve scrambled text from decryptLabel
    scrambled = decryptlabel.cget("text")
    # Descramble it
    descrambled = descramble(sequence, scrambled)
    # Replace the scrambled text with the descrambled flight info string
    decryptlabel.config(text=descrambled)

# Three Functions that open web browser pages

# Opens live air traffic map
def ofa(event):
    webbrowser.open_new_tab('https://flightaware.com/live/')

# Opens airline code guide
def iguide(event):
    webbrowser.open_new_tab('http://www.flugzeuginfo.net/table_airlinecodes_airline_en.php')

# When airline and flight entries are empty, opens search page.
# When airline and flight entries are entered, this formats them into a flight information page url
def flypage(event):
    # Initiate counter variable
    index = 0
    # Retrieve user input
    al = airlineEntry.get()
    flight = flinumEntry.get()

    # Convert code to match 3-Character ICAO format used in FlightAware's urls
    # Detect strings that are IATA codes
    if len(al) == 2:
        # Swap IATA code with corresponding ICAO code
        for ind, i in enumerate(iata):
            if i == al:
                index = ind
                break
        al = icao[index]
    # Add the two strings together
    full = al + flight
    # Compile url
    urlstring = 'https://flightaware.com/live/flight/' + full
    try:
        # Try opening web browser
        webbrowser.open_new_tab(urlstring)
    except:
        # Catch invalid urls
        origlabel = tk.Label(text="Invalid Entry")
        origlabel.grid(column=3, row=3)

# Function that facilitates encryption process
def getpage(event):
    # Same technique used in flypage
    index = 0
    al = airlineEntry.get()
    flight = flinumEntry.get()

    if len(al) == 2:
        for ind, i in enumerate(iata):
            if i == al:
                index = ind
                break
        al = icao[index]

    full = al + flight
    url = 'https://flightaware.com/live/flight/' + full
    try:
        # Use Regex to scrape specific flight data from html page
        r = requests.get(url)
        # Receive html document as input
        html_doc = r.text
        # Find code for origin airport
        originabr = regex(html_doc, "'origin_IATA', '...'", "'[A-Z]..")[1:]
        # Find code for destination airport
        destinationabr = regex(html_doc, "'destination_IATA', '...'", "'[A-Z]..")[1:]
        # Combine Airline Code, Flight Number, Origin Airport Code, and Destination Airport Code
        # This is the plaintext that will be encrypted
        pt = full + originabr + destinationabr
        # Get a list consisting of numbers 0-11 in a randomized order (used for scrambling plaintext)
        seq = retlist()
        # Map sequence to file
        seqfile = open("C:\\Program Files\\UTPRQ-LGA\\seq.txt", "w")
        for i in seq:
            seqfile.write("%d\n" %(i))
        seqfile.close()
        # Scramble plaintext using sequence
        scrambled = scramble(seq, pt)
        # Convert scrambled string to byte string for encryption
        infotext = tobyte(scrambled)
        # Encrypt infotext using public key
        encrypt(infotext)
        # Give information to user, so they can check if their entry was correct
        origlabel = tk.Label(text=originabr+"->"+destinationabr)
        origlabel.grid(column=3, row=3)
    except:
        # Catch invalid entries
        origlabel = tk.Label(text="Invalid Entry")
        origlabel.grid(column=3, row=3)

# Create GUI Window
window = tk.Tk()
# Window Title
window.title(" TRMNL: A Flight Information Encryption/Decryption Tool by Liam C. Ray ")
# Window Size
window.geometry("850x250")

photo = tk.PhotoImage(file = 'C:\\Users\\liamr\\Pictures\\Picture1.png')
window.wm_iconphoto(False, photo)
# Title within window
newLabel = tk.Label(image=photo)
newLabel.grid(column=0, row=0)

# Air traffic map button, bound to ofa function
atm = tk.Button(text=" Live Air Traffic Map ", font=('Helvetica', 12))
atm.grid(column=1, row=0)
atm.bind("<Button-1>", ofa)

# Flight info button, bound to flypage function
infor = tk.Button(text=" Flight Information ", font=('Helvetica', 12))
infor.grid(column=2, row=0)
infor.bind("<Button-1>", flypage)

# Instruction labels
iLabel1 = tk.Label(text="Enter IATA or ICAO Airline Code (Two or Three Letter or Number Code)")
iLabel1.grid(column=0, row=2)
iLabel2 = tk.Label(text='Enter flight number and hit "Encrypt"')
iLabel2.grid(column=0, row=3)
iLabel3 = tk.Label(text="i.e., [AA] [698]")
iLabel3.grid(column=0, row=4)
iLabel4 = tk.Label(text="------------------------------------------")
iLabel4.grid(column=0, row=5)
ilabel5 = tk.Label(text='Click "Upload Encrypted File" and Select Ciphertext')
ilabel5.grid(column=0, row=7)
ilabel6 = tk.Label(text='Click "Upload Descrambler File" and Select Sequence File')
ilabel6.grid(column=0, row=8)

# Airline code label and entry box
airline = tk.Label(text="Airline Code", fg='blue', font=('Helvetica', 14))
airline.grid(column=1, row=2)
airlineEntry = tk.Entry()
airlineEntry.grid(column=1, row=3)

# Airline code guide button, bound to iguide function
iataGuide = tk.Button(window, text=" Airline Codes Guide ", font=('Helvetica', 12))
iataGuide.grid(column=1, row=4)
iataGuide.bind("<Button-1>", iguide)

# Flight number Label and entry
flinum = tk.Label(text="Flight Number", fg='blue', font=('Helvetica', 14))
flinum.grid(column=2, row=2)
flinumEntry = tk.Entry()
flinumEntry.grid(column=2, row=3)

# Encryption button, bound to getpage function
ecrypt = tk.Button(window, text=" Encrypt Flight Data ", font=('Helvetica', 12))
ecrypt.grid(column=2, row=4)
ecrypt.bind("<Button-1>", getpage)

# Ciphertext label
ciph = tk.Label(text="Ciphertext", fg='blue', font=('Helvetica', 14))
ciph.grid(column=1, row=7)
# Encrypted File entry button, bound to tokenize function
dcrypt = tk.Button(window, text="Upload Encrypted File", font=('Helvetica', 12))
dcrypt.grid(column=1, row=8)
dcrypt.bind("<Button-1>", tokenize)
# Empty decrypted text label to be filled later
decryptlabel = tk.Label(text="  --------------------------", fg='blue', font=('Helvetica', 14))
decryptlabel.grid(column=2, row=7)
# End statement for tkinter
window.mainloop()
