import pandas as pd
cricket_data = pd.read_csv('/Users/P/Desktop/PythonLab5/cricket.csv')
players_with_more_wickets_than_matches = cricket_data[cricket_data['wickets'] > cricket_data['matches']]
print(players_with_more_wickets_than_matches[['name','matches','wickets']])

