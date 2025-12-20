import sys, Place_to_Db, Npc_to_Db
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
#pyhon NpcManager.py


