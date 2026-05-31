# -*- coding: utf-8 -*-
"""
systems/sex_system.py
单一职责：性爱系统框架（独立于普通RPG属性）
严格遵守固定流程 + 独立属性
"""

from core.player import Player

class SexState:
    def __init__(self):
        self.lust = 0          # 性欲值（0-100）
        self.corruption = 0    # 堕落度
        self.experience = 0    # 性爱经验

def start_sex_event(player: Player, npc_name: str) -> str:
    # 简化固定流程
    if player.lust < 30:
        return f"{npc_name}：『现在还不是时候……』"
    
    player.lust = max(0, player.lust - 40)
    return (
        f"与 {npc_name} 进入亲密互动……\n"
        "【固定流程】钺垫 → 调情 → 挑逗 → 插入 → 高潮 → 事后\n"
        "性欲 -40 | 好感提升"
    )