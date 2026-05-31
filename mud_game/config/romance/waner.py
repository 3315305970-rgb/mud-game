# -*- coding: utf-8 -*-
"""
config/romance/waner.py
单一职责：秦婉儿（女猎户）完整配置
"""

WANER = {
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