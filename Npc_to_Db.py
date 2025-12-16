import sqlite3, Npc, Place_to_Db

class Npc_to_Db():
    def __init__(self):
        self.__connection = sqlite3.connect("npc_manager.db")
        self.__cursor = self.__connection.cursor()

    def get_npc(self, npc_name):
        query = "SELECT * FROM npc where name == ?"
        self.__cursor.execute(query, (npc_name,))
        results = self.__cursor.fetchall()
        for row in results:
            print(row)
        query = "SELECT * FROM npc where id == ?"
        self.__cursor.execute(query, (input("Give the first number of the npc you would like to get from the above list:"),))
        results = self.__cursor.fetchall()
        result = results[0]
        p2db = Place_to_Db.Place_to_Db()
        place = p2db.get_place_by_id(result[6])
        p2db.close()
        npc = Npc.Npc(result[1], result[2], result[3], result[4], result[5], place, result[0])
        return npc
    
    def new_npc(self, npc):
        query = "INSERT INTO npc (name, race, gender, age, role, place_id) VALUES (?,?,?,?, ?, ?);"
        self.__cursor.execute(query, (npc.get_name(), npc.get_race(), npc.get_gender(), npc.get_age(), npc.get_role(), npc.get_place().get_id()))
        self.__connection.commit()
        
    def update_npc(self, npc_name, key, value):
        if key in ("name", "race", "gender", "age", "role"):
            npc = self.get_npc(npc_name)
            query = f"UPDATE npc set {key} = ? WHERE id = ?"
            self.__cursor.execute(query, (value, npc.get_id()))
            self.__connection.commit()
        elif key == "place":
            npc = self.get_npc(npc_name)
            query = "UPDATE npc set place_id = ? WHERE id = ?"
            self.__cursor.execute(query, (value.get_id(), npc.get_id()))
            self.__connection.commit()
        
        
    def update_all(self, search_key, search_value, replace_key, replace_value):
        if replace_key in ("name", "race", "gender", "age", "role"):
            if search_key in ("name", "race", "gender", "age", "role"):
                query = f"UPDATE npc SET {replace_key} = ? WHERE {search_key} = ?"
                self.__cursor.execute(query, (replace_value, search_value))
                self.__connection.commit()
            elif search_key == "place":
                query = f"UPDATE npc SET {replace_key} = ? WHERE place_id = ?"
                self.__cursor.execute(query, (replace_value, search_value.get_id()))
                self.__connection.commit()
        if replace_key == "place":
            if search_key in ("name", "race", "gender", "age", "role"):
                query = f"UPDATE npc SET place_id = ? WHERE {search_key} = ?"
                self.__cursor.execute(query, (replace_value.get_id(), search_value))
                self.__connection.commit()
            elif search_key == "place":
                query = "UPDATE npc SET place_id = ? WHERE place_id = ?"
                self.__cursor.execute(query, (replace_value.get_id(), search_value.get_id()))
                self.__connection.commit()
            

    def close(self):
        self.__cursor.close()
        self.__connection.close()
        
if __name__ == "__main__":
    n2db = Npc_to_Db()
    try:
        p2db = Place_to_Db.Place_to_Db()
        place = p2db.get_place("Vives")
        npc = Npc.Npc("Jeroen", "humen", "Student", "M", 18, place)
        n2db.new_npc(npc)
        n2db.update_npc("Jeroen", "race", "human")
        n2db.update_all("age", 18, "age", 19)
        place = p2db.get_place("Howest")
        n2db.update_npc("Jeroen", "place", place)
        npc = n2db.get_npc("Jeroen")
        
        
        print(npc)
        p2db.close()
        n2db.close()
    except Exception as e:
        print(e)
        p2db.close()
        n2db.close()
