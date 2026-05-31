# -*- coding: utf-8 -*-
"""
systems/alchemy.py
单一职责：炼药系统（丹药制作）
"""

from core.player import Player

def refine_pill(player: Player, pill_type: str = "回血丹") -> str:
    if player.gold < 20:
        return "铜钱不足，无法炼药。"
    
    player.gold -= 20
    if pill_type == "回血丹":
        player.add_item("healing_pill", 1)
        return "炼制成功！获得 低阶回血丹 x1"
    return "未知丹药类型。"