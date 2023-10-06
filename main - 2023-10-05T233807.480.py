import geopandas as gpd
import pandas as pd

# Step 1: Load the GIS data for the town
town_parcels = gpd.read_file('town_parcels.shp')  # Replace with the actual path to your data file

# Step 2: Examine the data structure
print(town_parcels.head())

# Step 3: Count parcel ownership
ownership_counts = town_parcels['Owner'].value_counts()

# Step 4: Find the owner with the most parcels
most_parcels_owner = ownership_counts.idxmax()
most_parcels_count = ownership_counts.max()

print(f"The owner with the most parcels in the town is {most_parcels_owner} with {most_parcels_count} parcels.")

# Step 5: Optionally, visualize the data
town_parcels.plot(column='Owner', legend=True)
