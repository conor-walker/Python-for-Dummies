# This program merges data from a CSV file of set format to an email template, and prints out the resulting emails
# Replacement fields in the template are marked by surrounding %% signs, and correspond to the first row of the CSV
# - i.e. %%FIRST NAME%% is the replacement field for the FIRST NAME column


def readCSV():
    with open ("list.csv") as emailData:
        header=emailData.readline() # reads the first line of the CSV as the header

        # The provided CSV file has 5 commas at the end of each line - headerData separates the line into a list and
        # strips out the trailing commas. This could likely be adjusted to just the new line - I'm not sure if that
        # sequence of commas is actual CSV formatting or a quirk of opening it in a text editor.
        headerData=header.strip(",,,,,\n").split(",")

        formData = {} # initialises an empty dictionary to store field replacements for each row of the CSV
        numRows = 0 # initialised at 0 for filling formData

        # loops through all rows in the file after the header
        for row in emailData.readlines():
            rowList=row.strip(",,,,,\n").split(",") # as with headerData
            dictRow={} # initialises a dictionary to store the data of each row

            # this loop goes through ever element in the row, and saves it to a dictionary with the key of the
            # relevant header - i.e. {FIRST NAME: Alan, EVENT: Basketball game}
            for element in rowList:
                dictRow[headerData[rowList.index(element)]]=element

            formData[numRows]=dictRow # adds the created dictRow to the overall dictionary
            numRows+=1 # iterates numRows to add the new key for the next row

    return formData, headerData


# Reads the email template and saves to a new string
def readEmail():
    with open ("template.txt") as template:
        emailForm=""
        for row in template:
            emailForm=emailForm+row
    return emailForm


# The mail merge logic - this replaces the fields in the email template with the relevant data from the CSV
def replaceEmail(formData, headerData, emailForm):
    # This loop might look a little scary but it's reasonably straightforward - for each email recipient, every line in
    # the email template is checked for the presence of each possible field. If present, these fields are updated with
    # the recipients data
    for recipient in formData:
        for line in emailForm.splitlines():
            for header in range(len(headerData)):
                # goes through every header and converts to the email field format to ensure full coverage of
                # valid fields
                formField = "%%" + headerData[header] + "%%"
                # checks for presence of field in a line, and replaces with the correct CSV data
                if formField in line:
                    tempLine= line.replace(formField, formData[recipient][headerData[header]])
                    line = tempLine # updates the line with the CSV data of the current field
            print(line)  # the assignment doesn't specify what to do with the created emails, so I'm just printing them!


def main():
    formData,headerData=readCSV()
    emailForm=readEmail()
    replaceEmail(formData,headerData,emailForm)


main()
