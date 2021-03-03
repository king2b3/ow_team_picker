from main import roles
import random

class Player():
    def __init__(self, name:str, roles:dict, heroes:dict):
        """
        Parameters:
        
        name: str
            name of the player, which will be printed out
        roles: dict
            holds the role preferences for the hero
        heroes: dict
            holds the hero preferences for this player
        """
        ...
        self.name = name
        self.map1 = None
        self.map2 = None
        self.map3 = None
        self.map4 = None
        self.roles = roles
        self.heroes = heroes
        self.maps_played = 0
        self.tank = roles["tank"]
        self.dps = roles["dps"]
        self.support = roles["support"]
        
        # makes roulette wheel for heroes        
        self.heroes_list = []
        for hero in self.heroes.keys():
            for i in range(self.heroes[hero]):
                self.heroes_list.append(hero)

        # makes roulette wheel for roles
        self.roles_list = []
        for role in self.roles.keys():
            for i in range(self.roles[role]):
                self.roles_list.append(role)
            
    
    def returnPlayer(self, role) -> str:
        """Returns a hero choice off of preference
        """
        temp_hero = None
        while temp_hero not in roles[role]:
            temp_hero = random.choice(self.heroes_list)
        return temp_hero       

        

def main():
    import GOML
    import random
    from main import roles
    
    
    # choses role
    t = Player("logro", GOML.LOGRO_ROLES, GOML.LOGRO_HEROES)
    
    temp_role = random.choice(t.roles_list)
    print(f"role picked {temp_role}")


    print(t.returnPlayer(temp_role))


    map1 = {
        "MT": Player("logro", GOML.LOGRO_ROLES, GOML.LOGRO_HEROES),
        "OT": None,
        "HS": None,
        "PJ": None,
        "MS": None,
        "FS": None
    }

    print(map1["MT"].name)


if __name__ == "__main__":
    main()