# -*- coding: utf-8 -*-
"""
config/romance_targets.py
单一职责：可攻略女性配置文件（绝世美女版）
每个女性包含完整设定：名字、身份、性格、性宖、敏感带、对话/吐吟/高潮模板
严格遵守总纲：18-36岁、极品身材、绝色容貌、好听名字
"""

ROMANCE_TARGETS = {
    "qingmei": {
        "id": "qingmei",
        "name": "柳清萝",
        "age": 18,
        "identity": "清水镇世家千金 / 你的青梅竹马",
        "relationship": "儿时玩伴，从小一起长大，对你有特殊感情",
        "personality": "温柔体贴、纯情害羞、偶尔会吃醋",
        "description": "柳清萝是清水镇最美的女子之一，肌肤胜雪，眼若秋水。自幼与你指腹为婚，性格温柔如水，却对你的任何风流事都吃醋。",
        "initial_favor": 45,
        "romance_quests": ["main_qingshui_01", "side_qingmei_01", "side_qingmei_02"],
        "sex_trigger": {
            "min_favor": 75,
            "required_quest": "side_qingmei_02",
            "min_lust": 45
        },
        "sensitive_zones": ["耳垂", "后颈", "大腿内侧", "脚心"],
        "kinks": ["温柔主导", "耳语轻哄", "纯爱慢节奏", "事后拥抱"],
        "dialogue_templates": {
            "default": "清萝轻声呫喻：『……你又来了呢』",
            "flirt": "清萝脸颊微红：『别……别这样看着我……』",
            "intimate": "清萝声音发颤：『今晚……不要走好吗？』"
        },
        "moan_templates": [
            "嗯……啊……",
            "轻……轻一点……",
            "好害羞……不要……",
            "啊……清萝要……要融化了……"
        ],
        "climax_templates": [
            "清萝全身发抖，紧紧抱住你，声音带着哭腔：『……要去了……要去了……！』",
            "清萝眼睛失焦，身体弓起，发出压抑却甜美的呜啮。"
        ],
        "exclusive_flags": ["qingmei_first_kiss", "qingmei_night_talk", "qingmei_jealous"]
    },
    
    "shaofu": {
        "id": "shaofu",
        "name": "沈婉玉",
        "age": 29,
        "identity": "隔壁人妻 / 茶楼老板娘",
        "relationship": "丈夫长期在外经商，寂寞已久，对你这个年轻人充满好奇与渴望",
        "personality": "成熟风韵、略带忧郁、偶尔强势、床上热情主动",
        "description": "沈婉玉是镇上公认的美人，腰胱盈盈一握，眼神勾人。丈夫常年不在，她独守空闺，对你的关心逐渐变成暧昧。",
        "initial_favor": 30,
        "romance_quests": ["side_shaofu_01", "side_shaofu_02", "side_shaofu_03"],
        "sex_trigger": {
            "min_favor": 80,
            "required_quest": "side_shaofu_03",
            "min_lust": 55
        },
        "sensitive_zones": ["腰窝", "胸口", "后颈", "大腿根部"],
        "kinks": ["成熟调教", "轻度SM", "酒后乱性", "事后烟"],
        "dialogue_templates": {
            "default": "婉玉轻叹：『小兄弟……你又来找我了』",
            "flirt": "婉玉眼神迷离：『今晚……要陪姐姐喝酒吗？』",
            "intimate": "婉玉声音低哒：『进来吧……门没锁』"
        },
        "moan_templates": [
            "啊……嗯……",
            "好深……要坏掉了……",
            "轻一点……婉玉受不了了……",
            "啊……要被你弄坏了……！"
        ],
        "climax_templates": [
            "沈婉玉身体剧烈颤斗，紧紧夹住你，声音带着哭腔：『要去了……要去了……！』",
            "婉玉眼睛翻白，身体弓起，发出压抑却甜美的长吟。"
        ],
        "exclusive_flags": ["shaofu_wine_night", "shaofu_secret", "shaofu_jealous"]
    },
    
    "xiaoxian": {
        "id": "xiaoxian",
        "name": "苏晚晴",
        "age": 21,
        "identity": "药铺仙子 / 医术高明却性格清冷",
        "relationship": "药铺掌柜之女，对你的频繁来访从厌烦到逐渐动心",
        "personality": "清冷高傲、外冷内热、医者仁心、床上意外敏感被动",
        "description": "苏晚晴是镇上最美的女子之一，气质清冷如仙，医术冠绝一方。起初对你这个「野小子」不屑一顾，却在一次次治疗中逐渐沦陷。",
        "initial_favor": 28,
        "romance_quests": ["side_xiaoxian_01", "side_xiaoxian_02"],
        "sex_trigger": {
            "min_favor": 70,
            "required_quest": "side_xiaoxian_02",
            "min_lust": 40
        },
        "sensitive_zones": ["手腕", "锁骨", "耳后", "脚脝"],
        "kinks": ["医疗play", "温柔被动", "轻度束缚", "事后依傠"],
        "dialogue_templates": {
            "default": "晚晴冷声：『……又来买药？』",
            "flirt": "晚晴耳根发红：『别……别碰我……』",
            "intimate": "晚晴声音发颤：『今晚……留下来吧……』"
        },
        "moan_templates": [
            "嗯……啊……",
            "好奇怪……不要……",
            "轻一点……晚晴……晚晴要融化了……",
            "啊……不要……要坏掉了……"
        ],
        "climax_templates": [
            "苏晚晴身体剧烈抽掻，紧紧抱住你，声音带着哭腔：『要去了……要去了……！』",
            "晚晴眼睛失焦，身体弓起，发出压抑却甜美的呜啮。"
        ],
        "exclusive_flags": ["xiaoxian_danfang", "xiaoxian_night_study", "xiaoxian_jealous"]
    },

    "miaoyin": {
        "id": "miaoyin",
        "name": "许妙音",
        "age": 24,
        "identity": "药铺女管事 / 被药商追求的清秀女子",
        "relationship": "负责药铺日常经营，对你这个常客从客气到暗生情懑",
        "personality": "精明能干、外柔内刚、略带书卷气、床上意外主动",
        "description": "许妙音是药铺的实际管理者，容貌清秀脱俗，腰胱纠细，手指修长。虽被富商追求，却对你这个「小兄弟」越来越在意。",
        "initial_favor": 35,
        "romance_quests": ["side_miaoyin_01", "side_miaoyin_02", "side_miaoyin_03"],
        "sex_trigger": {
            "min_favor": 78,
            "required_quest": "side_miaoyin_03",
            "min_lust": 48
        },
        "sensitive_zones": ["指尖", "耳后", "腰侧", "膝弯"],
        "kinks": ["轻度调教", "药香play", "主动骑乘", "事后轻吻"],
        "dialogue_templates": {
            "default": "妙音柔声：『又来采药了？这次要什么？』",
            "flirt": "妙音脸颊微红：『别……别靠这么近……』",
            "intimate": "妙音声音发软：『今晚……药铺关门后……』"
        },
        "moan_templates": [
            "嗯……啊……",
            "好舒服……不要停……",
            "妙音……妙音要……",
            "啊……被你弄得……好奇怪……"
        ],
        "climax_templates": [
            "许妙音身体突然绷紧，紧紧抱住你，声音带着哭腔：『要去了……妙音要去了……！』",
            "妙音眼睛湿润，身体轻轻颤斗，发出压抑却甜美的长叹。"
        ],
        "exclusive_flags": ["miaoyin_drug_night", "miaoyin_jealous", "miaoyin_secret"]
    },

    "waner": {
        "id": "waner",
        "name": "秦婉儿",
        "age": 19,
        "identity": "女猎户 / 山林中的野性少女",
        "relationship": "常年在后山打猎，对你这个「镇上来的小子」从挑衅到逐渐倾心",
        "personality": "野性直率、略带傲娇、身体结实、床上热情主动",
        "description": "秦婉儿是后山猎户之女，皮肤小麦色，腰胱有力，胸膝挺拔。性格像山里的野猫，起初对你充满敌意，却在一次次共同猎猎中逐渐沦陷。",
        "initial_favor": 22,
        "romance_quests": ["side_waner_01", "side_waner_02"],
        "sex_trigger": {
            "min_favor": 72,
            "required_quest": "side_waner_02",
            "min_lust": 50
        },
        "sensitive_zones": ["大腿内侧", "腰窝", "胸口", "后背"],
        "kinks": ["野外play", "轻度束缚", "主动骑乘", "事后拥抱"],
        "dialogue_templates": {
            "default": "婉儿冷哼：『哼……又来后山？小心被狼咬』",
            "flirt": "婉儿脸红转头：『别……别用那种眼神看我……』",
            "intimate": "婉儿声音发颤：『今晚……别走……』"
        },
        "moan_templates": [
            "啊……嗯……",
            "好深……婉儿受不了了……",
            "轻一点……好舒服……",
            "啊……要……要飞起来了……"
        ],
        "climax_templates": [
            "秦婉儿身体剧烈颤斗，紧紧夹住你，声音带着哭腔：『要去了……婉儿要去了……！』",
            "婉儿眼睛失焦，身体弓起，发出压抑却甜美的呜啮。"
        ],
        "exclusive_flags": ["waner_hunt_night", "waner_jealous", "waner_wild"]
    }
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