# -*- coding: utf-8 -*-
"""
systems/crafting.py
单一职责：打造/炼器系统
"""

from core.player import Player

def forge_equipment(player: Player, equip_type: str = "铁剑") -> str:
    if player.gold < 30:
        return "材料不足，无法打造。"
    
    player.gold -= 30
    player.add_item("iron_sword", 1)
    return f"打造成功！获得 {equip_type} x1"