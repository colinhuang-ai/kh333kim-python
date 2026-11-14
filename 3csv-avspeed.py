import csv


# step 1: use csv to read pokemon_data
with open("pokemon_water.csv") as csv_file:
    pokemon_reader = csv.DictReader(csv_file)
    pokemon_rows = list(pokemon_reader)

# step 2: calculate average based on speed
total_speed = 0
for pokemon in pokemon_rows:
    total_speed += float(pokemon["Speed"])

average_speed = total_speed / len(pokemon_rows)

# step 3: print
print(f"Average Speed: {average_speed}")
