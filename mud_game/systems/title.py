# -*- coding: utf-8 -*-
"""
systems/title.py
单一职责：称号系统（成就 + 特殊效果）
"""

from core.player import Player

def earn_title(player: Player, title: str) -> str:
    if "titles" not in player.flags:
        player.flags["titles"] = []
    if title not in player.flags["titles"]:
        player.flags["titles"].append(title)
        return f"获得称号：【{title}】！"
    return "已拥有该称号。"

def show_titles(player: Player) -> str:
    titles = player.flags.get("titles", [])
    if not titles:
        return "你还没有获得任何称号。"
    return "【称号】\n" + "\n".join([f"  【{t}】" for t in titles])