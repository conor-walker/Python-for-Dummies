
# def readCSV():
with open ("list.csv") as emailData:
    header=emailData.readline()
    headerData=header.strip(",,,,,\n").split(",")
    formData = {}
    numRows = 0

    for row in emailData.readlines():
        rowList=row.strip(",,,,,\n").split(",")
        dictRow={}
        for element in rowList:
            dictRow[headerData[rowList.index(element)]]=element
        formData[numRows]=dictRow
        numRows+=1

# return formData, headerData

# def readEmail():
with open ("template.txt") as template:
    # TODO -
    emailForm=""
    for row in template:
        emailForm=emailForm+row
# return emailForm

# def replaceEmail():
for header in range(len(headerData)):
    formField="%%"+headerData[header]+"%%"

for recipient in formData:
    for line in emailForm.splitlines():
        for header in range(len(headerData)):
            formField = "%%" + headerData[header] + "%%"
            if formField in line:
                tempLine= line.replace(formField, formData[recipient][headerData[header]])
                line = tempLine
        print(line)
