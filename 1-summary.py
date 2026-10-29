# library paht --> funciton pathlib
from pathlib import Path

# import lib pandas , use alias as pd
import pandas as pd


# function programming
# function return None
def main() -> None:
    # step 1: get the path of the CSV file
    csv_path = Path(__file__).with_name("pokemon_data.csv")
    print(f"Path to CSV file: {csv_path}")

    # step 2: read the CSV file into a pandas DataFrame
    pokemon = pd.read_csv(csv_path)
    print(pokemon.head())  # print the first 5 rows of the DataFrame

    # step 3: split the DataFrame
    top10pk = pokemon.head(10)
    print(top10pk)

    print(f"So luong Pokemon: {len(pokemon)}")

    # step 4: loop through the stats and find the highest value for each stat
    # array of stats
    statArray = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
    for stat in statArray:
        # panda support max() function to find the highest value of a column
        highest_value = pokemon[stat].max()

        # find pokemon with the highest value for the current stat
        # for example highest_value = 100,
        highest_pokemon = pokemon.loc[pokemon[stat] == highest_value, "Name"]

        # print the result
        print(f"{stat} cao nhat ({highest_value}): {', '.join(highest_pokemon)}")


if __name__ == "__main__":
    main()
