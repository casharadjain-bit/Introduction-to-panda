import pandas as pd
# Part1. create panda series
print("panda series")
scores=[98500,87200,76400,65100,54800,43200,38900,35100]
players=pd.Series(scores,index=["NightWolf","StarBlaze",'PixelKing','CyberFox','IronStorm','GhostRider','LunaStrike','ShadowByte'])
print(players)

# Part2. pandas dataframe
print("pandas data frame")
var={"player":['NightWolf','StarBlaze','PixelKing','CyberFox','IronStorm'],
      "level":[42,38,35,30,27],
      "score":[98500,87200,76400,65100,54800],
      "wins":[210,185,162,140,118]}
var1=pd.DataFrame(var)
print(var1)

# Part3. access rows using LOC
print("access rows using LOC:")
print("row 0:")
print(var1.loc[0])
print("row 2 and 3:")
print(var1.loc[2:3])

# Part4. load leaderboard and view data
print("reading CSV file")
read=pd.read_csv("leaderboard.csv")
print("first 5 rows:")
print(read.head())
print("last 3 rows")
print(read.tail(3))
print(read.info())

# Part5. clean the data
print("cleaning data")
clean=read.dropna()
print(clean)
clean1=read.fillna(0)
print(clean1)