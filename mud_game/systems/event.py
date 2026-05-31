# -*- coding: utf-8 -*-
"""
systems/event.py
单一职责：随机事件系统（夜晚事件、突发剧情）
"""

from core.player import Player
import random

def trigger_random_event(player: Player) -> str:
    events = [
        "夜晚突然下起大雨，你在街边避雨时遇到一位祖师。",
        "后山传来狼嗚声，附近居民请求你帮忙驱赶野兽。",
        "药铺新到一批罕见药材，老郎中邀请你帮忙鉴定。",
        "柳清萝在河边等你，脸上带着罕见的笑容。"
    ]
    event = random.choice(events)
    player.gold += 5
    return f"【随机事件】{event}\n获得铜钱 +5"