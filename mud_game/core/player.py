# -*- coding: utf-8 -*-
"""
core/player.py
单一职责：玩家角色类 + 基础属性管理
"""

class Player:
    def __init__(self, name="无名"):
        self.name = name
        self.location = "qingshui_town_start"
        self.realm = "武师"
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.mp = 50
        self.max_mp = 50
        self.gold = 100
        self.lust = 0
        self.inventory = {}
        self.equipment = {}
        self.relationships = {}
        self.flags = {}

    def add_item(self, item_id, count=1):
        self.inventory[item_id] = self.inventory.get(item_id, 0) + count

    def remove_item(self, item_id, count=1):
        if item_id in self.inventory:
            self.inventory[item_id] -= count
            if self.inventory[item_id] <= 0:
                del self.inventory[item_id]
            return True
        return False

    def has_item(self, item_id, count=1):
        return self.inventory.get(item_id, 0) >= count

    def get_status(self):
        return (
            f"【{self.name}】\n"
            f"境界：{self.realm} | 等级：{self.level}\n"
            f"生命：{self.hp}/{self.max_hp} | 灵力：{self.mp}/{self.max_mp}\n"
            f"铜钱：{self.gold} | 性欲：{self.lust}/100\n"
            f"位置：{self.location}"
        )

    def move_to(self, new_location):
        self.location = new_location

    def add_relationship(self, npc_id, rel_type, favor=0):
        self.relationships[npc_id] = {"type": rel_type, "favor": favor}

    def change_favor(self, npc_id, delta):
        if npc_id in self.relationships:
            self.relationships[npc_id]["favor"] += delta
            return self.relationships[npc_id]["favor"]
        return 0