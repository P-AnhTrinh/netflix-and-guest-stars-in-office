#1. Load data into a dictionary
years = [i for i in range(2011,2021,1)]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
movie_dict = {"years":years, "durations":durations}

#2. Creating a DF from a dictionary
import pandas as pd
durations_df = pd.DataFrame.from_dict(data = movie_dict)
print(durations_df)

#3. A visual inspection 
