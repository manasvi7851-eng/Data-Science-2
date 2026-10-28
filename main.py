import pandas as pd
print("Panda series")
scores = [90500,87200,76400,65100,54800]
players = pd.Series(scores,index = ["Sam","Dia","Ray","Alex","Sia"])
print(players)
print(players["Alex"])
print(players.max())
print(players.min())
print(players.mean())
print("======")
print("Data frame")
data = {
    "players":["Sam","Dia","Ray","Alex","Sia"],
    "scores" : [90500,87200,76400,65100,54800],
    "level":[52,42,32,22,12],
    "wins":[500,400,300,200,100]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[2:4])
data_set = pd.read_csv("players.csv")
print(data_set.head(4))
print(data_set.tail(3))
print(data_set.info())
