from main import iata, icao
def standard(al):
    if len(al) == 2:
        for ind, i in enumerate(iata):
            if i == al:
                index = ind
                break
        final = icao[index]
    elif len(al) == 3:
        for ind, i in enumerate(icao):
            if i == al:
                index = ind
                break
        final = iata[index]
    return final



