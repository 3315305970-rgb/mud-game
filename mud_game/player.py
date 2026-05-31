# -*- coding: utf-8 -*-
"""玩家角色系统 - 凡人界 MUD
"""

class Player:
    def __init__(self, name="无名"):
        self.name = name
        self.location = "qingshui_town_start"  # 初始位置
        self.realm = "武师"  # 境界
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.mp = 50
        self.max_mp = 50
        self.gold = 100  # 初始铜钱
        self.lust = 0  # 性欲值 (0-100)
        self.inventory = {}  # {item_id: count}
        self.equipment = {}  # 装备槽
        self.relationships = {}  # 关系身份记录 {npc_id: {"type": "qingmei_bamboo_horse", "favor": 30}}
        self.flags = {}  # 剧情标记

    def add_item(self, item_id, count=1):
        if item_id in self.inventory:
            self.inventory[item_id] += count
        else:
            self.inventory[item_id] = count

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
        return f"你来到了 {new_location}。"

    def add_relationship(self, npc_id, rel_type, favor=0):
        self.relationships[npc_id] = {"type": rel_type, "favor": favor}

    def change_favor(self, npc_id, delta):
        if npc_id in self.relationships:
            self.relationships[npc_id]["favor"] += delta
            return self.relationships[npc_id]["favor"]
        return 0