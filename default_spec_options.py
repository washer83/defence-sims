
class Player:
    def __init__(self,role):
        self.role = role
        # HITS
        self.bgs_hits = []
        self.hammer_hits = []
        self.ralos_hits = []
        self.emaul_hits = []
        #STATS
        self.attackLvl = 118
        self.strengthLvl = 118
        self.rangeLvl = 112
        self.magicLvl = 112
        # WEAPON INFO
        self.ralosAttRoll = 30576
        self.ralosMax = 24
        self.bgsAttRoll = 69434
        self.bgsMax = 77
        self.dwhAttRoll = 34048
        self.dwhMax = 82
        self.emaulAttRoll = 35872
        self.emaulMax = 68
        # OTHER
        self.hitStyle = "live" # options: "live", "one_max", "max_minus_one"
        # hit rolls for above hit styles:
        # live: [0,max_hit] | one_max: [1, max_hit] | max_minus_one: [1, (max_hit-1)] 
        
def create_player_setup(setup_name):
    # Initialize empty players
    players = [Player(f"player{i + 1}") for i in range(4)]
    
    # Nomenclautre:
    # players[0] = mage
    # players[1] = mfrz
    # players[2] = rdps
    # players[3] = mdps

    # Configure based on setup name
    # DWH BGS SETUPS
    if setup_name == "2DWH2BGS":
        players[0].bgs_hits = [11]
        players[1].bgs_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]
    
    elif setup_name == "2DWH2BGS1BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]

    elif setup_name == "2DWH2BGS2BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11,17]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]

    elif setup_name == "2DWH2BGS3BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11,17]
        players[2].hammer_hits = [10]
        players[2].bgs_hits = [21]
        players[3].hammer_hits = [10]

    # GLAIVE SETUPS
    elif setup_name == "2DWH2G":
        players[0].ralos_hits = [11]
        players[1].ralos_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]

    elif setup_name == "2DWH2G1G":
        players[0].ralos_hits = [11,17]
        players[1].ralos_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]

    elif setup_name == "2DWH2G1BGS":
        players[0].ralos_hits = [11]
        players[1].ralos_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]
        players[3].bgs_hits = [16]

    elif setup_name == "2DWH2G1G1BGS":
        players[0].ralos_hits = [11,17]
        players[1].ralos_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]
        players[3].bgs_hits = [21]

    # ELDER GLAIVE SETUPS
    elif setup_name == "2EM2G":
        players[0].ralos_hits = [11]
        players[1].ralos_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
    
    elif setup_name == "2EM2G1BGS":
        players[0].ralos_hits = [11]
        players[1].ralos_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
        players[3].bgs_hits = [16]
    
    elif setup_name == "2EM2G1G":
        players[0].ralos_hits = [11,17]
        players[1].ralos_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]

    elif setup_name == "2EM2G1G1BGS":
        players[0].ralos_hits = [11,17]
        players[1].ralos_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
        players[3].bgs_hits = [18]          
    
    # ELDER BGS BU SETUPS
    elif setup_name == "2EM2BGS":
        players[0].bgs_hits = [11]
        players[1].bgs_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
    
    elif setup_name == "2EM2BGS1BGS":
        players[0].bgs_hits = [11]
        players[1].bgs_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
        players[3].bgs_hits = [16]

    elif setup_name == "2EM2BGS2BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11,17]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]

    elif setup_name == "2EM2BGS3BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11,17]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
        players[3].bgs_hits = [21]

    # SOTE SPECS
    elif setup_name == "2DWH":
        players[1].hammer_hits = [1]
        players[2].hammer_hits = [2]

    elif setup_name == "2DWH1H":
        players[0].hammer_hits = [1]
        players[1].hammer_hits = [1]
        players[3].hammer_hits = [6]

    elif setup_name == "2DWH1BGS":
        players[0].hammer_hits = [1]
        players[1].hammer_hits = [1]
        players[3].bgs_hits = [6]

    elif setup_name == "2DWH1G":
        players[0].hammer_hits = [1]
        players[1].hammer_hits = [1]
        players[3].ralos_hits = [6]

    elif setup_name == "2EM":
        players[0].emaul_hits = [1]
        players[1].emaul_hits = [1]

    elif setup_name == "2EM1EM":
        players[0].emaul_hits = [1]
        players[1].emaul_hits = [1]
        players[3].emaul_hits = [6]

    elif setup_name == "2EM1BGS":
        players[0].emaul_hits = [1]
        players[1].emaul_hits = [1]
        players[3].bgs_hits = [6]

    elif setup_name == "2EM1G":
        players[0].emaul_hits = [1]
        players[1].emaul_hits = [1]
        players[3].ralos_hits = [6]

    # DUO SPECS
    elif setup_name == "duo2DWH2BGSmaiden":
        players[0].hammer_hits = [6,12]
        players[1].bgs_hits = [16,22]

    elif setup_name == "duo2EM2BGSmaiden":
        players[0].emaul_hits = [6,12]
        players[1].bgs_hits = [16,22] 
    
    elif setup_name == "duo2DWH2BGSxarp":
        players[0].hammer_hits = [1]
        players[0].bgs_hits = [7]
        players[1].hammer_hits = [1]
        players[1].bgs_hits = [7]
    
    elif setup_name == "duo3DWH1BGSxarp":
        players[0].hammer_hits = [1,7]
        players[1].hammer_hits = [1]
        players[1].bgs_hits = [17]

    elif setup_name == "duo2EM2BGSxarp":
        players[0].emaul_hits = [1]
        players[0].bgs_hits = [7]
        players[1].emaul_hits = [1]
        players[1].bgs_hits = [7]

    elif setup_name == "duo3EM1BGSxarp":
        players[0].emaul_hits = [1,7]
        players[1].emaul_hits= [1]
        players[1].bgs_hits = [17]
    
    return players