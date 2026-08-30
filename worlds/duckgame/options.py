from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle
from . import data

class TotalArcadeLevels(Range):
    """
    The total number of arcade levels to be included

    """
    display_name = "Arcade Level Count"
    range_start = 1
    range_end = len(data.LEVEL_LIST)
    default = len(data.LEVEL_LIST)

class MedalCountGoal(Range):
    """
    The amount of necessary medals to goal
    If this is higher than amount of medals in-game it will be the max amount

    """
    display_name = "Medal Count for Goal"
    range_start = 1
    range_end = len(data.LEVEL_LIST)*5
    default = len(data.LEVEL_LIST)*4

class SendLowerMedals(DefaultOnToggle):
    """
    When you recieve a medal whether to send lower medals
    EX. Recieving Gold sends: Gold, Silver, Bronze

    """
    display_name = "Send Lower Medals"

class BronzeMedal(Toggle):
    """
    Whether to use Bronze Medals as possible locations
    The more medals you select the more filler/trap is included

    """
    display_name = "Use Bronze Medals"

class SilverMedal(DefaultOnToggle):
    """
    Whether to use Silver Medals as possible locations
    The more medals you select the more filler/trap is included

    """
    display_name = "Use Silver Medals"

class GoldMedal(DefaultOnToggle):
    """
    Whether to use Gold Medals as possible locations
    The more medals you select the more filler/trap is included

    """
    display_name = "Use Gold Medals"

class PlatinumMedal(DefaultOnToggle):
    """
    Whether to use Platinum Medals as possible locations
    The more medals you select the more filler/trap is included

    """
    display_name = "Use Platinum Medals"

class DeveloperMedal(Toggle):
    """
    Whether to use Developer Medals as possible locations
    The more medals you select the more filler/trap is included

    """
    display_name = "Use Developer Medals"

class MinMedalTypes(Range):
    """
    The minimum amount of medals types to be included
    Will never generate with less medals per level than this
    The more medals you select the more filler/trap is included
    Below 3 it may not be possible to not gen due to lack of locations for items
    
    """
    display_name = "Minimum Medal types"
    range_start = 1
    range_end = 5
    default = 3

class TrapPercent(Range):
    """
    Percentage of filler items that are traps
    Any items that are not traps(includes traps&anti-traps) are empty items that do nothing
    
    """
    display_name = "Trap Percent"
    range_start = 0
    range_end = 100
    default = 100

class RagdollTrapWeight(Range):
    """
    Weight of be Clumsy Trap
    Clumsy trap triggers ragdoll every 3 seconds up to 5 times
    
    """
    display_name = "Clumsy Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class BrainrotTrapWeight(Range):
    """
    Weight of Stop Hitting Yourself Trap
    Stop Hitting Yourself Trap activates "Brainrot" for 10 seconds
    
    """
    display_name = "Stop Hitting Yourself Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class FireTrapWeight(Range):
    """
    Weight of FIREEE! Trap
    FIREEE! Trap sets you on fire
    
    """
    display_name = "FIREEE! Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class FirePrankTrapWeight(Range):
    """
    Weight of FIREEE* Trap
    FIREEE* Trap sets you on fire and extinguishes before death
    
    """
    display_name = "FIREEE* Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class DropTrapWeight(Range):
    """
    Weight of Slippery Hands Trap
    Slippery Hands Trap drops held item
    
    """
    display_name = "Slippery Hands Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class SpeedTrapWeight(Range):
    """
    Weight of Whats Under There? Trap
    Whats Under There? Trap teleports you 5 frames every 0.25 seconds for up to 25 times
    
    """
    display_name = "Whats Under There? Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class NetTrapWeight(Range):
    """
    Weight of Caught You! Trap
    Caught You! Trap puts you in a net
    
    """
    display_name = "Caught You! Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class SuicideTrapWeight(Range):
    """
    Weight of Duck Season Trap
    Duck Season Trap replaces your weapon with the suicide gun
    
    """
    display_name = "Duck Season Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class GrenadeTrapWeight(Range):
    """
    Weight of Hot Potato Trap
    Hot Potato Trap gives you an active grenade
    
    """
    display_name = "Hot Potato Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class RandWeaponTrapWeight(Range):
    """
    Weight of Whats This? Trap
    Whats This? Trap gives you a random weapon/item
    
    """
    display_name = "Whats This? Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class ReverseTrapWeight(Range):
    """
    Weight of esreveR Trap
    esreveR Trap reverses your left and right inputs for 10 seconds
    
    """
    display_name = "esreveR Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class DeathCrateTrapWeight(Range):
    """
    Weight of A Gift for you Trap
    A Gift for you Trap is BAD(mostly)/spawns a random Death Crate
    
    """
    display_name = "A Gift for you Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class GrenadeRainTrapWeight(Range):
    """
    Weight of Don't look up Trap
    Don't look up Trap spawns a bunch of active grenades on the screen, Look out!
    
    """
    display_name = "Don't look up Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class ArmourTrapWeight(Range):
    """
    Weight of Prot V Anti-Trap
    Prot V Anti-Trap gives you armour
    
    """
    display_name = "Prot V Anti-Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class AmmoTrapWeight(Range):
    """
    Weight of Make it rain Anti-Trap
    Make it rain Anti-Trap gives you infinite ammo for the weapon you are holding
    
    """
    display_name = "Make it rain Anti-Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class DuckGameOptions(PerGameCommonOptions):
    total_arcade_levels:TotalArcadeLevels
    medal_count_goal:MedalCountGoal
    send_lower_medals:SendLowerMedals
    use_bronze_medal:BronzeMedal
    use_silver_medal:SilverMedal
    use_gold_medal:GoldMedal
    use_platinum_medal:PlatinumMedal
    use_developer_medal:DeveloperMedal
    min_medal_types:MinMedalTypes

    trap_percent:TrapPercent
    ragdoll_weight:RagdollTrapWeight
    brainrot_weight:BrainrotTrapWeight
    fire_weight:FireTrapWeight
    fire_prank_weight:FirePrankTrapWeight
    drop_weight:DropTrapWeight
    speed_weight:SpeedTrapWeight
    net_weight:NetTrapWeight
    suicide_weight:SuicideTrapWeight
    grenade_weight:GrenadeTrapWeight
    rand_weapon_weight:RandWeaponTrapWeight
    reverse_weight:ReverseTrapWeight
    death_crate_weight:DeathCrateTrapWeight
    grenade_rain_weight:GrenadeRainTrapWeight
    armour_weight:ArmourTrapWeight
    ammo_weight:AmmoTrapWeight


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
# option_groups = [
#     OptionGroup(
#         "Gameplay Options",
#         [HardMode, Hammer, ExtraStartingChest, StartWithOneConfettiCannon, TrapChance],
#     ),
#     OptionGroup(
#         "Aesthetic Options",
#         [ConfettiExplosiveness, PlayerSprite],
#     ),
# ]
option_groups = []

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
# option_presets = {
#     "boring": {
#         "hard_mode": False,
#         "hammer": False,
#         "extra_starting_chest": False,
#         "start_with_one_confetti_cannon": False,
#         "trap_chance": 0,
#         "confetti_explosiveness": ConfettiExplosiveness.range_start,
#         "player_sprite": PlayerSprite.option_human,
#     },
#     "the true way to play": {
#         "hard_mode": True,
#         "hammer": True,
#         "extra_starting_chest": True,
#         "start_with_one_confetti_cannon": True,
#         "trap_chance": 50,
#         "confetti_explosiveness": ConfettiExplosiveness.range_end,
#         "player_sprite": PlayerSprite.option_duck,
#     },
# }
option_presets = {}
