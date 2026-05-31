# -*- coding: utf-8 -*-
"""
systems/pet.py
单一职责：灵宠/炼妖壶系统（捕捉、培养、打书）
"""

from core.player import Player

class Pet:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.skills = []

def catch_pet(player: Player, pet_name: str = "小狐妖") -> str:
    player.add_item("pet_egg", 1)
    return f"成功捕捉 {pet_name}！获得宠物蛋 x1"

def book_pet(player: Player, skill: str = "魅惑") -> str:
    if not player.has_item("pet_egg"):
        return "没有宠物可打书。"
    player.remove_item("pet_egg")
    return f"宠物学会 {skill} 技能！"