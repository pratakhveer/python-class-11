import pandas as pd
import plotly.graph_objects as go
import csv

df = pd.read_csv("data.csv")
name = df.loc[df["student_id"] == "TRL_987"]
print(name)

fig = go.Figure(go.Bar(
    x=name.groupby("level")["attempt"].mean(),
    y=["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation="h"
))
fig.show()
