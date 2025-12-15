import sqlite3, Place

class Place_to_Db():
    def __init__(self):
        self.__connection = sqlite3.connect("npc_manager.db")
        self.__cursor = self.__connection.cursor()

    def get_place(self, place_name):
        query = "SELECT * FROM place where name == ?"
        self.__cursor.execute(query, (place_name,))
        results = self.__cursor.fetchall()
        for row in results:
            print(row)
        query = "SELECT * FROM place where id == ?"
        self.__cursor.execute(query, (input("Give the first number of the place you would like to get from the above list:"),))
        results = self.__cursor.fetchall()
        result = results[0]
        place = Place.Place(result[1], result[2], result[3], result[4])
        return place
    
        
    def new_place(self, place):
        query = "INSERT INTO place (name, city, danger_level, description) VALUES (?,?,?,?);"
        self.__cursor.execute(query, (place.get_name(), place.get_city(), place.get_danger_level(), place.get_description()))
        self.__connection.commit() 

    def close(self):
        self.__cursor.close()
        self.__connection.close()
        
if __name__ == "__main__":
    p2db = Place_to_Db()
    try:
        place = Place.Place("Vives", "Kortrijk")
        p2db.new_place(place)
        place = p2db.get_place("Vives")
        print(place)
        p2db.close()
    except Exception as e:
        print(e)
        p2db.close()
    

