import random

class Team():
    def __init__(self, players):
        """
        """
        self.players = players
        self.map1 = {
            "MT": None,
            "OT": None,
            "HS": None,
            "PJ": None,
            "MS": None,
            "FS": None
        }
        self.map2 = self.map1.copy()
        self.map3 = self.map1.copy()
        self.map4 = self.map1.copy()
        self.fillMaps()
        self.fillHereos()
        self.display()
    

    def fillMaps(self, max_attempts:int=1000, attempts:int=0) -> None:
        while attempts < max_attempts:
            if attempts != 0:
                self.resetMaps()
            self.map1 = self.generateMap()
            self.incrementMaps(1)
            self.map2 = self.generateMap()
            self.incrementMaps(2)
            self.map3 = self.generateMap()
            self.incrementMaps(3)
            self.map4 = self.generateMap()
            self.incrementMaps(4)
            count = True
            for p in self.players:
                if p.maps_played != 3:
                    count = False
            if count:
                attempts = max_attempts
            
            attempts += 1


    def fillHereos(self) -> None:
        # Couldn't think of a better way to do this in a pinch
        # map 1
        for role1, role2, role in [ ["MT","OT","tank"], ["HS","PJ","dps"], ["MS","FS","support"]]:
            self.map1[role1].map1 = self.map1[role1].returnPlayer(role)
            self.map1[role2].map1 = self.map1[role2].returnPlayer(role)
            while self.map1[role1].map1 == self.map1[role2].map1:
                self.map1[role2].map1 = self.map1[role2].returnPlayer(role)

        for role1, role2, role in [ ["MT","OT","tank"], ["HS","PJ","dps"], ["MS","FS","support"]]:
            self.map2[role1].map2 = self.map2[role1].returnPlayer(role)
            self.map2[role2].map2 = self.map2[role2].returnPlayer(role)
            while self.map2[role1].map2 == self.map2[role2].map2:
                self.map2[role2].map2 = self.map2[role2].returnPlayer(role)

        for role1, role2, role in [ ["MT","OT","tank"], ["HS","PJ","dps"], ["MS","FS","support"]]:
            self.map3[role1].map3 = self.map3[role1].returnPlayer(role)
            self.map3[role2].map3 = self.map3[role2].returnPlayer(role)
            while self.map3[role1].map3 == self.map3[role2].map3:
                self.map3[role2].map3 = self.map3[role2].returnPlayer(role)

        for role1, role2, role in [ ["MT","OT","tank"], ["HS","PJ","dps"], ["MS","FS","support"]]:
            self.map4[role1].map4 = self.map4[role1].returnPlayer(role)
            self.map4[role2].map4 = self.map4[role2].returnPlayer(role)
            while self.map4[role1].map4 == self.map4[role2].map4:
                self.map4[role2].map4 = self.map4[role2].returnPlayer(role)
        

    
    def incrementMaps(self, map_number:int) -> None:
        if map_number == 1:
            self.map1["MT"].maps_played += 1
            self.map1["OT"].maps_played += 1
            self.map1["HS"].maps_played += 1
            self.map1["PJ"].maps_played += 1
            self.map1["MS"].maps_played += 1
            self.map1["FS"].maps_played += 1
        
        elif map_number == 2:
            self.map2["MT"].maps_played += 1
            self.map2["OT"].maps_played += 1
            self.map2["HS"].maps_played += 1
            self.map2["PJ"].maps_played += 1
            self.map2["MS"].maps_played += 1
            self.map2["FS"].maps_played += 1

        elif map_number == 3:
            self.map3["MT"].maps_played += 1
            self.map3["OT"].maps_played += 1
            self.map3["HS"].maps_played += 1
            self.map3["PJ"].maps_played += 1
            self.map3["MS"].maps_played += 1
            self.map3["FS"].maps_played += 1

        else:
            self.map4["MT"].maps_played += 1
            self.map4["OT"].maps_played += 1
            self.map4["HS"].maps_played += 1
            self.map4["PJ"].maps_played += 1
            self.map4["MS"].maps_played += 1
            self.map4["FS"].maps_played += 1


    def resetMaps(self) -> None:
        for m in [self.map1, self.map2, self.map3, self.map4]:
            m["MT"].maps_played = 0
            m["OT"].maps_played = 0
            m["HS"].maps_played = 0
            m["PJ"].maps_played = 0
            m["MS"].maps_played = 0
            m["FS"].maps_played = 0
        

    def generateMap(self, max_attempts:int=100, attempts:int=0) -> dict:
        """Completes the team selection for a map

        PLEASE don't judge me for this, this might be the worst code I have ever written.
          I am beyond embarrassed that I didn't create a scheduling algorithm
        """
        while 1:
            temp_team = self.players.copy()
            # selects the tanks
            tank1 = random.choice(temp_team)
            temp_team.remove(tank1)
            tank2 = random.choice(temp_team)
            temp_team.remove(tank2)
            
            # dps 
            dps1 = random.choice(temp_team)
            temp_team.remove(dps1)
            dps2 = random.choice(temp_team)
            temp_team.remove(dps2)
            
            # support
            support1 = random.choice(temp_team)
            temp_team.remove(support1)
            support2 = random.choice(temp_team)

            # YES I HATE MYSELF TOO THIS IS THE WORST THING EVER BUT ITS LATE AND I DON'T CARE
            if (
                tank1.tank != 0 and
                tank2.tank != 0 and
                dps1.dps != 0 and
                dps2.dps != 0 and
                support1.support != 0 and
                support2.support != 0
            ):
                temp = {
                    "MT": tank1,
                    "OT": tank2,
                    "HS": dps1,
                    "PJ": dps2,
                    "MS": support1,
                    "FS": support2
                }
                return temp
            attempts += 1
    
    
    def display(self) -> None:
        """Displays the role pick for each player
        """
        import sys
        original_stdout = sys.stdout

        with open('output.txt','w') as f:
            sys.stdout = f

            print(f"BEHOLD YOUR WINNING LINEUP")
            print(f"########################")
            print(f"MAP 1")
            print(f'\tTank 1    : {self.map1["MT"].name} playing {self.map1["MT"].map1}')
            print(f'\tTank 2    : {self.map1["OT"].name} playing {self.map1["OT"].map1}')
            print(f'\tDPS 1     : {self.map1["HS"].name} playing {self.map1["HS"].map1}')
            print(f'\tDPS 2     : {self.map1["PJ"].name} playing {self.map1["PJ"].map1}')
            print(f'\tSupport 1 : {self.map1["MS"].name} playing {self.map1["MS"].map1}')
            print(f'\tSupport 2 : {self.map1["FS"].name} playing {self.map1["FS"].map1}')
            print(f"########################")
            print(f"MAP 2")
            print(f'\tTank 1    : {self.map2["MT"].name} playing {self.map2["MT"].map2}')
            print(f'\tTank 2    : {self.map2["OT"].name} playing {self.map2["OT"].map2}')
            print(f'\tDPS 1     : {self.map2["HS"].name} playing {self.map2["HS"].map2}')
            print(f'\tDPS 2     : {self.map2["PJ"].name} playing {self.map2["PJ"].map2}')
            print(f'\tSupport 1 : {self.map2["MS"].name} playing {self.map2["MS"].map2}')
            print(f'\tSupport 2 : {self.map2["FS"].name} playing {self.map2["FS"].map2}')
            print(f"########################")
            print(f"MAP 3")
            print(f'\tTank 1    : {self.map3["MT"].name} playing {self.map3["MT"].map3}')
            print(f'\tTank 2    : {self.map3["OT"].name} playing {self.map3["OT"].map3}')
            print(f'\tDPS 1     : {self.map3["HS"].name} playing {self.map3["HS"].map3}')
            print(f'\tDPS 2     : {self.map3["PJ"].name} playing {self.map3["PJ"].map3}')
            print(f'\tSupport 1 : {self.map3["MS"].name} playing {self.map3["MS"].map3}')
            print(f'\tSupport 2 : {self.map3["FS"].name} playing {self.map3["FS"].map3}')
            print(f"########################")
            print(f"MAP 4")
            print(f'\tTank 1    : {self.map4["MT"].name} playing {self.map4["MT"].map4}')
            print(f'\tTank 2    : {self.map4["OT"].name} playing {self.map4["OT"].map4}')
            print(f'\tDPS 1     : {self.map4["HS"].name} playing {self.map4["HS"].map4}')
            print(f'\tDPS 2     : {self.map4["PJ"].name} playing {self.map4["PJ"].map4}')
            print(f'\tSupport 1 : {self.map4["MS"].name} playing {self.map4["MS"].map4}')
            print(f'\tSupport 2 : {self.map4["FS"].name} playing {self.map4["FS"].map4}')
            print(f"########################")
            for p in self.players:
                print(f'\t{p.name} played {p.maps_played}')
            sys.stdout = original_stdout

def main():
    import GOML
    import random
    from main import roles
    from player import Player
    
    l = Player("logro", GOML.LOGRO_ROLES, GOML.LOGRO_HEROES)
    n = Player("npc", GOML.NPC_ROLES, GOML.NPC_HEROES)
    k = Player("kittybaka", GOML.KITTYBAKA_ROLES, GOML.KITTYBAKA_HEROES)
    s = Player("strk916", GOML.STRKR916_ROLES, GOML.STRKR916_HEROES)
    m = Player("meesh", GOML.MEESH_ROLES, GOML.MEESH_HEROES)
    v = Player("vengan", GOML.VENAGN_ROLES, GOML.VENAGN_HEROES)
    a = Player("akihikosanada", GOML.AKIHIKOSANADA_ROLES, GOML.AKIHIKOSANADA_HEROES)
    ma = Player("magpie", GOML.MAGPIE_ROLES, GOML.MAGPIE_HEROES)

    t = Team([l,n,k,s,m,v,a,ma])

if __name__ == "__main__":
    main()