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
    "Mace Collar":ItemClassification.progression,
    "Weight Ball":ItemClassification.progression,
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
    "AK47":ItemClassification.useful,
    "Filler":ItemClassification.filler,
}

LEVEL_LIST = {
    "VARIETY ZONE - OBSTACLE COURSE":[],
    "VARIETY ZONE - DEATH RAY 101":["Huge Laser"],
    "VARIETY ZONE - SWING SHOES":["Grapple","Boots"],
    "TARGET MISSIONS - STEP 1: OFFICE RAID":["Snubby Pistol"],
    "TARGET MISSIONS - STEP 2: INTEL":["Pistol","Key","Jetpack"],
    "TARGET MISSIONS - STEP 3: HEADQUARTERS":["Key","Crates","Magnum","Boots","Combat Shotgun"],
    "VARIETY ZONE 2 - MACE FACE":["Mace Collar","Weight Ball"],
    "VARIETY ZONE 2 - PHASER 101":["Phaser"],
    "VARIETY ZONE 2 - SWING SHOTGUN":["Grapple","Combat Shotgun"],
    "SUPER SAW DUCK - WALL JUMP 101":["Wall Boots"],
    "SUPER SAW DUCK - WOAH, SPIKES!":["Wall Boots"],
    "SUPER SAW DUCK - SUPER DUCK CHAMP":["Wall Boots"],
    "CHAINSAW RACING - OPEN ROAD":["Chainsaw"],
    "CHAINSAW RACING - PRO TOUR":["Chainsaw"],
    "CHAINSAW RACING - GRINDY 500":["Chainsaw"],
    "OFFICE WORK - WORKING LATE":[],
    "OFFICE WORK - DOOR CRASHER":["Virtual Shotgun"],
    "OFFICE WORK - INDUSTRIAL SHOOTOUT":["Pistol"],
    "WEAPON TRAINING - GRENADE LAUNCHER 101":["Grenade Launcher"],
    "WEAPON TRAINING - MAGNUM TRAINING":["Magnum"],
    "WEAPON TRAINING - CHAINGUN JETPACK":["Jetpack","Chaingun"],
    "TELEPORTERS - TELE TWISTER":["Grenade"],
    "TELEPORTERS - LABYRINTH":["Sword"],
    "TELEPORTERS - DUCK DODGER":["Quad Laser"],
    "VARIETY ZONE FINAL - ASCENSION":["Jetpack"],
    "VARIETY ZONE FINAL - SNIPER 101":["Sniper"],
    "VARIETY ZONE FINAL - SWING MACE":["Grapple","Mace Collar","Weight Ball","Helmet"],
    "VARIETY ZONE FINAL II - GUN JUMPER":["Mag Blaster"],
    "VARIETY ZONE FINAL II - REBOUND 101":["Laser Rifle"],
    "VARIETY ZONE FINAL II - SAW CHAMPION":["Wall Boots"],
}

# ALL_ITEMS
# Crates
# Huge Laser
# Jetpack
# Grapple
# Boots
# Pistol
# Snubby Pistol
# Desk
# Key
# Shotgun
# Magnum
# Combat Shotgun
# Chaingun
# Mace Collar
# Weight Ball
# Phaser
# Wall Boots
# Flower
# Chainsaw
# Virtual Shotgun
# Blue Barrel
# Grenade
# Quad Laser
# Sniper
# Grenade Launcher
# Chest Plate
# Helmet
# Sword
# Mag Blaster
# Laser Rifle
# AK47


# VARIETY ZONE
# OBSTACLE COURSE
# 1abc0a39-09e1-424f-9e21-9602c41b7da9
# none
# DEATH RAY 101
# 3ece00ba-d342-42b3-b22f-4ed21d75d062
# Huge Laser
# SWING SHOES
# 5a3ee55f-4149-4f2a-a222-95d1d52c8b8b
# Grapple,Boots

# TARGET MISSIONS
# STEP 1: OFFICE RAID
# 6e82639f-f0a1-4066-b08f-885392d81af7
# Snubby Pistol
# STEP 2: INTEL
# a618f1b0-d21e-4799-a097-cceb9bbbd675
# Pistol,Key,Jetpack
# STEP 3: HEADQUARTERS
# ff770032-94a7-4ab3-a0ba-5b6592d0e6d4
# Key,Crates,Magnum,Boots,Combat Shotgun

# VARIETY ZONE 2
# MACE FACE
# 588541bc-ffa3-4bdf-ac18-65c546818abe
# Mace Collar,Weight Ball
# PHASER 101
# 8a35adf1-3d07-430f-9dff-85cc0d3499a7
# Phaser
# SWING SHOTGUN
# 8bfb3be0-6c48-40af-8cf9-d997580ad931
# Grapple,Combat Shotgun

# SUPER SAW DUCK
# WALL JUMP 101
# 77ef8770-e7bf-44ac-b073-a7eadf8bf68d
# Wall Boots
# WOAH, SPIKES!
# cca244a5-946e-451c-9138-5ecf4776fdab
# Wall Boots
# SUPER DUCK CHAMP
# 9c8c5dd0-b2c9-4897-a9a2-beac49d3b366
# Wall Boots

# CHAINSAW RACING
# OPEN ROAD
# 23ff1f65-cf6a-4065-8857-43b12a587bf8
# Chainsaw
# PRO TOUR
# 127e162f-d016-4ae1-8ae5-a51101675713
# Chainsaw
# GRINDY 500
# 8e5a2b40-4c7b-460b-89a0-ab7910c530ab
# Chainsaw

# OFFICE WORK
# WORKING LATE
# a66c52a5-85fd-4399-b6c8-4a835c103771
# none
# DOOR CRASHER
# dc13e85a-ba4d-4819-afc9-b992b8a8fee1
# Virtual Shotgun
# INDUSTRIAL SHOOTOUT
# c5619b71-242f-48b9-8155-f430c66249fc
# Pistol

# WEAPON TRAINING
# GRENADE LAUNCHER 101
# b63bda64-4e7a-48ce-9d35-a49847c6612c
# Grenade Launcher
# MAGNUM TRAINING
# 6a67885f-341f-4722-b91e-70074c26f713
# Magnum
# CHAINGUN JETPACK
# 9be5612f-e004-4e94-9aba-0831b58a0f22
# Jetpack,Chaingun

# TEPEPORTERS
# TELE TWISTER
# 882626cc-16a3-436c-84ce-19ed8c21369a
# Grenade
# LABYRINTH
# f9761908-9d32-405e-adda-8ddf7c4a891d
# Sword
# DUCK DODGER
# c25b870c-3eef-41e6-a89f-0ef949c13ae4
# Quad Laser

# VARIETY ZONE FINAL
# ASCENSION
# 1b1188f7-6495-4317-a9dd-5f842d6bdec8
# Jetpack
# SNIPER 101
# 0ca36b08-c2bf-4dc7-bc19-492abf3691eb
# Sniper
# SWING MACE
# 9b081557-8042-4d31-a5dd-304b831f435b
# Grapple,Mace Collar,Weight Ball,Helmet

# VARIETY ZONE FINAL II
# GUN JUMPER
# 79586b9f-c989-4851-afce-d6c296db97f3
# Mag Blaster
# REBOUND 101
# 2d250f85-25f4-43ec-ad14-5010ce25eee2
# Laser Rifle
# SAW CHAMPION
# 1597667b-bd53-42be-9ba6-7eab66b13625
# Wall Boots