import csv

#dictionary that contains all pokemon names as keys, and types as list values
paldeanDict = {}
with open('Violet pokemon list.csv', newline='') as csvfile:
    lineCount = 0
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if lineCount != 0:
            sortRow = ' '.join(row)
            sortRow = sortRow.split(",")
            sortRow[1] = sortRow[1].lower()
            sortRow[2] = sortRow[2].lower().split("/")
            if "(" in sortRow[1]:
                sortRow[3] = sortRow[1][sortRow[1].index("(")+1:len(sortRow[1])-1]
                sortRow[1] = sortRow[1][0:sortRow[1].index("(")-1]
                if sortRow[1] in paldeanDict:
                    paldeanDict[sortRow[1]].update({sortRow[3]: sortRow[2]})
                else:
                    paldeanDict.update({sortRow[1]: {sortRow[3]: sortRow[2]}})
            else:
                paldeanDict.update({sortRow[1]: sortRow[2]})
                sortRow.pop(3)
        lineCount = 1

#dictionary that contains type as key and weaknesses as list values
weaknessDict = {}
weaknessDict.update({"normal": ["fighting"]})
weaknessDict.update({"fire": ["water", "ground", "rock"]})
weaknessDict.update({"water": ["grass", "electric"]})
weaknessDict.update({"grass": ["fire", "ice", "poison", "flying", "bug"]})
weaknessDict.update({"electric": ["ground"]})
weaknessDict.update({"ice": ["fire", "fighting", "rock", "steel"]})
weaknessDict.update({"fighting": ["flying", "psychic", "fairy"]})
weaknessDict.update({"poison": ["ground", "psychic"]})
weaknessDict.update({"ground": ["water", "grass", "ice"]})
weaknessDict.update({"flying": ["electric", "ice", "rock"]})
weaknessDict.update({"psychic": ["bug", "ghost", "dark"]})
weaknessDict.update({"bug": ["fire", "flying", "rock"]})
weaknessDict.update({"rock": ["water", "grass", "fighting", "ground", "steel"]})
weaknessDict.update({"ghost": ["ghost", "dark"]})
weaknessDict.update({"dragon": ["ice", "dragon", "fairy"]})
weaknessDict.update({"dark": ["fighting", "bug", "fairy"]})
weaknessDict.update({"steel": ["fire", "fighting", "ground"]})
weaknessDict.update({"fairy": ["poison", "steel"]})

#prompt user for pokemon name or tera type
pokemonWeak = input("Pokemon name or tera type? (name/type): ").lower()
#find name in pokedex
while (pokemonWeak not in paldeanDict) and (pokemonWeak not in weaknessDict):
    pokemonWeak = input("Please enter a valid pokemon name or tera type: ")
    #if tauros or wopper ("("), ask for specific type
typeOne = "no"
typeTwo = "none"
if pokemonWeak in paldeanDict:
    try:
        for breed in paldeanDict[pokemonWeak]:
            tryCatch = paldeanDict[pokemonWeak][breed]
            print(breed)
        breed = input("Please specify form or breed: ").lower()
        while breed not in paldeanDict[pokemonWeak]:
            breed = input("Not a form or breed. Please input a correct form or breed: ").lower()
        print(paldeanDict[pokemonWeak][breed])
        print("BREAK")
            #['fighting', 'fire']
            #['fighting']
        try:
            typeOne = (paldeanDict[pokemonWeak][breed][0])
            typeTwo = (paldeanDict[pokemonWeak][breed][1])
        except:
            pass
    except:
        print("NOT DOUBLE")
        print(paldeanDict[pokemonWeak])
        #['electric', 'fighting']
        #['dragon']
        print(paldeanDict[pokemonWeak][0])
        #'dragon'
        try:
            typeOne = paldeanDict[pokemonWeak][0]
            typeTwo = paldeanDict[pokemonWeak][1]
        except:
            pass

#find weakness one in weaknessDict
#if weakness 2 exists (pokedex pokemon), find it in weaknessDict
weakness = weaknessDict[typeOne]
    #if weakness one and two have the same type, store that type
fourTimes = False
if typeTwo != "none":
    weaknessTwo = weaknessDict[typeTwo]
    weaknessTemp = []
    for weaknessOne in weakness:
        if weaknessOne in weaknessTwo:
            weaknessTemp.append(weaknessOne)
    if not bool(weaknessTemp):
        weakness.extend(weaknessTwo)
    else:
        fourTimes = True
        weakness = weaknessTemp
print("WEAK BEFORE")
print(weakness)
print("WEAK AFTER")

#otherwise, output all pokemon with type in [0] and [1] slot
if bool(fourTimes):
    print("FOUR TIMES:")
for pokemon in paldeanDict:
    try:
        for breed in paldeanDict[pokemon]:
            tryCatch = paldeanDict[pokemon][breed]
            #print(paldeanDict[pokemon][breed])
            #['fighting']
            #['fighting', 'fire']
            typeTwo = "none"
            try:
                typeOne = (paldeanDict[pokemon][breed][0])
                typeTwo = (paldeanDict[pokemon][breed][1])
            except:
                pass
            if (typeOne in weakness) or (typeTwo in weakness):
                print(pokemon + " (" + breed + ") " + str(paldeanDict[pokemon][breed]))
    except:
        typeTwo = "none"
        try:
            typeOne = paldeanDict[pokemon][0]
            typeTwo = paldeanDict[pokemon][1]
        except:
            pass
        if (typeOne in weakness) or (typeTwo in weakness):
            print(pokemon + " " + str(paldeanDict[pokemon]))