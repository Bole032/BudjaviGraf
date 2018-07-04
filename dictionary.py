import pandas as pd

def takeFromCSV(fajl):
    f = open(fajl, 'r')
    ceoFajl = []
    for row in f:
        ceoFajl.append(row)
    f.close()
    return ceoFajl
    
def sedamdesetPosto(niz):
    dictonary = {}
    for red in niz:
        splitRow = red.split(',')
        if splitRow[1] in dictonary:
            dictonary[splitRow[1]].append(splitRow[2])
        else:
            dictonary[splitRow[1]] = [splitRow[2]]

        if splitRow[2] in dictonary:
            dictonary[splitRow[2]].append(splitRow[1])
        else:
            dictonary[splitRow[2]] = [splitRow[1]]
    return dictonary