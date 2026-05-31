# -*- coding: utf-8 -*-
"""
systems/inventory.py
单一职责：背包管理 + 物品操作
"""

from core.player import Player

def show_inventory(player: Player) -> str:
    if not player.inventory:
        return "你的背包空空如也。"
    result = "【背包】\n"
    for item_id, count in player.inventory.items():
        result += f"  {item_id} x{count}\n"
    return result

def use_item(player: Player, item_id: str) -> str:
    if player.has_item(item_id):
        player.remove_item(item_id)
        return f"你使用了 {item_id}。"
    return "你没有这个物品。"