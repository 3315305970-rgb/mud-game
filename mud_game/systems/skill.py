# -*- coding: utf-8 -*-
"""
systems/skill.py
单一职责：技能树系统（普通技能 + 性爱技能）
"""

from core.player import Player

class Skill:
    def __init__(self, name, level=1, skill_type="normal"):
        self.name = name
        self.level = level
        self.type = skill_type

def learn_skill(player: Player, skill_name: str, skill_type: str = "normal") -> str:
    if skill_name not in player.flags.get("skills", []):
        if "skills" not in player.flags:
            player.flags["skills"] = []
        player.flags["skills"].append(skill_name)
        return f"学会技能：{skill_name}！"
    return "已经学会该技能。"

def use_skill(player: Player, skill_name: str) -> str:
    if skill_name in player.flags.get("skills", []):
        return f"使用 {skill_name}！效果触发。"
    return "未学会该技能。"