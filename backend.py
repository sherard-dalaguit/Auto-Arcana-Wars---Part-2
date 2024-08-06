from pathlib import Path
from utils import RngEngine, BaseCharacter, Damage, Stats


def calculate_damage_taken(damage: Damage, character_stats: Stats) -> Stats:
    """
    Given the damage to be received by a character,
    calculate the actual damage done, taking into account the character's
    armor and magic resistance. The output should be the changes to be done to
    current_hp, provided as Stats
    """

    damage_dealt = 0

    if damage.physical > 0:
        damage_dealt += damage.physical * (1 - character_stats.armor / 100)

    if damage.magic > 0:
        damage_dealt += damage.magic * (1 - character_stats.magic_resistance / 100)

    damage_stats = Stats(current_hp=-damage_dealt)
    return damage_stats


def calculate_miss_chance(damage: Damage, character_stats: Stats) -> float:
    """
    Given the damage to be received by a character,
    calculate the percentage probability (a number between 0 and 100)
    that the character has to miss the damage entirely.
    """

    if damage.physical > 0:
        physical_miss_chance = character_stats.armor / 10
        return physical_miss_chance

    elif damage.magic > 0:
        magic_miss_chance = character_stats.magic_resistance / 10
        return magic_miss_chance


def play_turn(your_character: BaseCharacter, opponent_character: BaseCharacter,
              is_your_turn: bool, rng_engine: RngEngine) -> str:
    """Take a turn in the game, updating the character's stats and returning 
        a description of what happened in the turn
        
    Raises:
        ValueError if any of the characters are already dead (0 current_hp)

    Arguments:
        your_character -- your character in the combat
        opponent_character -- the opponent's character
        is_your_move -- whether it is your move or not
        rng_engine -- the rng system handling the randomness in the game

    Returns:
        the description of what happened in the move
    """  
    special_chance = 0.0  # change this
    is_attack_special = rng_engine.rng(probability=special_chance)  # DO NOT change this line

    damage = None  # change this
    
    if damage is not None:  # DO NOT change this line
        miss_chance = 0.0  # change this
        is_damage_missed = rng_engine.rng(probability=miss_chance)  # DO NOT change this line
            
    return ""


def play_match(your_assignments: Path, 
               opponent_assignments: Path,
               rng_engine: RngEngine) -> tuple[bool, list[str]]:
    """Play the match out under the game engine. 

    Arguments:
        your_assignments -- your assignments for all rounds in the match
        opponent_assignments -- the opponent's assignments for all rounds in the match
        rng_engine -- the rng system handling the randomness in the game

    Returns:
        a tuple of the outcome and a list of the match breakdown:
            - whether you won or not: True if you did, False otherwise
            - the turn-by-turn breakdown of what happened throughout
    """
    
    is_your_turn_first = rng_engine.rng(probability=50)  # DO NOT change this line
        
    return False, []
    
    
if __name__ == "__main__":
    from argparse import ArgumentParser
    
    parser = ArgumentParser()
    parser.add_argument("--your_assignments", 
                        type=str, 
                        help="The location of the team assignment file to read",
                        default="./samples/match_1/your_assignments",
                        required=False)
    parser.add_argument("--opponent_assignments", 
                        type=str, 
                        help="The location of the team assignment file to read",
                        default="./samples/match_1/opponent_assignments",
                        required=False)
    parser.add_argument("--output_file", 
                        type=str, 
                        help="The location to the text file to store the output in.",
                        default=None, 
                        required=False)
    args = parser.parse_args()
    your_assignments = Path(args.your_assignments)
    opponent_assignments = Path(args.opponent_assignments)
    rng_engine = RngEngine()  # DO NOT change this line
    match_outcome, description = play_match(your_assignments=your_assignments, 
               opponent_assignments=opponent_assignments, 
               rng_engine=rng_engine)
    if args.output_file is not None:
        with open(args.output_file, "w") as f:
            print(*description, sep="\n", file=f)
    else:
        print(*description, sep="\n")
