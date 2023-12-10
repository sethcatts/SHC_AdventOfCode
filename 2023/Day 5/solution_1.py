#Data
# A B C
# A + C - Destination range
# B + C - Source range
# C     - Range length

#Edge case:  Number does not fall in range -> return that number 

# Given a seed number
# Send to map and return a corresponding map number for that map
# Supply that number to the next map until you get the value of the final map
# Store that number and then return the lowest location number from the list of seed numbers

class map:
    def __init__(drs, srs, rng):
        self.drs = [drs, drs+rng]
        self.srs = [srs, srs+rng]
        self.rng = rng
    def getSeedNumber(seed):
        if(seed not in range(self.srs[0], self.srs[1])):
            return seed
        else:
            return 0

# Create a map class instance for all maps
# Get a location value for all seeds
# Return the lowest seed
