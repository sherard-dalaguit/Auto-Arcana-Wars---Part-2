from pathlib import Path
from characters import Warrior
from utils import RngEngine, BaseCharacter, Damage, Stats
from game import read_data
from typing import List
import os


def calculate_damage_taken(damage: Damage, character_stats: Stats) -> Stats:
    """
    Given the damage to be received by a character,
    calculate the actual damage done, taking into account the character's
    armor and magic resistance. The output should be the changes to be done to
    current_hp, provided as Stats
    """
    # if damage is None:
    #     return Stats()

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

    return 0


def your_attack(your_character: BaseCharacter, opponent_character: BaseCharacter,
                rng_engine: RngEngine, event_log: List[str],
                opponent_team: List[BaseCharacter], opponent_character_index: int) -> None | tuple[BaseCharacter, int]:
    """
    Simulates the player's attack on the opponent. Appends the result of the attack to a log.
    Checks if the opponent character is defeated or not, and if so,
    increments the opponent character index.

    Arguments:
        your_character -- The Character representing the player
        opponent_character -- The Character representation the opponent.
        rng_engine -- The randomness engine used for the battle simulation.
        log -- A list containing the log of events of the round.
        opponent_team -- A list containing the opponent's characters.
        opponent_character_index -- The index of the opponent's current character in
        the opponent's team list.

    Returns:
        Tuple containing the next opponent character and their index, or None if
        there are no more character's left.
    """

    event_log.append(play_turn(your_character, opponent_character, True, rng_engine))

    if opponent_character.effective_stats.current_hp <= 0:
        opponent_character_index += 1

        if opponent_character_index < len(opponent_team):
            opponent_character = opponent_team[opponent_character_index]
        else:
            return None

    return opponent_character, opponent_character_index


def opponent_attack(your_character: BaseCharacter, opponent_character: BaseCharacter,
                    rng_engine: RngEngine, event_log: List[str],
                    your_team: List[BaseCharacter], your_character_index: int) -> None | tuple[BaseCharacter, int]:
    """
    Simulates the opponent's attack on the player. Appends the result of the attack to a log.
    Checks if the player character is defeated or not, and if so,
    increments the player character index.

    Arguments:
        your_character -- The Character representing the player
        opponent_character -- The Character representation the opponent.
        rng_engine -- The randomness engine used for the battle simulation.
        log -- A list containing the log of events of the round.
        your_team -- A list containing the player's characters.
        your_character_index -- The index of the player's current character in
        the player's team list.

    Returns:
        Tuple containing the next player character and their index, or None if
        there are no more character's left.
    """

    event_log.append(play_turn(your_character, opponent_character, False, rng_engine))

    if your_character.effective_stats.current_hp <= 0:
        your_character_index += 1

        if your_character_index < len(your_team):
            your_character = your_team[your_character_index]
        else:
            return None

    return your_character, your_character_index


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

    if is_your_turn:
        attacker = your_character
        defender = opponent_character
    else:
        attacker = opponent_character
        defender = your_character

    special_chance = attacker.effective_stats.special_trigger_chance
    is_attack_special = rng_engine.rng(probability=special_chance)  # DO NOT change this line

    damage = attacker.basic_attack if not is_attack_special else attacker.special_attack

    if damage is not None:  # DO NOT change this line
        miss_chance = calculate_miss_chance(damage.damage, defender.effective_stats)
        is_damage_missed = rng_engine.rng(probability=miss_chance)  # DO NOT change this line

        if not is_damage_missed:
            defender.effective_stats = defender.effective_stats.add_stat_changes(
                calculate_damage_taken(damage.damage, defender.effective_stats))

    return damage.description


def play_round(your_assignment: Path, opponent_assignment: Path,
               is_your_turn_first: bool, rng_engine: RngEngine) -> tuple[bool, list[str]]:
    """Play the **round** out under the game engine.

    Arguments:
        your_assignment -- your team assignment for this round
        opponent_assignment -- the opponent's assignment for this round
        is_your_turn_first -- whether the first player to take turn is you
        rng_engine -- the rng system handling the randomness in the game

    Returns:
        a tuple of the outcome and a list of the **round** breakdown:
            - whether you won or not: True if you did, False otherwise
            - the turn-by-turn breakdown of what happened throughout
    """

    your_team = read_data(your_assignment)
    opponent_team = read_data(opponent_assignment)

    outcome, event_log = True, []

    your_character_index, opponent_character_index = 0, 0

    while your_character_index < len(your_team) and opponent_character_index < len(opponent_team):
        your_character = your_team[your_character_index]
        opponent_character = opponent_team[opponent_character_index]

        if not your_character or not opponent_character:
            break

        if is_your_turn_first:
            result = your_attack(your_character, opponent_character, rng_engine,
                                 event_log, opponent_team, opponent_character_index)
            if result is None:
                break
            else:
                opponent_character, opponent_character_index = result

        else:
            result = opponent_attack(your_character, opponent_character, rng_engine,
                                     event_log, your_team, your_character_index)
            if result is None:
                break
            else:
                your_character, your_character_index = result

    outcome = your_character_index > opponent_character_index

    return outcome, event_log


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

    your_points, opponent_points = 0, 0

    your_files = os.listdir(your_assignments)
    opponent_files = os.listdir(opponent_assignments)

    match_log = []

    for your_file, opponent_file in zip(your_files, opponent_files):
        your_assignment = your_assignments / your_file
        opponent_assignment = opponent_assignments / opponent_file

        outcome, round_log = play_round(your_assignment, opponent_assignment, is_your_turn_first, rng_engine)
        if outcome:
            your_points += 1
        else:
            opponent_points += 1

        for turn in round_log:
            match_log.append(turn)

    match_won = your_points > opponent_points

    return match_won, match_log


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
