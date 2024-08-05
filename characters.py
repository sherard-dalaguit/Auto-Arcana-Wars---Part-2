from utils import BaseCharacter


class Ninja(BaseCharacter):
	@property
	def name(self) -> str:
		"""Returns the name of the character."""
		return "Ninja"

	@property
	def special_attack_name(self) -> str:
		"""Returns the name of the character and its special attack."""
		return f"{self.name}: A poisoned dagger shot"

	def special_attack(self) -> float:
		"""
		Performs the Ninja's special attack: A poisoned dagger shot.

		This attack deals 40 base damage, plus additional damage equal
		to 50% of the Ninja's physical power and magic power.

		Returns:
			float: The character's special attack damage
		"""

		damage = 40 + 0.5 * self.base_stats.physical_power + 0.5 * self.base_stats.magic_power

		return damage


class Mage(BaseCharacter):
	@property
	def name(self) -> str:
		"""Returns the name of the character."""
		return "Mage"

	@property
	def special_attack_name(self) -> str:
		"""Returns the name of the character and its special attack."""
		return f"{self.name}: A lullaby to deep sleep"

	def special_attack(self) -> float:
		"""
		Performs the Mage's special attack: A lullaby to deep sleep.

		This attack deals 1 base damage, plus additional damage equal
		to 125% of the Mage's magic power.

		Returns:
			 float: The character's special attack damage
		"""

		damage = 1 + 1.25 * self.base_stats.magic_power

		return damage


class Warrior(BaseCharacter):
	@property
	def name(self) -> str:
		"""Returns the name of the character."""
		return "Warrior"

	@property
	def special_attack_name(self) -> str:
		"""Returns the name of the character and its special attack."""
		return f"{self.name}: A call to the shield hero"

	def special_attack(self) -> float:
		"""
		Performs the Warrior's special attack: A call to the shield hero.

		This 'attack' heals 50 base hp, plus additional hp equal
		to 75% of the Warrior's physical power and 300% of the Warrior's
		magic power.

		Returns:
			float: The character's special attack healing
		"""

		healing = 50 + 0.75 * self.base_stats.physical_power + 3 * self.base_stats.magic_power

		return healing
