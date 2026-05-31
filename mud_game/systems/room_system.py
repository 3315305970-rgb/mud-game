# -*- coding: utf-8 -*-
"""
systems/room_system.py
单一职责：房间查看、移动、描述生成
"""

from core.player import Player

# 假设导入

def look(player):
    # 简化实现
    return f"你在 {player.location}。"

def move(player, direction):
    # 简化实现
    player.move_to("qingshui_street")
    return f"你向{direction}移动。"