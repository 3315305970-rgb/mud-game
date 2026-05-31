# -*- coding: utf-8 -*-
"""
systems/economy.py
单一职责：经济系统（金钱、交易、拍卖基础）
"""

from core.player import Player

def earn_money(player: Player, amount: int, reason: str = "任务奖励") -> str:
    player.gold += amount
    return f"获得铜钱 +{amount}（{reason}）"

def spend_money(player: Player, amount: int, reason: str = "购买物品") -> bool:
    if player.gold >= amount:
        player.gold -= amount
        return True
    return False

def show_wealth(player: Player) -> str:
    return f"当前铜钱：{player.gold}"