import playingCard

# There's a fair bit of extra work that can be done on this, but I'm conscious of time so submitting while it's working
# i.e. before I break it in half with extra additions!
# Comments:
# - The common hand only reaches three cards - the assignment only says to deal 3, and doesn't mention 2 should be dealt
#   at first. If I knew poker better when I started I'd have noticed this! It breaks every time I try to change it
#   so I'm leaving it well alone for now
# - Additional functions could be added - definitely gameFlow and winningScore should be split into two I think
# - add additional text and checks to show what hands have drawn, what cards constituted the winning hand
# - I'm not happy with how the flush logic works. I think more booleans could be used throughout to check for presence
#   of winning hands i.e. pair is True, straight is True. Could be more elegant/easy to work with and extend/reuse


# Creates and shuffles a deck of cards using playingCard
def pokerDeck():
    deck = playingCard.generateDeck()
    playingCard.shuffleCards(deck)

    return deck


# Deals cards to a preset number of players, and prompts for input for dealing to centre of table (i.e. commonHand)
def gameFlow(deck):
    hands = playingCard.dealCards(deck, 2, 3)
    commonHand = []  # this is the hand shared by all players, which is added to their own hand
    userHand = hands[0]
    playingCard.sortHands(hands)
    scoreDict = {}

    # prompts for input and deals cards to middle deck 3 times
    # quits on input of F/f
    for deals in range(3):
        userDecision = str(input("Your hand is: " + str(userHand) + ". Would you like to (C)ontinue or (F)old?: "))
        while userDecision.lower() != "c" and userDecision.lower() != "f":
            userDecision = input(str("Please enter C to continue, or F to fold: "))
        print(userDecision)
        if userDecision.lower() == "f":
            print("You have decided to fold. Thanks for playing!")
            quit()
        commonHand.append(playingCard.dealACard(deck))
        playingCard.sortHand(commonHand)
        print("The middle has the following cards" + str(commonHand))

    return hands, commonHand, scoreDict


# Makes a list of the numbers only and suits only in each hand, and sorts
# This is used to make score calculation simpler, as some scoring uses suits and some just numbers.
def cardsConvert(hands, commonHand):
    numList = []
    suitList = []

    for hand in hands:
        tempNum = []
        tempSuit = []
        hand.extend(commonHand)
        playingCard.sortHand(hand)
        playingCard.convertFacesToNumbers(hand)
        for card in hand:
            tempNum.append(int(card[1:]))
            tempSuit.append(card[0])
        numList.append(sorted(tempNum))
        suitList.append(sorted(tempSuit))

    # print(numList) verify card numbers
    # print(suitList) verify card suits
    return numList, suitList


# The following functions are all used to determine the presence of any scoring combination of cards
# Scoring is added to a dictionary with the users ID as the key, and the max score they have obtained as the value

# Determines the highest card in each hand
def highCard(numList, scoreDict):
    for hand in enumerate(numList):
        currentHand = hand[1]
        currentPlayer = hand[0]
        scoreDict[currentPlayer] = [1, max(currentHand)]


# Determines if any multi-card hands (pair, three of a kind) are in a users hand, and adds to their score
def pairScore(numList, scoreDict):
    for hand in enumerate(numList):
        currentHand = hand[1]
        currentPlayer = hand[0]
        pair = False
        triple = False
        for card in currentHand:
            duplicateCount = currentHand.count(card)
            if duplicateCount == 2 and scoreDict[currentPlayer][0] <= 2:
                scoreDict[currentPlayer] = [2, card]
                pair = True
            if duplicateCount == 3 and scoreDict[currentPlayer][0] <= 3:
                scoreDict[currentPlayer] = [3, card]
                triple = True
            if triple is True and pair is True and scoreDict[currentPlayer][0] <= 6:
                scoreDict[currentPlayer] = [6, card]
            if duplicateCount == 4 and scoreDict[currentPlayer][0] <= 7:
                scoreDict[currentPlayer] = [7, card]  # ADD CHECK IF HIGHER SCORE PRESENT


# Determines if 5 of one suit are in any users hand
def flush(suitList,scoreDict):
    for hand in enumerate(suitList):
        currentHand = hand[1]
        currentPlayer = hand[0]
        flushPresent = False
        for card in currentHand:
            duplicateCount = currentHand.count(card)
            if duplicateCount > 4:
                flushPresent = True
                scoreDict[currentPlayer] = [5, card]
        return flushPresent


# Determines if hands possess a sequence of 5 cards in a row. Additionally checks if they are of the same suit
def straight(numList, suitList, scoreDict,):
    for hand in enumerate(numList):
        print(hand)
        currentHand = hand[1]
        currentPlayer = hand[0]
        straightCount = 0
        prevCard = 0  # using value that can't match for initial card

        for card in currentHand:
            print(card)
            if card == (prevCard + 1):
                straightCount += 1
                prevCard = card

        if (straightCount >= 4) and flush(suitList[currentHand][1],scoreDict) == True:
            scoreDict[currentPlayer] = [8, card]  # gives highest score for straight in same suite if flush present
        elif straightCount >= 4 and scoreDict[currentPlayer][0] <= 4:
            scoreDict[currentPlayer] = [4, card]


# Calculates the winning score and user based on the values in scoreDict
# I tried to separate this into two functions but for some reason it does not like that, and crashes :(
# Would revisit in future when i have more time!
def winningScore(scoreDict, hands):
    playerScores = list(scoreDict.values())
    playerID = list(scoreDict.keys())
    maxScore = max(playerScores)
    tie = False

    for players in range(len(hands)):
        playingCard.convertNumbersToFaces(hands[players])
        if players == 0:
            print("Your final hand was: " + str((hands[players])))
        else:
            print("Player " + str(players + 1) + " had hand: " + str(hands[players]))

    if playerScores.count(maxScore) > 1:
        tie = True
    else:
        winningPlayer = playerID[playerScores.index(maxScore)]

    scoreExplain = {1: "Highest card", 2: "Pair", 3: "Three of a kind", 4: "Straight", 5: "Flush", 6: "Full House",
                    7: "Four of a kind", 8: "Straight of one suit"}

    if tie:
        print("The game is drawn - more than one player had an identical hand: " + str(scoreExplain[maxScore[0]]))
        print("There are no winners today!")

    elif winningPlayer == 0:
        print("You have won with a score of " + str(maxScore[0]) + "!")
        print("The winning hand was: " + str(scoreExplain[maxScore[0]]))
    else:
        print("Player " + str(winningPlayer + 1) + " wins with a score of " + str(maxScore[0]) + "!")
        print("The winning hand was: " + str(scoreExplain[maxScore[0]]))


def main():
    deck = pokerDeck()
    hands, commonHand, scoreDict = gameFlow(deck)
    numList, suitList = cardsConvert(hands, commonHand)
    highCard(numList, scoreDict)
    pairScore(numList, scoreDict)
    flush(suitList, scoreDict)
    straight(numList, suitList, scoreDict)
    winningScore(scoreDict, hands)


main()
