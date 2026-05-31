# -*- coding: utf-8 -*-
"""
systems/command_handler.py
单一职责：命令解析 + 路由分发（不包含具体业务逻辑）
"""

from core.player import Player

from .cultivation import cultivate
from .quest import QuestManager


def handle_command(player: Player, command: str, args: str = "") -> str:
    cmd = command.lower().strip()
    
    if cmd in ["look", "l", "查看"]:
        from .room_system import look
        return look(player)
    elif cmd in ["go", "移动", "走"]:
        from .room_system import move
        return move(player, args)
    elif cmd in ["xiulian", "修炼"]:
        return cultivate(player)
    elif cmd in ["quest", "任务"]:
        qm = QuestManager(player)
        return qm.list_quests()
    elif cmd in ["accept", "接受任务"]:
        qm = QuestManager(player)
        return qm.start_quest(args)
    elif cmd in ["inventory", "i", "背包"]:
        from .inventory import show_inventory
        return show_inventory(player)
    elif cmd in ["fight", "战斗"]:
        from .combat import start_combat
        return start_combat(player)
    elif cmd in ["help", "帮助"]:
        return get_help_text()
    else:
        return "未知命令。输入 'help' 查看可用命令。"

def get_help_text():
    return (
        "【可用命令】\n"
        "look/l/查看 - 查看当前位置\n"
        "go <方向> - 移动\n"
        "xiulian/修炼 - 修炼提升\n"
        "inventory/i/背包 - 查看背包\n"
        "fight/战斗 - 普通战斗\n"
        "quest/任务 - 查看任务\n"
        "accept <ID> - 接受任务\n"
        "help - 此帮助\n\n"
        "单机模式：所有社交均通过NPC对话进行。"
    )