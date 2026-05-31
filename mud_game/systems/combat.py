# -*- coding: utf-8 -*-
"""
systems/combat.py
单一职责：普通回合制战斗系统（梦幻西游风格）
"""

from core.player import Player

def start_combat(player: Player, monster_name: str = "野狼") -> str:
    # 简化战斗逻辑
    player.hp = max(10, player.hp - 15)
    gold_gain = 10
    player.gold += gold_gain
    return (
        f"你与 {monster_name} 进入战斗！\n"
        f"经过一番激战，你胜利了！\n"
        f"生命 -15 | 获得铜钱 +{gold_gain}\n"
        f"当前生命：{player.hp}"
    )

def normal_attack(player: Player) -> str:
    return "你挥拳攻击，造成 10 点伤害！"