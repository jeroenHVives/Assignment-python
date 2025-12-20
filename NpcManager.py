import sys, Place_to_Db, Npc_to_Db, Place, Npc
import pandas as pd


def places_to_df():
    p2db = Place_to_Db.Place_to_Db()
    results = p2db.get_all_places()
    ids = []
    names = []
    cities = []
    danger_levels = []
    descriptions = []
    for result in results:
        ids.append(result[0])
        names.append(result[1])
        cities.append(result[2])
        danger_levels.append(result[3])
        descriptions.append(result[4])
    df = pd.DataFrame({
        "Id": ids,
        "Name": names,
        "City": cities,
        "Danger_level": danger_levels,
        "Description": descriptions
    })
    return df

def npcs_to_df():
    n2db = Npc_to_Db.Npc_to_Db()
    results = n2db.get_all_npcs()
    ids = []
    names = []
    races = []
    genders = []
    ages = []
    roles = []
    place_names = []
    for result in results:
        ids.append(result[0])
        names.append(result[1])
        races.append(result[2])
        genders.append(result[3])
        ages.append(result[4])
        roles.append(result[5])
        p2db = Place_to_Db.Place_to_Db()
        place = p2db.get_place_by_id(result[6])
        place_names.append(place.get_name())
    df = pd.DataFrame({
        "Id": ids,
        "Name": names,
        "Race": races,
        "Gender": genders,
        "Age": ages,
        "Role": roles,
        "Place": place_names
    })
    return df

#python NpcManager.py -csv table filename 
if sys.argv[1] == "-csv":
    if sys.argv[2] == "place":
        df = places_to_df()
        try:
            df.to_csv(sys.argv[3], sep=',', index=False)
        except:
            print(f"File {sys.argv[3]} doesn't exists")
    elif sys.argv[2] == "npc":
        df = npcs_to_df()
        try:
            df.to_csv(sys.argv[3], sep=',', index=False)
        except:
            print(f"File {sys.argv[3]} doesn't exists")
    else:
        print(f"Given table {sys.argv[2]} doesn't exist. Only the tables npc and place exists.")
        sys.exit(-1)
#python NpcManager.py -excel table filename
elif sys.argv[1] == "-excel":
    if sys.argv[2] == "place":
        df = places_to_df()
        try:
            df.to_excel(sys.argv[3], sheet_name="placeList", index=False)
        except:
            print(f"File {sys.argv[3]} doesn't exists")
    elif sys.argv[2] == "npc":
        df = npcs_to_df()
        try:
            df.to_excel(sys.argv[3], sheet_name="npcList", index=False)
        except:
            print(f"File {sys.argv[3]} doesn't exists")
    else:
        print(f"Given table {sys.argv[2]} doesn't exist. Only the tables npc and place exists.")
#pyhon NpcManager.py -new table
elif sys.argv[1] == "-new":
    if sys.argv[2] == "place":
        name = input("What's the place's name?")
        city = input(f"In what city is this {name}?")
        danger_level = input("How dangerous is {name} on a scale from 1 to 10?(if you don't know yet type 0)")
        description = input(f"Describe {name}:(if you have no description yet press enter)")
        if(danger_level == 0):
            danger_level = None
        if(description == ""):
            description = None 
        place = Place.Place(name, city, int(danger_level), description)
        p2db = Place_to_Db.Place_to_Db()
        p2db.new_place(place)
    if sys.argv[2] == "npc":
        name = input("what's the npc's name?")
        race = input(f"Of what race is {name}?")
        gender = input(f"What gender is {name}? Use M for male, F for female and X for other. (press enter if you don't know yet)")
        age = input(f"How old is {name}? (if you're not sure yet press enter)")
        role = input(f"What role does {name} have?")
        place_name = input(f"At what place is {name} right now? (if you don't know press enter)")
        if gender == "":
            gender = None
        if age == "":
            age = None
        if place_name == "":
            place = None
        else:
            p2db = Place_to_Db.Place_to_Db()
            place = p2db.get_place(place_name)
        npc = Npc.Npc(name, race, role, gender, int(age), place)
        n2db = Npc_to_Db.Npc_to_Db()
        n2db.new_npc(npc)
#python NpcManager.py -edit one_edit table
#one_edit is a boolean that decides if one row or multiple rows needs to be edited 
elif sys.argv[1] == "-edit":
    if sys.argv[2] == "True":
        if sys.argv[3] == "place":
            p2db = Place_to_Db.Place_to_Db()
            place_name = input("What's the name of the place you would like to change?")
            key = input(f"What would you like to change about {place_name}? (name, city, danger_level or description)")
            value = input(f"What should the value of {key} be instead?")
            p2db.update_place(place_name, key, value)
        elif sys.argv[3] == "npc":
            n2db = Npc_to_Db.Npc_to_Db()
            npc_name = input("What's the name of the npc you would like to change?")
            key = input(f"What would you like to change about {npc_name}? (name, race, gender, age, role, place)")
            value = input(f" what should the value of {key} be instead?")
            n2db.update_npc(npc_name, key, value)
        else:
            print(f"{sys.argv[3]} does not exist. The only tables that exist are npc and place.")
            sys.exit(-1)
    elif sys.argv[2] == "False":
        if sys.argv[3] == "place":
            p2db = Place_to_Db.Place_to_Db()
            search_key = input("Which field should be used to find the record? (name, city, danger_level or description) ")
            search_value = input(f"What is the current value of {search_key} you want to search for? ")
            replace_key = input("Which field would you like to update? (name, city, danger_level or description) ")
            replace_value = input(f"What should the new value of {replace_key} be instead? ")
            p2db.update_all(search_key, search_value, replace_key, replace_value)
        elif sys.argv[3] == "npc":
            n2db = Npc_to_Db.Npc_to_Db()
            search_key = input("Which field should be used to find the record? (name, race, gender, age, role, place) ")
            search_value = input(f"What is the current value of {search_key} you want to search for? ")
            replace_key = input("Which field would you like to update? (name, race, gender, age, role, place) ")
            replace_value = input(f"What should the new value of {replace_key} be instead? ")
            n2db.update_all(search_key, search_value, replace_key, replace_value)
        else:
            print(f"{sys.argv[3]} does not exist. The only tables that exist are npc and place.")
            sys.exit(-1)
    else:
        print(f"{sys.argv[2]} is not a valid answer.Type True is you want to change only one row and False if you want to change multiple rows.")
#python NpcManager.py -get table
elif sys.argv[1] == "-get":
    if sys.argv[2] == "place":
        p2db = Place_to_Db.Place_to_Db()
        place_name = input("What's the name of the place(s) you would like to get?")
        p2db.get_places(place_name)
    elif sys.argv[2] == "npc":
        n2db = Npc_to_Db.Npc_to_Db()
        npc_name = input("What's the name of the npc(s) you would like to get?")
        n2db.get_npcs(npc_name)
    else:
        print(f"{sys.argv[2]} does not exist. The only tables that exist are npc and place.")

     