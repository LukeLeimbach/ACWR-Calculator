# ========================================================================================================
# Project:               ACWR Calculation Module TEMPLATE VERSION
# Template by:           Luke Leimbach
# Template updated:      04/22/2023
# NOTE: Please don't edit above.
#
# By:    YOUR_NAME
# DATE:  CURRENT_DATE
# 
# NOTE: For places where you need to update a formula, do CTRL+F and look up '# FIXME'.
# Read through the code where I have made comments.
# TEST CODE AT BOTTOM OF FILE.
# 
# METHODS:
# Analyze(CSVFILE) : requires a csv file with data (I use soccer.csv and I'd recommend doing the same)
#  - Calls all methods except toCSV()
# calcWeeklyWork(PLAYER_NUMBER) : requires a player number as argument
#  - Calculates the amount of work done by a player every week and updates 'weeklyWork' dictionary - NEEDS WORK HERE
# calcACWR() : No arguments
#  - Calculates ACWR starting at week 5                                                            - NEEDS WORK HERE
# toCSV(OUTFILE) : OPTIONAL ARGUMENT - take a file path to a csv file that you want written to. LEAVE BLANK for 'out.csv' to appear in current directory (folder)
#  - Writes the ACWR to a CSV file
# main
#  - For unit testing
# ====================================================

import datetime as dt
import pandas as pd

# Player 1: Midfielder
# Player 2: Defender
# Player 3: Defender
# Player 4: Defender
# Player 5: Midfielder
# Player 6: Defender
# Player 7: Defender
# Player 8: Forward
# Player 9: Forward

class Analyze:
    def __init__(self, csv):
        self.df = pd.read_csv(csv)

        # Stores weekly work for each player
        # Data is stored in a dictionary of lists
        # Access list data for each player with 'self.weeklyWork[PLAYER NUMBER]'
        # This returns list of work for each week (eg. '[20, 25, 19, ...]')
        # This is needed to calculate ACWR
        self.weeklyWork = {}

        # Stores ACWR starting from week 5 (index 0)
        # Data is stored in a dictionary of lists
        # Access data same as above
        self.ACWR = {}

        # Stores all the data for each player
        # Access data for each player with 'self.playerData[PLAYER_NUMBER]'
        # to get Panda (pd) data for Player1 for example, use 'self.playerData[1]'
        # NOTE: There is no player 0
        self.playerData = [None]

        # Updates Player Data - NOTE: Don't need to edit
        self._appendPlayerData()

        # Updates weeklyWork Dictionary
        for i in range(1, 10):
            self.calcWeeklyWork(i)

        # Calculates ACWR and updates self.ACWR dictionary
        self.calcACWR()


    # Adds player data to playerData
    # NOTE: Don't need to touch this!
    def _appendPlayerData(self):
        for i in range(1, 10):
            self.playerData.append(self.df.loc[self.df['Player Name'] == f'Player{i}'])


    # 'player' argument is the integer at the end of 'Player Name' (eg. Player1 = 1, Player2 = 2, etc.)
    def calcWeeklyWork(self, player):
        self.weeklyWork[player] = []
        playerData = self.playerData[player]
        playerDataLength = len(playerData)
        startDate = dt.date(2021, 9, 3)
        endWeekDate = startDate + dt.timedelta(days=7)
        work = 0

        # Goes over data from every day with data
        for i in range(playerDataLength):
            dayData = playerData.iloc[i]
            _day = dayData.get("Event Date").split("/")
            day = dt.date(int(_day[2]), int(_day[0]), int(_day[1]))

            # Checks if the current day is past the end of week
            # If needed, sends data to the weeklyWork dictionary and resets work in loop
            if day >= endWeekDate:
                endWeekDate += dt.timedelta(days=7)
                self.weeklyWork[player].append(work)
                work = 0
            
            # NOTE: If you are dividing, make sure not to divide by 0! You can write an if statement to only run calculation if a value is not 0.
            work += (-999) # FIXME: Add work calculation here

        self.weeklyWork[player].append(work)


    # This calculates ACWR
    def calcACWR(self):
        # For every player...
        for i in range(1, 10):
            self.ACWR[i] = []
            weekData = self.weeklyWork[i]
            # For every week played starting at week 4 ... (because before week 4, you can't calculate ACWR)
            for j in range(4, len(weekData)):
                # Your ACWR formula here
                self.ACWR[i].append(-999) # FIXME: Calculation for ACWR here (eg. weekData[j-4]*0.2 + weekData[j-3]*0.4 + ...) or however you want to weight the weeks


    # Writes your data to a csv file. Argument can be a path to a csv file. No argument returns data to 'out.csv' to current directory.
    # NOTE: calling this multiple times will keep adding data to FILENAME.csv. Be sure to delete contents of FILENAME.csv every time this funciton is ran
    def toCSV(self, filename="out.csv"):
        with open(filename, "a") as outFile:
            for i in range(1, len(self.ACWR)+1):
                outFile.write(str(i) + "\n")
                for j in self.ACWR[i]:
                    outFile.write(str(j) + "\n")
        
        outFile.close()

    # If you need to see all data, you can print the Analyze() object (eg. print(Analyze("soccer.csv")))
    def __str__(self):
        return str(print(self.df))
    

# NOTE: Testing Here. Only the code below will run when you run this file.
if __name__ == "__main__":
    analyzer = Analyze("soccer.csv")
    # analyzer.toCSV() # FIXME: to write to a csv file after updating formulas, uncomment this line. NOTE: Check toCSV() method above for more details.
