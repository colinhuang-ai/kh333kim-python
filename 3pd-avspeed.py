import pandas as pd

# step 1: using panda to read pokemon_data
pokemonFrame = pd.read_csv('pokemon_water.csv')

# step 2: calcualte average base on speed
# ko them cot
pokemonSpeed = pokemonFrame['Speed']
average_speed = pokemonSpeed.mean()

# them cot
pokemonFrame['Average Speed'] = pokemonFrame['Speed'].mean()

# step 3: print
print(f"Average Speed: {average_speed}")
