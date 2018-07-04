import vezba

maxLines = 13838
lines = int(maxLines*0.7)

ceoFajl = vezba.takeFromCSV('cleaned.csv')
dictionary = vezba.sedamdesetPosto(ceoFajl[0: lines])

