import pandas as pd
cricket_data = pd.read_csv('/Users/P/Desktop/PythonLab5/cricket.csv')
sorted_data = cricket_data.sort_values(by='runs', ascending=True)[['name','matches','runs']]
print("Information about the Players by ascending order of Runs: ")
print(sorted_data)
