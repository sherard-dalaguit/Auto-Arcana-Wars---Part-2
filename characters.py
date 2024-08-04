from utils import BaseCharacter

class Ninja(BaseCharacter):
    @property
    def name(self) -> str:
        return "Ninja"
    
    @property
    def special_attack_name(self) -> str:
        return (
            "Special Attack: A precise poisoned dagger shot designed to "
            "incapacitate most opponents"
        )
        
        
class Mage(BaseCharacter):
    @property
    def name(self) -> str:
        return "Mage"
    
    @property
    def special_attack_name(self) -> str:
        return "Special Attack: A lullaby to deep sleep"
    

class Warrior(BaseCharacter):
    @property
    def name(self) -> str:
        return "Warrior"
    
    @property
    def special_attack_name(self) -> str:
        return "Special Attack: A call to the shield hero"
    