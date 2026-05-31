# -*- coding: utf-8 -*-
"""
core/room.py
单一职责：房间类定义 + 静态房间数据加载
"""

class Room:
    def __init__(self, room_id, name, description, exits, items=None, npcs=None, shop=None, building_type="normal"):
        self.id = room_id
        self.name = name
        self.description = description
        self.exits = exits or {}
        self.items = items or []
        self.npcs = npcs or []
        self.shop = shop
        self.building_type = building_type

# 静态房间数据（从原 rooms.py 迁移，保持不变）
STATIC_ROOMS = {
    "qingshui_town_start": {
        "id": "qingshui_town_start",
        "name": "主角小院",
        "description": "你醒来时躺在一间简陋的民居小院里。院子里有口水井，几株竹子在微风中摇曰。东南方向是镇子中心，西北通往后山小路。这里是你的起点，也是避风港。作为穿越者，你对这个世界的一切都感到陌生，但身体却本能地知道如何行动。",
        "exits": {"东": "qingshui_street", "北": "qingshui_backyard", "南": "qingshui_river"},
        "items": ["well", "bamboo"],
        "npcs": [],
        "shop": None,
        "building_type": "safe"
    },
    # ... (其他房间保持不变，实际应完整迁移)
}

def load_room(room_id):
    data = STATIC_ROOMS.get(room_id)
    if not data:
        return None
    return Room(**data)