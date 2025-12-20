import sqlite3, Place

class Place_to_Db():
    def __init__(self):
        self.__connection = sqlite3.connect("npc_manager.db")
        self.__cursor = self.__connection.cursor()

    def get_all_places(self):
        query = "SELECT * from place"
        self.__cursor.execute(query)
        results = self.__cursor.fetchall()
        return results

    def get_places(self, place_name):
        query = "SELECT * FROM place where name == ?"
        self.__cursor.execute(query, (place_name,))
        results = self.__cursor.fetchall()
        return results

    def get_place(self, place_name):
        results = self.get_places(place_name)
        for row in results:
            print(row)
        query = "SELECT * FROM place where id == ?"
        self.__cursor.execute(query, (input("Give the first number of the place you would like to get from the above list:"),))
        results = self.__cursor.fetchall()
        result = results[0]
        place = Place.Place(result[1], result[2], result[3], result[4], result[0])
        return place
    
    def get_place_by_id(self, place_id):
        query = "SELECT * FROM place where id == ?"
        self.__cursor.execute(query, (place_id,))
        results = self.__cursor.fetchall()
        result = results[0]
        place = Place.Place(result[1], result[2], result[3], result[4], result[0])
        return place
    
    def new_place(self, place):
        query = "INSERT INTO place (name, city, danger_level, description) VALUES (?,?,?,?);"
        self.__cursor.execute(query, (place.get_name(), place.get_city(), place.get_danger_level(), place.get_description()))
        self.__connection.commit()
        
    def update_place(self, place_name, key, value):
        if key in ("name","city","danger_level","description"):
            place = self.get_place(place_name)
            query = f"UPDATE place set {key} = ? WHERE id = ?"
            self.__cursor.execute(query, (value, place.get_id()))
            self.__connection.commit()
        
    def update_all(self, search_key, search_value, replace_key, replace_value):
        if replace_key in ("name","city", "danger_level", "description"):
            if search_key in ("name","city","danger_level", "description"):
                query = f"UPDATE place SET {replace_key} = ? WHERE {search_key} = ?"
                self.__cursor.execute(query, (replace_value, search_value))
                self.__connection.commit()
            

    def close(self):
        self.__cursor.close()
        self.__connection.close()
        
if __name__ == "__main__":
    p2db = Place_to_Db()
    try:
        place = Place.Place("Vives", "Gent", 2, "A college in Kortrijk")
        p2db.new_place(place)
        p2db.update_place("Vives", "city", "Kortrijk")
        p2db.update_all("description", "A high school in Kortrijk", "description", "A college in Kortrijk")
        place = p2db.get_place("Vives")
        
        
        print(place)
        p2db.close()
    except Exception as e:
        print(e)
        p2db.close()
    

