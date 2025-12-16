import Place

class Npc:
    def __init__(self,name,race,role,gender=None,age=None, place=None, id_npc=None):
        self.__name = name
        self.__race = race
        self.__role = role
        if gender in (None, "M", "F", "X"):
            self.__gender = gender
        self.__age = age
        self.__place = place
        self.__id = id_npc
    
    def get_name(self):
        return self.__name
    
    def get_race(self):
        return self.__race
    
    def get_role(self):
        return self.__role
    
    def get_gender(self):
        return self.__gender
    
    def get_age(self):
        return self.__age
    
    
    def get_place(self):
        return self.__place
    
    def get_id(self):
        return self.__id
    
    def __str__(self):
        s = f"{self.__name} is a {self.__role} from the {self.__race} race."
        if(self.__gender != None):
            s+= " He is "
            if(self.__gender == "M"):
                s += "male "
            elif(self.__gender == "F"):
                s += "female "
            else:
                s += "x "
        if self.__age != None:
            s += f"and {self.__age} years old."
        if self.__place != None:
            s+=f" He is in {self.__place.get_name()} in {self.__place.get_city()}."
        return s
    
    
    
if __name__ == "__main__":
    vives = Place.Place("vives", "kortrijk", 2, "een hoge school in kortrijk")
    jeroen = Npc("jeroen", "human", "student", "m", 18, vives)
    print(jeroen)