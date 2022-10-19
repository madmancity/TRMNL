# LCR
import tkinter as tk
from test import regex
from bs4 import BeautifulSoup

from tkinter import ttk
import webbrowser
import requests
iata = ['6E','AA','AC','AF','AI','AM','AS','AY','AZ','B6','BA','CA','CI','CZ','DL','EI','EK','EY','FR','G4','HA','IB',
        'JL','KE','KL','LA','LD','LH','LX','LY','MH','MS','MU','NH','NK','NZ','QF','QR','RK','SA','SK','SQ','SU','TG','TK','UA','VN','VS','W6','WS']
icao = ['IGO','AAL','ACA','AFR','AIC','AMX','ASA','FIN','AZA','JBU','BAW','CCA','CAL','CSN','DAL','EIN','UAE','ETD','RYR','AAY','HAL','IBE',
        'JAL','KAL','KLM','LAN','AHK','DLH','SWR','ELY','MAS','MSR','CES','ANA','NKS','ANZ','QFA','QTR','RKH','SAA','SAS','SIA','AFL','THA','THY',
        'UAL','HVN','VIR','WZZ','WJA']

 
def ofa(event):
    webbrowser.open_new_tab('https://flightaware.com/live/')


def getpage(event):
    index = 0
    al = airlineEntry.get()
    flight = flinumEntry.get()
    #print(al)

    if len(al) == 2:
        for ind, i in enumerate(iata):
            if i == al:
                index = ind
                break
        al = icao[index]

    #print(flight)
    full = al + flight
    #print(full)
    url = 'https://flightaware.com/live/flight/' + full
    #TODO: Handle Invalid Flight Entry
    #webbrowser.open_new_tab(url)
    r = requests.get(url)
    r.text
    #print(r.text)
    html_doc = r.text
    testlabel = tk.Label(text="Working")
    testlabel.grid(column=3, row=8)
    originabr = regex(html_doc, "'origin_IATA', '...'", "'[A-Z]..")[1:]
    destinationabr = regex(html_doc, "'destination_IATA', '...'", "'[A-Z]..")[1:]
    #acman = regex(html_doc, "'aircraft_make', '******'", "[A-Z].....")
    #print(acman)
    print(originabr)
    print(destinationabr)
    origlabel = tk.Label(text=originabr+"->"+destinationabr)
    origlabel.grid(column=2, row=4)


window = tk.Tk()
window.title(" TRMNL ")
window.geometry("1000x800")
newLabel = tk.Label(text="TRMNL", font=('Helvetica', 14), fg='green')
newLabel.grid(column=0, row=0)
auth = tk.Label(text=" A Flight Information Tool By Liam C Ray", font=('Helvetica', 10), fg='green')
auth.grid(column=1, row=0)
iLabel1 = tk.Label(text="Enter IATA or ICAO Airline Code (Two or Three Letter or Number Code next to flight number)")
iLabel1.grid(column=0, row=3)
iLabel2 = tk.Label(text="Enter flight number")
iLabel2.grid(column=0, row=4)
iLabel3 = tk.Label(text="i.e., [AA] [698]")
iLabel3.grid(column=0, row=5)
iLabel4 = tk.Label(text="(American Airlines Flight 698 From BOS to ORD)")
iLabel4.grid(column=0, row=6)
button = tk.Button(window, text=" Live Air Traffic Map ", font=('Helvetica', 12))
button.grid(column=2, row=0)
button.bind("<Button-1>", ofa)
getInfo = tk.Button(window, text=" Get Flight Info ", font=('Helvetica', 14))
getInfo.grid(column=3, row=3)
getInfo.bind("<Button-1>", getpage)
airline = tk.Label(text="Airline ICAO Code", fg='blue', font=('Helvetica', 14))
airline.grid(column=1, row=2)
iataGuide = tk.Button(window, text=" IATA Airline Codes Guide ", font=('Helvetica', 12))
iataGuide.grid(column=1, row=4)
airlineEntry = tk.Entry()
airlineEntry.grid(column=1, row=3)
flinum = tk.Label(text="Flight Number", fg='blue', font=('Helvetica', 14))
flinum.grid(column=2, row=2)
flinumEntry = tk.Entry()
flinumEntry.grid(column=2, row=3)

window.mainloop()
