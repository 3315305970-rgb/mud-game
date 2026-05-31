# -*- coding: utf-8 -*-
"""
config/romance/shaofu.py
单一职责：沈婉玉（隔壁人妻）完整配置
"""

SHAOFU = {
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
}