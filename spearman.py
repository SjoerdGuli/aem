import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import spearmanr

# Load the data from the uploaded CSV file
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Reshape the data
data_long = pd.melt(data, id_vars=['participant'], var_name='Temperature', value_name='Rating')

# Create mapping 'score_setting1' to actual temperature values
temperature_mapping = {
    'score_setting1': '20°C',
    'score_setting2': '25°C',
    'score_setting3': '30°C',
    'score_setting4': '35°C',
    'score_setting5': '40°C'
}

# Apply mapping
data_long['Temperature'] = data_long['Temperature'].map(temperature_mapping)

# Create numeric mapping
temperature_num_mapping = {
    '20°C': 20,
    '25°C': 25,
    '30°C': 30,
    '35°C': 35,
    '40°C': 40
}
data_long['Temperature_Num'] = data_long['Temperature'].map(temperature_num_mapping)

# Delete rows with missing values
data_long = data_long.dropna(subset=['Temperature_Num', 'Rating'])

# Correct data types
data_long['Temperature_Num'] = pd.to_numeric(data_long['Temperature_Num'])
data_long['Rating'] = pd.to_numeric(data_long['Rating'])

# Spearman Rank Correlation
stat, p = spearmanr(data_long['Temperature_Num'], data_long['Rating'])
print('Spearman Rank Correlation')
print('Correlation Coefficient:', stat)
print('p-value:', p)
