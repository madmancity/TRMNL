# LCR
# Airline code conversion
from main import iata, icao

# Convert ICAO to IATA and convert IATA to ICAO, depending on the length of the string inputted
def standard(al):
    index = 0
    # If code is IATA, swap with corresponding ICAO code
    if len(al) == 2:
        for ind, i in enumerate(iata):
            if i == al:
                index = ind
                break
        final = icao[index]
    # If code is ICAO, swap with corresponding IATA code
    else:
        for ind, i in enumerate(icao):
            if i == al:
                index = ind
                break
        final = iata[index]
    # Return swapped code
    return final
