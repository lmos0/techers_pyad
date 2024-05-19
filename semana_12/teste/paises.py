import pandas as pd

# Create a list of data
data = [
    ["China", 1444000000, "Asia"],
    ["India", 1380000000, "Asia"],
    ["United States", 331002651, "North America"],
    ["Indonesia", 273523615, "Asia"],
    ["Pakistan", 220892331, "Asia"],
    ["Brazil", 212559409, "South America"],
    ["Nigeria", 206139587, "Africa"],
    ["Bangladesh", 164669751, "Asia"],
    ["Russia", 143500000, "Europe"],
    ["Mexico", 128915307, "North America"]
]

# Create a DataFrame
df = pd.DataFrame(data, columns=["country", "population", "continent"])

# Save the DataFrame to a CSV file
df.to_csv("world_population.csv", index=False)

print("CSV file created successfully!")
