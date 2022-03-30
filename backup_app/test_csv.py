import csv
iii=0
with open('predictions_fight.csv', newline='') as csvfile:
    
    reader=csv.reader(csvfile)
    rows=[r for r in reader]
print (rows[9][1])
#print row[88]