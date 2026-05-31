# -*- coding: utf-8 -*-
"""
config/romance/qingmei.py
单一职责：柳清萝（青梅竹马）完整配置
"""

QINGMEI = {
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
}