import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'Engine.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Clean the data
# Rename the columns using the first row
column_names = data.iloc[0].values
# Drop the first row and set the index
clean_data = data.drop(0).set_index('Netflix recommendation engine')
# Rename the columns
clean_data.columns = column_names[1:]
clean_data.index.name = None

# Convert the data to numeric type
clean_data = clean_data.apply(pd.to_numeric, errors='coerce')

# Generate a heatmap with a rectangular shape
plt.figure(figsize=(14, 6))  # Adjusting the size to be more rectangular
sns.heatmap(clean_data, annot=True, cmap='coolwarm', center=0, cbar=True, xticklabels=clean_data.columns, yticklabels=clean_data.index)
plt.title('Netflix Recommendation Engine')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('Netflix_Recommendation_Engine_Rectangular.png')

# Display the plot
plt.show()
