import csv

#CSV format converter used to convert bill of materials in CSV format 
#to workable txt format where it lists all the parts and their respective
#items that they are related to. It also removes all other irrelevant
#information which are not neede when viewing an parts list

#CSV Converter
#Version 1.0
#Author: Wade Huang
#Date: July 10th


with open('bom2.csv') as csvfile:
    read = csv.reader(csvfile, delimiter=',') #Separates all values by commas
    data = [] #initialies Array
    num = 1 #initializes integer variable
    for row in read:#Skips lines (ie. line where it specifies auther, date, etc.) until
                    #it comes to the header where it specifies what each values are for
                    #Converts all of the rows of data into the a 2d array that represents a table
        if "Ref Des" in row and "Item Number" in row:
            num = 2
        if num == 2:
            data.append(row)
    temp = 0 #initializes integer variable
    while data[0] is not "Res Def" and data[1] is not "Item Number": #When "Res Def" and "Item Number" are
                                                                     #not the only headers, that header
                                                                     #is removed.
     for i in data[0]: #Select that element in the first row of the array (the header)
                       #if that is not "Res Def" or "Item Number"
                       #That number is stored to be used
         if "Res Def" not in i or "Item Number" not in i:
             temp = data[0].index(i)
     for x in data: #Removes the entire column that was indicated previously to not be "Res Def" or "Item Number"
         del x[temp]
    txtfile = open("converted bom", "w+") #Creates a file named "converted bom"
    for x in data:#Since the part number are either separate by common (ie. G12,G29) or if there a multiple in a 
                  #row, done through a hyphen (G12-G29), the array element that has the part numbers will be converted
                  #to an array by itself. Since each item is separated by a comma, the "splitter" are comams
        tempArr = x[1].split(",")
        for y in tempArr:
            if "-" in y:#If one of the "range of parts" are found (ie. the G12-G29), the letter is removed and stored and the number is used
                        #as a range in the for loop where all the numbers are converted into a string, combined with the letter, and put
                        #into the array
                letter = y[0]
                tempStr = y.replace(letter, "")
                tempArr2 = tempStr.split("-")
                for p in range(int(tempArr2[0]), int(tempArr2[1])+1):
                    tempArr.append(letter+str(p))
        for k in tempArr:#Prints all the values in the array to the text file except for the ones that are "a range of parts" 
                         #since all the parts have been added in the array as individual parts
            if "-" not in k:
                txtfile.write(k + " " + x[0] + "\n")
