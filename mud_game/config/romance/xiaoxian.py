# -*- coding: utf-8 -*-
"""
config/romance/xiaoxian.py
单一职责：苏晚晴（药铺仙子）完整配置
"""

XIAOXIAN = {
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
        "苏晚晴身体剧烈拜掻，紧紧抱住你，声音带着哭腔：『要去了……要去了……！』",
        "晚晴眼睛失焦，身体弓起，发出压抑却甜美的呜啮。"
    ],
    "exclusive_flags": ["xiaoxian_danfang", "xiaoxian_night_study", "xiaoxian_jealous"]
}