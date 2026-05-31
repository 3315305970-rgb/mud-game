# -*- coding: utf-8 -*-
"""
config/romance_targets.py
单一职责：聚合所有可攻略女性配置（从 romance/ 子目录导入）
每个NPC独立一个文件，严格遵守单一职责 + 高颗粒度原则
"""

from .romance.qingmei import QINGMEI
from .romance.shaofu import SHAOFU
from .romance.xiaoxian import XIAOXIAN
from .romance.miaoyin import MIAOYIN
from .romance.waner import WANER

ROMANCE_TARGETS = {
    "qingmei": QINGMEI,
    "shaofu": SHAOFU,
    "xiaoxian": XIAOXIAN,
    "miaoyin": MIAOYIN,
    "waner": WANER,
}

def get_target(npc_id: str):
    """ 获取指定女性的完整配置 """
    return ROMANCE_TARGETS.get(npc_id.lower())

def check_sex_available(player, npc_id: str) -> tuple[bool, str]:
    """ 检查是否可以触发性爱（好感度 + 任务 + 性欲） """
    target = get_target(npc_id)
    if not target:
        return False, "该女性不存在"
    
    rel = player.relationships.get(npc_id, {})
    favor = rel.get("favor", 0)
    
    if favor < target["sex_trigger"]["min_favor"]:
        return False, f"好感度不足（当前 {favor}/{target['sex_trigger']['min_favor']}）"
    
    if target["sex_trigger"]["required_quest"] not in player.flags:
        return False, "相关攻略任务未完成"
    
    if player.lust < target["sex_trigger"]["min_lust"]:
        return False, f"性欲不足（当前 {player.lust}/{target['sex_trigger']['min_lust']}）"
    
    return True, "可以触发性爱事件"

def get_all_targets() -> list:
    """ 获取所有可攻略女性列表（用于后宫等系统） """
    return list(ROMANCE_TARGETS.keys())