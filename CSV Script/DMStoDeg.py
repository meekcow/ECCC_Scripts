## Convert DMS lat/long format to Degrees
## Michael Zhang
## michaelhzhang@hotmail.com
## Last Updated: 06/09/2018

import csv

#print dir(csv)
#help(csv.reader)
#help(csv.writer)

#CSV is binary format so use rb/wb

def dms2dd(dd, mm, ss):
    degrees = abs(float(dd)) + float(mm)/60 + float(ss)/(60*60)
    return degrees

with open('inFile.csv', 'rb') as csvFile, open('outFile.csv', 'wb') as outFile:
    csvObj = csv.reader(csvFile)
    output = csv.writer(outFile)
    headings = next(csvObj)
    for row in csvObj:
        print row
        lat = row[-2]
        lon = row[-1]
        row[-2] = dms2dd(lat[:-6], lat[-5:-3], lat[-2:])
        row[-1] = -1 * dms2dd(lon[:-6], lon[-5:-3], lon[-2:])
        print row
        output.writerow(row)
