# -*- coding: utf-8 -*-
"""
systems/sex_system.py
单一职责：性爱系统框架（独立于普通RPG属性）
严格遵守：攻略任务 + 好感度达标后才能成功做爱
"""

from core.player import Player

class SexState:
    def __init__(self):
        self.lust = 0          # 性欲值（0-100）
        self.corruption = 0    # 堕落度
        self.experience = 0    # 性爱经验

def start_sex_event(player: Player, npc_name: str = "青梅竹马") -> str:
    """
    性爱触发条件：
    1. 好感度 >= 70
    2. 相关攻略任务已完成（player.flags 中有标记）
    3. 性欲 >= 40
    """
    rel = player.relationships.get(npc_name.lower().replace(" ", "_"), {})
    favor = rel.get("favor", 0)
    
    # 检查好感度
    if favor < 70:
        return f"{npc_name}：『我们还不够亲密……（好感度 {favor}/70）』"
    
    # 检查任务完成（示例：青梅竹马任务）
    task_flag = f"quest_{npc_name.lower().replace(' ', '_')}_done"
    if not player.flags.get(task_flag, False):
        return f"{npc_name}：『我们之间还有未完成的心结……』"
    
    # 检查性欲
    if player.lust < 40:
        return f"{npc_name}：『现在气氛不对……（性欲 {player.lust}/40）』"
    
    # 成功触发
    player.lust = max(0, player.lust - 50)
    player.change_favor(npc_name.lower().replace(" ", "_"), 15)
    
    return (
        f"✅ 与 {npc_name} 成功进入亲密互动！\n"
        "【固定流程】钺垫 → 调情 → 挑逗 → 插入 → 高潮 → 事后\n"
        "性欲 -50 | 好感 +15 | 关系更进一步"
    )