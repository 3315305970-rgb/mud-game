# -*- coding: utf-8 -*-
"""
systems/buff.py
单一职责：状态效果系统（Buff/Debuff）
"""

from core.player import Player

def apply_buff(player: Player, buff_name: str, duration: int = 3) -> str:
    if "buffs" not in player.flags:
        player.flags["buffs"] = {}
    player.flags["buffs"][buff_name] = duration
    return f"获得状态：{buff_name}（持续 {duration} 回合）"

def tick_buffs(player: Player) -> str:
    if "buffs" not in player.flags:
        return ""
    result = []
    for buff in list(player.flags["buffs"].keys()):
        player.flags["buffs"][buff] -= 1
        if player.flags["buffs"][buff] <= 0:
            del player.flags["buffs"][buff]
            result.append(f"{buff} 效果消失")
    return "\n".join(result) if result else ""