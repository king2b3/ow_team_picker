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
        #if self.maps_played == 2:
        #    return False
        ...
        

def main():
    import GOML
    import random
    from main import roles
    
    t = Player("npc", GOML.NPC_ROLES, GOML.NPC_HEROES)
    # choses role
   
    
    temp_role = random.choice(t.roles_list)
    print(f"role picked {temp_role}")


    temp_hero = None
    while temp_hero not in roles[temp_role]:
        temp_hero = random.choice(t.heroes_list)
    print(f"Hero picked {temp_hero}")       

    


    

if __name__ == "__main__":
    main()