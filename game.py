import json
from pathlib import Path
from typing import List, Dict, Type
from characters import Ninja, Mage, Warrior
from items import EnchantedSword, ShinyStaff, Pole, MagicCauldron, SolidRock
from utils import Stats, BaseItem, BaseCharacter


name_to_character_class: Dict[str, Type[BaseCharacter]] = {
    'ninja': Ninja,
    'mage': Mage,
    'warrior': Warrior
}

name_to_item_class: Dict[str, Type[BaseItem]] = {
    'enchanted_sword': EnchantedSword,
    'shiny_staff': ShinyStaff,
    'pole': Pole,
    'magic_cauldron': MagicCauldron,
    'solid_rock': SolidRock
}


def create_character(character_data: dict) -> BaseCharacter:
    """
    Creates and returns a character instance based on the provided character data.

    Args:
        character_data: A dictionary containing character attributes as key, value pairs.

    Returns:
        A class instance of the character.

    Raises:
        ValueError if the character name does not match predefined types.
    """
    stats_dict = character_data['character']['stats']
    stats_dict['current_hp'] = stats_dict['total_hp'] = float(stats_dict.pop('hp'))

    # Makes sure everything is a float, doesn't change its values though
    stats_dict = {stat_name: float(value) for stat_name, value in stats_dict.items()}

    base_stats = Stats(**stats_dict)
    character_name = character_data['character']['name']
    character_class = name_to_character_class.get(character_name)

    if not character_class:
        raise ValueError(f"Unknown character type: {character_name}")
    return character_class(base_stats)


def create_item(item_data: dict) -> BaseItem:
    """
    Creates and returns an item instance based on the provided item data.

    Args:
        item_data: A dictionary containing item attributes as key, value pairs.

    Returns:
        A class instance of the item.

    Raises:
        ValueError if the item name does not match predefined types.
    """
    item_stats_dict = item_data['stats']

    if item_data['name'] == 'magic_cauldron':  # Only MagicCauldron has hp attributes
        item_stats_dict['current_hp'] = item_stats_dict['total_hp'] = float(item_stats_dict.pop('hp', 0))

    # Makes sure everything is a float, doesn't change its values though
    item_stats_dict = {stat_name: float(value) for stat_name, value in item_stats_dict.items()}

    item_base_stats = Stats(**item_stats_dict)

    item_name = item_data['name']
    item_class = name_to_item_class.get(item_name)

    if not item_class:
        raise ValueError(f"Unknown item type: {item_name}")
    return item_class(item_base_stats)


def read_data(team_assignment: Path) -> List[BaseCharacter]:
    """
    Reads character and item data from a JSON file and creates respective
    character and item instances. Each character has their own list of items.

    Args:
        team_assignment: Path to the JSON data file.

    Returns:
        A list of character instances.
    """
    print(team_assignment.resolve())

    with team_assignment.open() as open_file:
        team_data = json.load(open_file)

    character_list = []
    for character_data in team_data:
        character = create_character(character_data)

        if 'items' in character_data:
            for item_data in character_data['items']:
                item = create_item(item_data)
                character.add_item(item)

        character_list.append(character)
    print_character_list(character_list)

    return character_list


def print_character_list(character_list: List[BaseCharacter]) -> None:
    """
    Prints out a formatted list of characters along with their attributes.

    Args:
        character_list (List[BaseCharacter]): List of characters to be printed.

    Notes:
        This function prints character information in a specific formatted manner.
        Spaces and tabulation in the output are tailored to align with the provided
        feedback on gradescope for readability and standardized grading evaluation.
    """

    for character_index, character in enumerate(character_list):
        print_stats(character_index, character)
        print_items(character)


def print_stats(index: int, character: BaseCharacter) -> None:
    """Prints the stats for a specific character"""
    print(f"{index + 1}: {character.name}")
    stats = character.effective_stats
    print(f"        Current HP: {stats.current_hp}")
    print(f"        Total HP: {stats.total_hp}")
    print(f"        Armor: {stats.armor}")
    print(f"        Magic Resistance: {stats.magic_resistance}")
    print(f"        Physical Power: {stats.physical_power}")
    print(f"        Magic Power: {stats.magic_power}")
    print(f"        Special Trigger Chance: {stats.special_trigger_chance}")


def print_items(character: BaseCharacter) -> None:
    """Lists the items held by a specific character"""
    if character.items:
        print("          with items:")
        for item_index, item in enumerate(character.items):
            print(f"                {item_index + 1}: {item.name}")
            print(f"                        {item.get_stats()}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--team_assignment",
                        type=str,
                        help="The location of the team assignment file to read",
                        default="./team_assignments/assignment_6.json",
                        required=False)
    args = parser.parse_args()
    team_assignment = Path(args.team_assignment)
    read_data(team_assignment=team_assignment)
