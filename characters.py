from utils import Stats, BaseCharacter, Attack, Damage


class Ninja(BaseCharacter):
	@property
	def name(self) -> str:
		"""Returns the name of the character."""
		return "Ninja"

	@property
	def special_attack_name(self) -> str:
		"""Returns the name of the character's special attack."""
		return "Special Attack: A precise poisoned dagger shot designed to incapacitate most opponents"

	@property
	def special_attack(self) -> Attack:
		"""
		Performs the Ninja's special attack: A poisoned dagger shot.

		This attack deals 40 base damage, plus additional damage equal
		to 50% of the Ninja's physical power and magic power.

		Returns:
			Attack: An instance of the Attack class, encapsulating
			the damage and a description of the attack
		"""

		new_damage = 40 + 0.5 * self.effective_stats.physical_power + 0.5 * self.effective_stats.magic_power
		damage_dealt = Damage(physical=new_damage)
		special_attack_description = f"""
		{self.name} performed {self.special_attack_name}, dealing {damage_dealt.physical} Physical Damage.
		"""

		return Attack(damage=damage_dealt, description=special_attack_description)


class Mage(BaseCharacter):
	@property
	def name(self) -> str:
		"""Returns the name of the character."""
		return "Mage"

	@property
	def special_attack_name(self) -> str:
		"""Returns the name of the character's special attack."""
		return "Special Attack: A lullaby to deep sleep"

	@property
	def special_attack(self) -> Attack:
		"""
		Performs the Mage's special attack: A lullaby to deep sleep.

		This attack deals 1 base damage, plus additional damage equal
		to 125% of the Mage's magic power.

		Returns:
			 Attack: An instance of the Attack class, encapsulating
			 the damage and a description of the attack
		"""

		new_damage = 1 + 1.25 * self.effective_stats.magic_power
		damage_dealt = Damage(magic=new_damage)
		special_attack_description = f"""
		{self.name} performed {self.special_attack_name}, dealing {damage_dealt.magic} Magic Damage.
		"""

		return Attack(damage=damage_dealt, description=special_attack_description)


class Warrior(BaseCharacter):
	@property
	def name(self) -> str:
		"""Returns the name of the character."""
		return "Warrior"

	@property
	def special_attack_name(self) -> str:
		"""Returns the name of the character's special attack."""
		return "Special Attack: A call to the shield hero"

	@property
	def special_attack(self) -> Attack:
		"""
		Performs the Warrior's special attack: A call to the shield hero.

		This 'attack' heals 50 base hp, plus additional hp equal
		to 75% of the Warrior's physical power and 300% of the Warrior's
		magic power.

		Returns:
			Attack: An instance of the Attack class, encapsulating
			the stat updates to self and a description of the attack
		"""

		healing_amount = 50 + 0.75 * self.effective_stats.physical_power + 3 * self.effective_stats.magic_power
		special_attack_description = f"""
		{self.name} performed {self.special_attack_name}, healing {healing_amount} HP.
		"""

		return Attack(damage=Damage(), stat_updates_to_self=Stats(current_hp=healing_amount),
					  description=special_attack_description)
