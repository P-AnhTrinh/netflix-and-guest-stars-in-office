import pandas as pd
import matplotlib.pyplot as plt

office_episode = pd.read_csv("datasets/office_episodes.csv")
office_episode.head(10)

#color scheme reflecting the scaled ratings of each episode
colors = []
for lab, row in office_episode.iterrows():
    if row["scaled_ratings"] < 0.25:
        colors.append("red")
    elif 0.25 <= row["scaled_ratings"] < 0.5:
        colors.append("orange")
    elif 0.5 <= row["scaled_ratings"] < 0.75:
        colors.append("lightgreen")
    elif row["scaled_ratings"] >= 0.75:
        colors.append("darkgreen")
colors[:10]

#sizing sytem guest appearances have a marker size of 250 and episodes without are sized 25
size = []
for lab, row in office_episode.iterrows():
    if row["has_guests"] == True:
        size.append(250)
    else:
        size.append(25)
size[:10]

#scatter plot
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(11,7))

for color in ['red', 'orange', 'lightgreen', 'darkgreen']:
    plt.scatter(office_episode["episode_number"], office_episode["viewership_mil"], c=color, s=size)
    if color == "red": 
        plt.scatter(office_episode["episode_number"], office_episode["viewership_mil"], 
                    c=color, s=size, label = "rating < 0.25")
    elif color == "orange":
        plt.scatter(office_episode["episode_number"], office_episode["viewership_mil"], 
                    c=color, s=size, label = "0.25 <= rating < 0.5")

    elif color == "lightgreen":
        plt.scatter(office_episode["episode_number"], office_episode["viewership_mil"], 
                    c=color, s=size, label = "0.5 <= rating < 0.75")
    elif color == "darkgreen":
        plt.scatter(office_episode["episode_number"], office_episode["viewership_mil"], 
                    c=color, s=size, label = "rating >= 0.75")

plt.legend()
plt.scatter(office_episode["episode_number"], office_episode["viewership_mil"], c=colors, s=size, label = color)
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")
plt.show()

guest_stars_df = office_episode[office_episode["has_guests"]==True]
guest_stars_df.head(10)

highestView = max(guest_stars_df['viewership_mil'])
guest_stars_most_watched_df = guest_stars_df[guest_stars_df['viewership_mil']==highestView]
top_stars_list = guest_stars_most_watched_df["guest_stars"]
print(top_stars_list)