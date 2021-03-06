import plotly
import pandas as pd
import plotly.express as px

def table_each_team(team_name, y_axis):
    x_axis = []
    for element in range(len(y_axis)):
        x_axis.append(element+1)
    df = pd.DataFrame({'Round': x_axis, 'Cargo Points': y_axis})
    df.to_excel(f".././data/{team_name}.xlsx")

def plot_each_team(team_name, dataframe):
    fig = px.bar(dataframe, x="Round", y="Cargo Points", title=f"Team{team_name}")
    plotly.offline.plot(fig, filename = f".././graphs/{team_name}.html")

df = pd.read_excel('Sacramento Scouting Data.xlsx')
new_df = df[["Team Number", "Final Total Score Including Hanger", "Final Total Score Just Cargo"]]
list_of_teams = new_df["Team Number"].tolist()
score_with_hanger = new_df["Final Total Score Including Hanger"].tolist()
score_just_cargo = new_df["Final Total Score Just Cargo"].tolist()

score = []
no_repeat_teams = set(list_of_teams)

print("team options: ")
print(no_repeat_teams)
team_input = int(input('>'))

counter = 0
for team in list_of_teams:
    if team == int(team_input):
        score.append(score_just_cargo[counter])
    counter += 1

table_each_team(str(team_input), score)
df = pd.read_excel(f".././data/{team_input}.xlsx")
plot_each_team(str(team_input), df)