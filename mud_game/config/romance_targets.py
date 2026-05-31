# -*- coding: utf-8 -*-
"""
config/romance_targets.py
单一职责：可攻略女性配置文件
每个女性包含：基本信息、攻略条件、性爱触发、专属设定
"""

ROMANCE_TARGETS = {
    "qingmei": {
        "id": "qingmei",
        "name": "青梅竹马",
        "age": 18,
        "description": "儿时玩伴，温柔体贴，对你有特殊感情。从小一起长大，是你在这个世界最亲近的人。",
        "initial_favor": 40,
        "romance_quests": ["main_qingshui_01", "side_qingmei_01"],
        "sex_trigger": {
            "min_favor": 70,
            "required_quest": "side_qingmei_01",
            "min_lust": 40
        },
        "sensitive_zones": ["耳垂", "颈部", "大腿内侧"],
        "kinks": ["温柔主导", "耳语"],
        "exclusive_flags": ["qingmei_first_kiss", "qingmei_night_talk"]
    },
    
    "shaofu": {
        "id": "shaofu",
        "name": "隔壁少妇",
        "age": 28,
        "description": "成熟美妇，丈夫长期外出，生活压力大。成熟风韵，对年轻人的关心充满好奇。",
        "initial_favor": 25,
        "romance_quests": ["side_shaofu_01", "side_shaofu_02"],
        "sex_trigger": {
            "min_favor": 75,
            "required_quest": "side_shaofu_02",
            "min_lust": 50
        },
        "sensitive_zones": ["腰部", "胸部", "后颈"],
        "kinks": ["成熟调教", "轻SM"],
        "exclusive_flags": ["shaofu_wine_night", "shaofu_secret"]
    },
    
    "xiaoxian": {
        "id": "xiaoxian",
        "name": "药铺小仙",
        "age": 20,
        "description": "药铺掌柜的女儿，医术高明但性格害羞。对你的频繁来访逐渐产生好感。",
        "initial_favor": 30,
        "romance_quests": ["side_xiaoxian_01"],
        "sex_trigger": {
            "min_favor": 65,
            "required_quest": "side_xiaoxian_01",
            "min_lust": 35
        },
        "sensitive_zones": ["手腕", "锁骨", "脚踝"],
        "kinks": ["医疗play", "温柔被动"],
        "exclusive_flags": ["xiaoxian_danfang", "xiaoxian_night_study"]
    }
}

def get_target(npc_id: str):
    """ 获取指定女性的配置 """
    return ROMANCE_TARGETS.get(npc_id.lower())

def check_sex_available(player, npc_id: str) -> tuple[bool, str]:
    """ 检查是否可以触发性爱 """
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