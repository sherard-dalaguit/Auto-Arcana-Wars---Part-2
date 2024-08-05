from utils import Stats, BaseItem


class EnchantedSword(BaseItem):
	@property
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Enchanted Sword"

	@property
	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: Lucky Strike"

	@property
	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return True

	def get_stats(self) -> str:
		"""
		Overridden from BaseItem.

		This method returns a string illustrating the specific stats of an EnchantedSword item.

		This method is used in the 'game.py', within the 'print_character_list()' function
		to print the stats of each item	owned by a character in a readable format.

		Returns:
			A string containing the stats of the EnchantedSword.
		"""
		return (f"Physical Power: {self.base_item_stats.physical_power}\n"
				f"						Magic Power: {self.base_item_stats.magic_power}")

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""

		if self.is_passive_active:
			return self.base_item_stats._replace(special_trigger_chance=5 + 0.25 * base_character_stats.special_trigger_chance)
		return self.base_item_stats


class ShinyStaff(BaseItem):
	@property
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Shiny Staff"

	@property
	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: Blessings of Echo"

	@property
	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return False

	def get_stats(self) -> str:
		"""
		Overridden from BaseItem.

		This method returns a string illustrating the specific stats of a ShinyStaff item.

		This method is used in the 'game.py', within the 'print_character_list()' function
		to print the stats of each item	owned by a character in a readable format.

		Returns:
			A string containing the stats of the ShinyStaff.
		"""
		return (f"Physical Power: {self.base_item_stats.physical_power}\n"
				f"						Magic Power: {self.base_item_stats.magic_power}")

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""

		effective_stats = self.base_item_stats

		if self.is_passive_active:
			added_effect = Stats(magic_power=1 + 0.5 * base_character_stats.magic_power)
			effective_stats = effective_stats.add_stat_changes(added_effect)

		return effective_stats


class Pole(BaseItem):
	@property
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Pole"

	@property
	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: No passive abilities"

	@property
	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return False

	def get_stats(self) -> str:
		"""
		Overridden from BaseItem.

		This method returns a string illustrating the specific stats of a Pole item.

		This method is used in the 'game.py', within the 'print_character_list()' function
		to print the stats of each item	owned by a character in a readable format.

		Returns:
			A string containing the stats of the Pole.
		"""
		return (f"Physical Power: {self.base_item_stats.physical_power}\n"
				f"						Magic Power: {self.base_item_stats.magic_power}")

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""

		return self.base_item_stats


class MagicCauldron(BaseItem):
	@property
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Magic Cauldron"

	@property
	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: Potion of Life"

	@property
	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return True

	def get_stats(self) -> str:
		"""
		Overridden from BaseItem.

		This method returns a string illustrating the specific stats of a MagicCauldron item.

		This method is used in the 'game.py', within the 'print_character_list()' function
		to print the stats of each item	owned by a character in a readable format.

		Returns:
			A string containing the stats of the MagicCauldron.
		"""
		return f"HP: {self.base_item_stats.current_hp}"

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""

		effective_stats = self.base_item_stats

		if self.is_passive_active:
			added_effect = Stats(current_hp=10 + 0.3 * base_character_stats.total_hp,
								 total_hp=10 + 0.3 * base_character_stats.total_hp)
			effective_stats = effective_stats.add_stat_changes(added_effect)

		return effective_stats


class SolidRock(BaseItem):
	@property
	def name(self) -> str:
		"""Returns the name of the item."""
		return "Solid Rock"

	@property
	def passive_name(self) -> str:
		"""Returns the name of the item and its special ability."""
		return f"{self.name}: No passive abilities"

	@property
	def is_unique_passive(self) -> bool:
		"""Returns whether an item has a unique passive effect."""
		return False

	def get_stats(self) -> str:
		"""
		Overridden from BaseItem.

		This method returns a string illustrating the specific stats of an EnchantedSword item.

		This method is used in the 'game.py', within the 'print_character_list()' function
		to print the stats of each item	owned by a character in a readable format.

		Returns:
			A string containing the stats of the EnchantedSword.
		"""
		return (f"Armor: {self.base_item_stats.armor}\n"
				f"						Magic Resistance: {self.base_item_stats.magic_resistance}")

	def calculate_effective_stats(self, base_character_stats: Stats) -> Stats:
		"""
		Calculates the effective stats after equipping the item.

		The new stats will be based on the base character stats and
		the passive ability effects if the passive is active.

		Args:
			base_character_stats (Stats): The basic character stats before equipping the item

		Returns:
			Stats: The new character stats after equipping the item.
		"""
		return self.base_item_stats
