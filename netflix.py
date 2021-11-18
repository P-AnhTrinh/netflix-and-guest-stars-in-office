#1. Load data into a dictionary
years = [i for i in range(2011,2021,1)]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
movie_dict = {"years":years, "durations":durations}

#2. Creating a DF from a dictionary
import pandas as pd
durations_df = pd.DataFrame.from_dict(data = movie_dict)

#3. A visual inspection 
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(years, durations)
plt.title("Netflix Movie Durations 2011-2020")
plt.show()

#4. Loading the rest of the data from a CSV
netflix_df = pd.read_csv("datasets/netflix_data.csv")
netflix_df.head(5)

#5. Filtering the movies
netflix_df_movies_only = netflix_df[netflix_df["type"]=="Movie"]
netflix_movies_col_subset = pd.DataFrame(data = netflix_df_movies_only, 
                                         columns = ["title","country", "genre", "release_year", "duration"])
netflix_movies_col_subset.head(5)

#6. Creating a scatterplot
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"])
plt.title("Movie Duration by Year of Release")
plt.show()

#7. Digging deeper
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"]<60]
short_movies.head(20)

#8. Marking non-feature films
colors = []

for index, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == "Children":
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-up":
        colors.append("green")
    else:
        colors.append("black")

#9. Plotting with color
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], color = colors)

plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

plt.show()