# Player and NPC base classes

from evennia import DefaultCharacter

class MortalCharacter(DefaultCharacter):
    """Custom player character with cultivation and lust system."""
    def at_object_creation(self):
        super().at_object_creation()
        self.db.level = 1
        self.db.realm = '武师入门'
        self.db.lust = 20
        self.db.harem = []
        self.db.sex_attrs = {}  # sensitive zones, preferences etc.

class NpcCharacter(MortalCharacter):
    """NPCs with dialogue and relationship system."""
    pass