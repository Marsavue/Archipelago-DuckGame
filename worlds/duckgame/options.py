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
    Below 3 it is possible to not gen due to lack of locations for items
    
    """
    display_name = "Minimum Medal types"
    range_start = 1
    range_end = 5
    default = 3


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
