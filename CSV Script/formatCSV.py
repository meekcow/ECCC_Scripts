"""
This script takes the download .csv file from [redacted] and
creates a new .csv file that is correctly formatted and ready for mapping.

Last modified: September 2018 by Michael Zhang
"""
import os, glob, csv, datetime

# Hardcoded file path locations
# 'file' assumes  there is only one 'raw' downloaded .csv file in the directory
filePath = os.getcwd() + "\\"
file = os.listdir()[0]

def readFile(file):
    """
    Preconditions: Takes in the file name (string) as input. 
    Postconditions: Builds and returns a list of all the relevant records and fields
                    that is required for the creation of the Ship map.
    """
    with open(file, newline = "") as csvfile:
        csvReader = csv.reader(csvfile, delimiter = ",", quotechar = "|")

        # Retrieve only the relevant headers required in the map
        lst = ["SHIP NAME", "CALL SIGN", "Data Date", "LATITUDE", "LONGITUDE", "WX IND"]
        masterLst = [lst]

        # Read and record every row with the exception of additional headers and blank records
        for row in csvReader:
            if(row != []) and (row[0] != "") and (row[0] != "SHIP NAME"):
                lst = [row[0], row[1], row[2], row[3], row[4], row[8]]
                masterLst.append(lst)

    return masterLst

def buildDate():
    """
    Preconditions: N/A.
    Postconditions: Returns a list where the first element is today's year,
                    the second element is today's month, and the third
                    element is today's day.
    """
    # Retrieve today's day from datetime library
    currentDate = datetime.datetime.now().date()
    year = currentDate.year

    # If the numeric value for today's month is single digits,
    # Place a '0' in front as placeholder for formatting
    if(currentDate.month < 10):
        month = "0{}".format(currentDate.month)
    else:
        month = currentDate.month

    # If the numeric value for today's day is single digits,
    # Place a '0' in front as placeholder for formatting
    if(currentDate.day < 10):
        day = "0{}".format(currentDate.day)
    else:
        day = currentDate.day

    return [year, month, day]

def createDir(filePath, date):
    """
    Preconditions: Takes the filePath (string) and the date (list) as input.
    Postconditions: Builds and returns a list of the appropriate directory as the
                    first element and the file directory as the second element.
    """
    # Format the folder and file names based on today's date
    folderName = "{}{}{}".format(date[0], date[1], date[2])
    fileName = "newFile_{}-{}-{}.csv".format(date[0], date[1], date[2])

    # Build the directories
    directory = "{}{}\\".format(filePath, folderName)
    fileDir = "{}{}".format(directory, fileName)

    return [directory, fileDir]
    

"""
Main
"""
# Read records from downloaded .csv file and build the date (list)
records = readFile(file)
date = buildDate()

# Determine file name, directory, and naming of folder/file
directories = createDir(filePath, date)

# Check if the folder exists, if not, create it
if(not os.path.exists(directories[0])):
    os.makedirs(directories[0])
    print("{} does not exist and has been created.".format(directories[0]))
else:
    print("{} already exists. The file will be created in this location.".format(directories[0]))

# Create/overwrite the .csv file and write to it from records
with open(directories[1], "w", newline = "") as csvfile:
    writer = csv.writer(csvfile, delimiter = ",", quotechar = "|", quoting = csv.QUOTE_MINIMAL)

    for record in records:
        writer.writerow(record)

print("\nCompleted.")
