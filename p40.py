import pandas as pd
import matplotlib.pyplot as plt

# Sample data (you can replace this with your own dataset)
data = {
    'Name': ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5'],
    'Age': [25, 28, 22, 30, 24],
    'Position': ['Forward', 'Midfield', 'Defender', 'Forward', 'Midfield'],
    'Goals_Scored': [20, 15, 5, 25, 10],
    'Salary': [100000, 90000, 75000, 120000, 85000]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Find top 5 players with the highest number of goals scored
top_goals_players = df.nlargest(5, 'Goals_Scored')

# Find top 5 players with the highest salaries
top_salary_players = df.nlargest(5, 'Salary')

# Calculate the average age of players
average_age = df['Age'].mean()

# Display names of players above the average age
above_average_age_players = df[df['Age'] > average_age]['Name']

# Visualize the distribution of players based on their positions using a bar chart
position_counts = df['Position'].value_counts()
position_counts.plot(kind='bar', xlabel='Position', ylabel='Count', title='Players Distribution by Position')
plt.show()

# Display the results
print("Top 5 Players with the Highest Goals Scored:")
print(top_goals_players)
print("\nTop 5 Players with the Highest Salaries:")
print(top_salary_players)
print(f"\nAverage Age of Players: {average_age}")
print("\nPlayers Above Average Age:")
print(above_average_age_players)
