# This program will take information from a games.txt file with four defined categories, and print a table of the info

# Reads from a file named games.txt, and adds each line to a list
# Produces a list of lists
def getGames():
    with open ("games.txt") as games:
        lines=games.readlines()

    gameList=[]
    for line in lines:
        line=line.rstrip() # removes whitespace
        correctedLine=line.replace('Â','') # removes incorrect character from formatting
        gameList.append(correctedLine.split(',')) # divides line into a list and adds to gameList

    return gameList

# Establish the basic "width" variables for use in the table
# A width is established for each category, and updated with the max length from each "column" in the table
# This is used to extend the table to ensure each column will be the correct width in the final output
def formTable(gameList):
    gameWidth=0
    relWidth=0
    devWidth=0
    priceWidth=0

    for line in gameList: # for each "category", check the length of the string and update corresponding category if larger
        for column in enumerate(line):
            if column[0] == 0:
                if len(column[1]) > gameWidth:
                    gameWidth=len(column[1])
            elif column[0] == 1:
                if len(column[1]) > relWidth:
                    relWidth=len(column[1])
            elif column[0] == 2:
                if len(column[1]) > devWidth:
                    devWidth=len(column[1])
            elif column[0] == 3:
                if len(column[1]) > priceWidth:
                    priceWidth=len(column[1])

    return gameWidth, relWidth, devWidth, priceWidth

# Using the gameList and category widths, prints out the table of information
# The category widths are used to ensure all cells are evenly spaced
def printTable(gameList, gameWidth, relWidth, devWidth, priceWidth):
    # establishes the 'border' to use for the table with the relevant line widths
    border=("+" + "-"*(gameWidth + 2) + "+" + "-"*(relWidth+2)+"+"+"-"*(devWidth+2)+"+"+"-"*(priceWidth+2)+"+")
    print(border)

    # For each element of each list in gameList, checks which category it belongs to and prints to the table
    # This is quite ungainly - could definitely be optimised by pulling the length check into a function
    for line in gameList:
        for column in enumerate(line):
            if column[0] == 0:
                tempGame=column[1] # using a temp string to allow concatenating the space, for correct width
                if len(column[1]) < gameWidth:
                    while len(tempGame) < gameWidth:
                        tempGame = tempGame + " "
                print("| "+tempGame + " ",end='')
            elif column[0] == 1:
                tempRel=column[1]
                if len(column[1]) < relWidth:
                    while len(tempRel) < relWidth:
                        tempRel = tempRel + " "
                print("| "+ tempRel + " ",end='')
            elif column[0] == 2:
                tempDev=column[1]
                if len(tempDev) < devWidth:
                    while len(tempDev) < devWidth:
                        tempDev=tempDev+" "
                print("| " + tempDev + " ",end='')
            elif column[0] == 3 and column[1] == "Price":
                tempPrice=column[1]
                if len(tempPrice) < priceWidth:
                    while len(tempPrice)<priceWidth:
                        tempPrice = tempPrice + " "
                print("| " + tempPrice + " |")
                print(border)
            elif column[0] == 3 :
                tempPrice=column[1]
                if len(tempPrice) < priceWidth:
                    while len(tempPrice)<priceWidth:
                        tempPrice = tempPrice + " "
                print("| " + tempPrice + " |")
    print(border)

def main():
    gameList = getGames()
    gameWidth, relWidth, devWidth, priceWidth = formTable(gameList)
    printTable(gameList, gameWidth, relWidth, devWidth, priceWidth)

main()
