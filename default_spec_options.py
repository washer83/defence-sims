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