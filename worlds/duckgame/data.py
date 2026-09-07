from BaseClasses import ItemClassification

ITEM_LIST = {
    "Crates":ItemClassification.progression,
    "Huge Laser":ItemClassification.progression,
    "Jetpack":ItemClassification.progression,
    "Grapple":ItemClassification.progression,
    "Boots":ItemClassification.progression,
    "Pistol":ItemClassification.progression,
    "Snubby Pistol":ItemClassification.progression,
    "Desk":ItemClassification.trap,
    "Key":ItemClassification.progression,
    "Shotgun":ItemClassification.progression,
    "Magnum":ItemClassification.progression,
    "Combat Shotgun":ItemClassification.progression,
    "Chaingun":ItemClassification.progression,
    "Mace":ItemClassification.progression,
    "Phaser":ItemClassification.progression,
    "Wall Boots":ItemClassification.progression,
    "Flower":ItemClassification.useful,
    "Chainsaw":ItemClassification.progression,
    "Virtual Shotgun":ItemClassification.progression,
    "Blue Barrel":ItemClassification.trap,
    "Grenade":ItemClassification.progression,
    "Quad Laser":ItemClassification.progression,
    "Sniper":ItemClassification.progression,
    "Grenade Launcher":ItemClassification.progression,
    "Chest Plate":ItemClassification.trap,
    "Helmet":ItemClassification.progression,
    "Sword":ItemClassification.progression,
    "Mag Blaster":ItemClassification.progression,
    "Laser Rifle":ItemClassification.progression,
    "AK47":ItemClassification.progression,
}

FILLER_LIST = {
    "Clumsy":ItemClassification.trap,                   #Ragdoll
    "Stop Hitting Yourself":ItemClassification.trap,    #Brainrot
    "FIREEE!":ItemClassification.trap,                  #Fire
    "FIREEE*":ItemClassification.trap,                  #Fire Prank
    "Slippery Hands":ItemClassification.trap,           #Throw held item
    "Whats Under There?":ItemClassification.trap,       #Speed up/Teleport
    "Caught You!":ItemClassification.trap,              #Net
    "Duck Season":ItemClassification.trap,              #Suicide Gun
    "Hot Potato":ItemClassification.trap,               #Grenade in hand
    "Whats This?":ItemClassification.trap,              #Give random weapon
    "esreveR":ItemClassification.trap,                  #Reverse
    "A Gift for you":ItemClassification.trap,           #Death Crate
    "Don't look up":ItemClassification.trap,            #Grenade rain

    "Prot V":ItemClassification.filler,                 #Give armour
    "Make it rain":ItemClassification.filler,           #Infinite ammo

    "Filler":ItemClassification.filler,
}

SETTING_FILLER_LIST = {
    "ragdoll":"Clumsy",
    "brainrot":"Stop Hitting Yourself",
    "fire":"FIREEE!",
    "fire_prank":"FIREEE*",
    "drop":"Slippery Hands",
    "speed":"Whats Under There?",
    "net":"Caught You!",
    "suicide":"Duck Season",
    "grenade":"Hot Potato",
    "rand_weapon":"Whats This?",
    "reverse":"esreveR",
    "death_crate":"A Gift for you",
    "grenade":"Don't look up",
    "armour":"Prot V",
    "ammo":"Make it rain",
}

LEVEL_LIST = {
    "VARIETY ZONE - OBSTACLE COURSE":           [[],[],[],[],[]],
    "VARIETY ZONE - DEATH RAY 101":             [["Huge Laser"],[],[],[],[]],
    "VARIETY ZONE - SWING SHOES":               [["Grapple","Boots"],[],[],[],[]],
    "TARGET MISSIONS - STEP 1: OFFICE RAID":    [["Snubby Pistol","Pistol"],[],[],[],["AK47"]],
    "TARGET MISSIONS - STEP 2: INTEL":          [["Pistol","Jetpack"],[],[],[],["Shotgun","Magnum"]],
    "TARGET MISSIONS - STEP 3: HEADQUARTERS":   [["Key","Magnum","Boots","Combat Shotgun"],[],[],[],[]],
    "VARIETY ZONE 2 - MACE FACE":               [["Mace"],[],[],[],[]],
    "VARIETY ZONE 2 - PHASER 101":              [["Phaser"],[],[],[],[]],
    "VARIETY ZONE 2 - SWING SHOTGUN":           [["Combat Shotgun","Grapple"],[],[],[],[]],
    "SUPER SAW DUCK - WALL JUMP 101":           [["Wall Boots"],[],[],[],[]],
    "SUPER SAW DUCK - WOAH, SPIKES!":           [["Wall Boots"],[],[],[],[]],
    "SUPER SAW DUCK - SUPER DUCK CHAMP":        [["Wall Boots"],[],[],[],[]],
    "CHAINSAW RACING - OPEN ROAD":              [[],[],[],[],["Chainsaw"]],
    "CHAINSAW RACING - PRO TOUR":               [["Chainsaw"],[],[],[],[]],
    "CHAINSAW RACING - GRINDY 500":             [["Chainsaw"],[],[],["Key"],[]],
    "OFFICE WORK - WORKING LATE":               [[],[],[],[],["Crates"]],
    "OFFICE WORK - DOOR CRASHER":               [["Virtual Shotgun"],[],[],[],[]],
    "OFFICE WORK - INDUSTRIAL SHOOTOUT":        [["Pistol"],[],[],[],[]],
    "WEAPON TRAINING - GRENADE LAUNCHER 101":   [["Grenade Launcher"],[],[],[],[]],
    "WEAPON TRAINING - MAGNUM TRAINING":        [["Magnum"],[],[],[],[]],
    "WEAPON TRAINING - CHAINGUN JETPACK":       [["Chaingun"],[],["Jetpack"],[],[]],
    "TELEPORTERS - TELE TWISTER":               [["Grenade"],[],[],[],[]],
    "TELEPORTERS - LABYRINTH":                  [["Sword"],[],[],[],[]],
    "TELEPORTERS - DUCK DODGER":                [["Quad Laser"],[],[],[],[]],
    "VARIETY ZONE FINAL - ASCENSION":           [["Jetpack"],[],[],[],[]],
    "VARIETY ZONE FINAL - SNIPER 101":          [["Sniper"],[],[],[],[]],
    "VARIETY ZONE FINAL - SWING MACE":          [["Grapple","Mace"],[],["Helmet"],[],[]],
    "VARIETY ZONE FINAL II - GUN JUMPER":       [["Mag Blaster"],[],[],[],[]],
    "VARIETY ZONE FINAL II - REBOUND 101":      [["Laser Rifle"],[],[],[],[]],
    "VARIETY ZONE FINAL II - SAW CHAMPION":     [["Wall Boots"],[],[],[],["AK47"]],
}

medal_order = ["Bronze","Silver","Gold","Platinum","Developer"]
low_medal_order = ["Silver","Gold","Platinum","Bronze","Developer"]
level_list_keys = list(LEVEL_LIST.keys())
setting_filler_list_keys = list(SETTING_FILLER_LIST.keys())
