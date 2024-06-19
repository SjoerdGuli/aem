import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Reshape the data
data_long = pd.melt(data, id_vars=['participant'], var_name='Temperature', value_name='Rating')

# Create mapping
temperature_mapping = {
    'score_setting1': '20°C',
    'score_setting2': '25°C',
    'score_setting3': '30°C',
    'score_setting4': '35°C',
    'score_setting5': '40°C'
}

data_long['Temperature'] = data_long['Temperature'].map(temperature_mapping)

# Violin plot
plt.figure(figsize=(12, 8))
sns.violinplot(x='Temperature', y='Rating', data=data_long, palette='muted', cut=0, inner=None, linewidth=4)

# median dots
medians = data_long.groupby('Temperature')['Rating'].median().values
sns.swarmplot(x='Temperature', y='Rating', data=data_long, color='white', size=7, marker='o', edgecolor='black', linewidth=2)

plt.xlabel('Temperature (°C)', fontsize=34)
plt.ylabel('Comfort Rating (scale 1-9)', fontsize=34)
plt.xticks(fontsize=36)
plt.yticks(fontsize=36)
plt.ylim(1, 9)
plt.grid(linewidth=1.5)

plt.show()
