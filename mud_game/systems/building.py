# -*- coding: utf-8 -*-
"""
systems/building.py
单一职责：功能建筑系统（武馆、药铺、铁匠铺等）
"""

from core.player import Player

def train_at_wuguan(player: Player) -> str:
    if player.gold < 10:
        return "铜钱不足，无法训练。"
    player.gold -= 10
    player.level += 1
    return f"武馆训练完成！等级 +1，花费 10 铜钱。"

def rest_at_inn(player: Player) -> str:
    player.hp = player.max_hp
    player.mp = player.max_mp
    return "在客栈休息一晚，生命与灵力完全恢复。"