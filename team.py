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
    

    def generate(self) -> None:
        """Fills the roles for the team across all four maps
        """
        self.map1 = generate()
        self.map2 = generate()
        self.map3 = generate()
        self.map4 = generate()

    

    def map(self) -> dict:
        """Completes the team selection for a map

        PLEASE don't judge me for this, this might be the worst code I have ever written.
          I am beyond embarrassed that I didn't create a scheduling algorithm
        """
        while True:
            temp_team = self.team.copy()
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
                return {
                    "MT": tank1,
                    "OT": tank2,
                    "HS": dps1,
                    "PJ": dps2,
                    "MS": support1,
                    "FS": support2
                }
    
    
    def display(self) -> None:
        """Displays the role pick for each player
        """
        print(f"BEHOLD YOUR WINNING LINEUP")
        print(f"########################")
        print(f"MAP 1")
        print(f"\tTank 1    : {self.map1["MT"].name} playing {self.map1["MT"].map1}")
        print(f"\tTank 2    : {self.map1["OT"].name} playing {self.map1["OT"].map1}")
        print(f"\tDPS 1     : {self.map1["HS"].name} playing {self.map1["HS"].map1}")
        print(f"\tDPS 2     : {self.map1["PJ"].name} playing {self.map1["PJ"].map1}")
        print(f"\tSupport 1 : {self.map1["MS"].name} playing {self.map1["MS"].map1}")
        print(f"\tSupport 2 : {self.map1["FS"].name} playing {self.map1["FS"].map1}")
        print(f"########################")
        print(f"MAP 2")
        print(f"\tTank 1    : {self.map2["MT"].name} playing {self.map2["MT"].map2}")
        print(f"\tTank 2    : {self.map2["OT"].name} playing {self.map2["OT"].map2}")
        print(f"\tDPS 1     : {self.map2["HS"].name} playing {self.map2["HS"].map2}")
        print(f"\tDPS 2     : {self.map2["PJ"].name} playing {self.map2["PJ"].map2}")
        print(f"\tSupport 1 : {self.map2["MS"].name} playing {self.map2["MS"].map2}")
        print(f"\tSupport 2 : {self.map2["FS"].name} playing {self.map2["FS"].map2}")
        print(f"########################")
        print(f"MAP 3")
        print(f"\tTank 1    : {self.map3["MT"].name} playing {self.map3["MT"].map3}")
        print(f"\tTank 2    : {self.map3["OT"].name} playing {self.map3["OT"].map3}")
        print(f"\tDPS 1     : {self.map3["HS"].name} playing {self.map3["HS"].map3}")
        print(f"\tDPS 2     : {self.map3["PJ"].name} playing {self.map3["PJ"].map3}")
        print(f"\tSupport 1 : {self.map3["MS"].name} playing {self.map3["MS"].map3}")
        print(f"\tSupport 2 : {self.map3["FS"].name} playing {self.map3["FS"].map3}")
        print(f"########################")
        print(f"MAP 2")
        print(f"\tTank 1    : {self.map4["MT"].name} playing {self.map4["MT"].map4}")
        print(f"\tTank 2    : {self.map4["OT"].name} playing {self.map4["OT"].map4}")
        print(f"\tDPS 1     : {self.map4["HS"].name} playing {self.map4["HS"].map4}")
        print(f"\tDPS 2     : {self.map4["PJ"].name} playing {self.map4["PJ"].map4}")
        print(f"\tSupport 1 : {self.map4["MS"].name} playing {self.map4["MS"].map4}")
        print(f"\tSupport 2 : {self.map4["FS"].name} playing {self.map4["FS"].map4}")
