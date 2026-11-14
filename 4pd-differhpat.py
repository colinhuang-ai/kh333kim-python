import pandas as pd

# Step 1: Using panda to read csv file
pokemon_data = pd.read_csv("pokemon_data.csv")

# Step 2: each item in data-frame, calculate different betweeen HP and ATTACK, and store in new column "Diff_HP_ATT"
pokemon_data["Diff"] = pokemon_data["HP"] - pokemon_data["Attack"]

# Step 3: sort by alphabe
pokemon_data_sorted = pokemon_data.sort_values(by="Name")

# Step 4: print the result
print(pokemon_data_sorted[["Name", "Diff"]])