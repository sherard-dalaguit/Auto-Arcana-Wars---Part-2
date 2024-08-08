import json
from pathlib import Path
from typing import Dict, Type
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


def read_data(team_assignment: Path) -> list[BaseCharacter]:
    """
    Reads character and item data from a JSON file and creates respective
    character and item instances. Each character has their own list of items.

    Args:
        team_assignment: Path to the JSON data file.

    Returns:
        A list of character instances.
    """

    with open(team_assignment, "r") as f:
        read_assignment = json.load(f)

    character_list = []
    for character_data in read_assignment:
        character_name = character_data["character"]["name"]
        character_stats = character_data["character"]["stats"]
        character_stats.update({"current_hp": character_stats["hp"],
                                "total_hp": character_stats["hp"]})
        del character_stats["hp"]
        character_stats = Stats(**character_stats)
        new_character = name_to_character_class[character_name](base_stats=character_stats)
        if "items" in character_data:
            for item_data in character_data["items"]:
                item_name = item_data["name"]
                item_stats = item_data["stats"]
                if "hp" in item_stats:
                    item_stats.update({"current_hp": item_stats["hp"],
                                       "total_hp": item_stats["hp"]})
                    del item_stats["hp"]
                item_stats = Stats(**item_stats)
                item = name_to_item_class[item_name](base_item_stats=item_stats)
                new_character.add_item(item)
        character_list.append(new_character)

    return character_list


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--assignment",
                        type=str,
                        help="The location of the team assignment file to read",
                        default="./team_assignments/assignment_1.json",
                        required=False)
    args = parser.parse_args()
    team_assignment = Path(args.assignment)
    characters = read_data(team_assignment=team_assignment)
    for i, character in enumerate(characters):
        print(f"{i + 1}. {character}")
