# Importing the pandas library to handle data manipulation and analysis
import pandas as pd

# Read in the data from 'schools.csv'
schools = pd.read_csv("schools.csv")

# Display the first few rows of the dataset to get an overview of the data
schools.head()

# Identify schools that excel in math by filtering schools with an average math score of 640 or higher.
# The dataset is then sorted in descending order to list the best performing schools at the top.
best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values("average_math", ascending=False)

# Adding a new column 'total_SAT' to the dataframe.
# This column represents the total SAT score for each school, calculated by summing the average scores in math, reading, and writing.
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# Finding the top 10 performing schools based on their total SAT scores.
# The schools are grouped by their name, and the mean total SAT score is calculated for each school.
# The result is sorted in descending order, and the top 10 schools are selected.
top_10_schools = schools.groupby("school_name", as_index=False)["total_SAT"].mean().sort_values("total_SAT", ascending=False).head(10)

# Grouping the data by borough and calculating statistical measures for total SAT scores: count, mean, and standard deviation.
# The results are rounded to two decimal places for better readability.
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

# Filtering to find the borough with the highest standard deviation in total SAT scores.
# This highlights the borough with the most variability in school performances.
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

# Renaming the columns of the filtered data for better understanding.
# The columns are renamed to 'num_schools', 'average_SAT', and 'std_SAT' to clearly represent their contents.
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

# Displaying the borough with the highest standard deviation in SAT scores.
largest_std_dev.head()
