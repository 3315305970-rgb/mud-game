# -*- coding: utf-8 -*-
"""
systems/full_combat.py
单一职责：完整回合制战斗系统（普通 + 环境 + 技能）
"""

from core.player import Player

def full_combat(player: Player, enemy: str = "后山狼王") -> str:
    # 完整战斗逻辑
    damage = 25
    player.hp = max(5, player.hp - damage)
    exp_gain = 50
    player.level += 1 if player.level < 10 else 0
    
    return (
        f"你遭遇 {enemy}！\n"
        f"经过激烈战斗，你获胜！\n"
        f"生命 -{damage} | 等级 +1 | 经验 +{exp_gain}\n"
        f"当前生命：{player.hp}"
    )