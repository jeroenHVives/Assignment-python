import Place

class Npc:
    def __init__(self,name,race,role,gender=None,age=None, traits=[], place=None, id_npc=None):
        self.__name = name
        self.__race = race
        self.__role = role
        self.__gender = gender
        self.__age = age
        self.__traits = traits
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
    
    def get_traits(self):
        return self.__traits
    
    def get_place(self):
        return self.__place
    
    def __str__(self):
        s = f"{self.__name} is a {self.__role} from the {self.__race} race."
        if(self.__gender != None):
            s+= " He is "
            if(self.__gender == "m"):
                s += "male "
            elif(self.__gender == "f"):
                s += "female "
            else:
                s += "x "
        if self.__age != None:
            s += f"and {self.__age} years old."
        if len(self.__traits) > 0:
            s+= "He is "
            for trait in self.__traits[:-1]:
                s += trait + ", "
            s = s[:-2]
            s += f" and {self.__traits[-1]}."
        if self.__place != None:
            s+=f" He is in {self.__place.get_name()} in {self.__place.get_city()}."
        return s
    
    
    
if __name__ == "__main__":
    vives = Place.Place("vives", "kortrijk", 2, "een hoge school in kortrijk")
    jeroen = Npc("jeroen", "human", "student", "m", 18, ["happy", "nice", "friendly"], vives)
    print(jeroen)