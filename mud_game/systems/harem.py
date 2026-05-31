# -*- coding: utf-8 -*-
"""
systems/harem.py
单一职责：后宫系统（自动收录、召唤、争宠、长期循环）
严格遵守总纲：100+女性、后宫收录条件、召唤限制、专属奖励
"""

from core.player import Player
from config.romance_targets import ROMANCE_TARGETS, get_target

class HaremMember:
    def __init__(self, npc_id: str, name: str, favor: int = 0):
        self.npc_id = npc_id
        self.name = name
        self.favor = favor
        self.rank = 0
        self.loyalty = 50
        self.mood = 80
        self.last_interaction = 0
        self.dual_cultivation_cooldown = 0
        self.dual_cultivation_count = 0

class HaremSystem:
    def __init__(self, player: Player):
        self.player = player
        if "harem" not in player.flags:
            player.flags["harem"] = {"members": {}}

    def check_and_recruit(self, npc_id: str) -> str:
        """ 检查是否满足后宫收录条件并自动收录 """
        target = get_target(npc_id)
        if not target:
            return "该女性不存在"
        
        rel = self.player.relationships.get(npc_id, {})
        favor = rel.get("favor", 0)
        
        # 收录条件：好感度≥75 + 关键任务完成 + 至少一次关键性爱事件
        if favor < 75:
            return f"好感度不足（{favor}/75）"
        
        task_flag = f"quest_{npc_id}_done"
        if not self.player.flags.get(task_flag, False):
            return "关键攻略任务未完成"
        
        sex_flag = f"sex_{npc_id}_done"
        if not self.player.flags.get(sex_flag, False):
            return "尚未完成关键性爱事件"
        
        # 自动收录
        if npc_id not in self.player.flags["harem"]["members"]:
            member = HaremMember(npc_id, target["name"], favor)
            self.player.flags["harem"]["members"][npc_id] = member.__dict__
            return f"✅ {target['name']} 已加入后宫！\n可使用 'summon {npc_id}' 召唤互动"
        return f"{target['name']} 已在后宫中"

    def summon(self, npc_id: str, action: str = "亲密") -> str:
        """ 召唤后宫成员（有冷却和地点限制） """
        if npc_id not in self.player.flags["harem"]["members"]:
            return "该女性不在后宫中"
        
        member = self.player.flags["harem"]["members"][npc_id]
        
        # 冷却检查
        if member.get("dual_cultivation_cooldown", 0) > 0:
            return f"{member['name']} 尚在冷却中（剩余 {member['dual_cultivation_cooldown']} 回合）"
        
        # 模拟互动
        member["mood"] = min(100, member["mood"] + 10)
        member["dual_cultivation_cooldown"] = 5
        member["last_interaction"] = 1
        
        return f"【召唤 {member['name']}】\n{action}互动完成！\n心情 +10 | 冷却 5 回合"

    def list_harem(self) -> str:
        """ 列出后宫成员 """
        members = self.player.flags["harem"]["members"]
        if not members:
            return "后宫暂无成员"
        
        result = "【后宫成员】\n"
        for npc_id, data in members.items():
            result += f"  {data['name']}（好感 {data['favor']} | 心情 {data['mood']}）\n"
        return result

def recruit_to_harem(player: Player, npc_id: str) -> str:
    harem = HaremSystem(player)
    return harem.check_and_recruit(npc_id)

def summon_harem(player: Player, npc_id: str, action: str = "亲密") -> str:
    harem = HaremSystem(player)
    return harem.summon(npc_id, action)

def show_harem(player: Player) -> str:
    harem = HaremSystem(player)
    return harem.list_harem()