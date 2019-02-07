## A collection of functions made in Python

import os

def dms2dd(dd, mm, ss):
    ''' Takes degrees(dd), minutes(mm), and seconds(ss) values
        and converts it to decimal degrees of absolute value

        Example: dms2dd(10, 30, 40) '''
    degrees = abs(float(dd)) + float(mm)/60 + float(ss)/(60*60)
    return degrees

def subdirectory(directory, output = '', counter = 0):
    ''' Input [directory] in the following format: 'C:/folder/folder/last'
        or 'C:\\folder\\folder\\last'
        to output a list of all subdirectories of [last]

        Example: subdirectory('C:/what/is/in/here/') '''
    try:
        basename = os.path.basename(directory)
        if '.' in basename:
            return "\t"*counter + "|_____" + basename
        else:
            subdir = os.listdir(directory)
            if not subdir:
                return "\t"*counter + "-----(empty)"
            else:
                for name in subdir:
                    if '.' not in name:
                        print "\t"*counter + "|_____" + name
                        print subdirectory(directory + '/' + name, output, counter+1)
                    else:
                        print subdirectory(directory + '/' + name, output, counter)
                return ''
    except Exception as e:
        pass

def searchDirectory(directory, query):
    ''' Searches a [directory] for all files that contain an input value

        Example: searchDirectory('C:/', '.doc') '''
    try:
        subdir = os.listdir(directory)
        for name in subdir:
            if query in name:
                print directory + '/' + name
            if '.' not in name:
                searchDirectory(directory + '/' + name, query)
    except Exception as e:
        pass

listOfTools = dir()[5:]
listOfTools.remove('os')

#print "Hello World! Below are the following 'tools' available in this CLI, please type 'help(tool_name)' for assistance!"
print listOfTools
