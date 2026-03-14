# Week 5 - Mini Project 1 - Movie Ratings Analysis System:

import pandas as pd

# Load the dataset
file_path = 'movie_ratings.csv'
df = pd.read_csv(file_path)

# Calculate average rating per genre
genre_avg_ratings = df.groupby('Genre')['Rating'].mean().round(2)

# Find the top 5 highest-rated movies
top_movies = df.sort_values(by=['Rating', 'Votes'], ascending=[False, False]).head(5)

# Generate report
report_content = "Genre-wise Average Ratings:\n"
report_content += genre_avg_ratings.to_string() + "\n\nTop 5 Highest Rated Movies:\n"
report_content += top_movies[['Movie', 'Rating', 'Votes']].to_string(index=False)

# Save report to file
report_file = 'movie_report.txt'
with open(report_file, 'w') as file:
    file.write(report_content)

print("Report generated and saved as 'movie_report.txt'.")