# Step 1: Use csv lib to read from files, relative path
with open("./pokemon_data.csv") as pokemonFile:
    #import csv reader/parser
    import csv
    
    # Step 2: Read lines by lines from csv file
    pokemonReader = csv.reader(pokemonFile)
    print("Reader object_id: " + str(pokemonReader)) #debug only

    headerField = next(pokemonReader)
    # print(headerField) #debug only

    # Step 3: put into eachline to array of pokemon
    namePokemons = []
    hpPokemons = []
    for row in pokemonReader:
        # Step 4: read till end of line of file
        # print(row) #debug
        name = row[0]
        type1 = row[1]
        type2 = row[2]
        hp = row[3]

        # Step 5: build array
        namePokemons.append(name)
        hpPokemons.append(hp)

    print(namePokemons)
    print(hpPokemons)

    # Step 6: loop via array to find pokemon
    nameMaxHP = ""
    maxHP = 0
    for i in range(len(namePokemons)):
        if int(hpPokemons[i]) > maxHP:
            maxHP = int(hpPokemons[i]) # set maxHP to current value
            nameMaxHP = namePokemons[i]

    print(f"Pokemon with highest HP: {nameMaxHP} with HP: {maxHP}")

    # Step 7: loop using while loop to find pokemon with highest HP
    nameMaxHP2 = ""
    maxHP2 = 0
    index = 0
    while index < len(namePokemons):
        if int(hpPokemons[index]) > maxHP2:
            maxHP2 = int(hpPokemons[index])
            nameMaxHP2 = namePokemons[index]
        index += 1

    print(f"Pokemon with highest HP (while loop): {nameMaxHP2} with HP: {maxHP2}")