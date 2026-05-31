# -*- coding: utf-8 -*-
"""
config/romance/miaoyin.py
单一职责：许妙音（药铺女管事）完整配置
"""

MIAOYIN = {
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
}