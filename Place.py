class Place:
    
    def __init__(self, name, city, danger_level = None, description = None, id_place = None):
        self.__name = name
        self.__city = city
        self.__danger_level = danger_level
        self.__description = description
        self.__id = id_place
        
    def get_name(self):
        return self.__name
    
    def get_city(self):
        return self.__city
    
    def __str__(self):
        s = f"{self.__name} is a place in {self.__city}. "
        if self.__danger_level != None:
            s+= f"With a danger level of {self.__danger_level} out of 10."
        if self.__description != None:
            s += f"Here's a bit more info about {self.__name}: {self.__description}."
        return s
    
if __name__ == "__main__":
    vives = Place("vives", "kortrijk", 2, "een hoge school in kortrijk")
    print(vives)