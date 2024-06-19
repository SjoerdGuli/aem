import pandas as pd
import matplotlib.pyplot as plt
import plot_likert

# Load the dataset
file_path = 'data.csv'
data = pd.read_csv(file_path)

# columns
ordinal_columns = ['40 °C', '35 °C', '30 °C', '25 °C', '20 °C']

likert_data = data.drop(columns=['participant'])

# Likert scale
scale_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Create Likert chart
fig, ax = plt.subplots(figsize=(16, 4))
color_codes = ['#ffffff', '#e6e6e6', '#cccccc', '#b3b3b3', '#999999', '#808080', '#666666', '#4d4d4d', '#333333', '#000000']
plot_likert.plot_likert(likert_data, plot_scale=[1, 2, 3, 4, 5, 6, 7, 8, 9], ax=ax, plot_percentage=True, colors = color_codes)

ax.set_xlabel('Proportion', fontsize=20)
ax.set_ylabel('Temperature Setting', fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(ticks=range(len(ordinal_columns)), fontsize=14, labels=ordinal_columns)
ax.legend(title='Scores', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()