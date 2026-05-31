# -*- coding: utf-8 -*-
"""静态房间定义 - 凡人界 MUD
所有房间固定，不可动态生成
"""

ROOMS = {
    "qingshui_town_start": {
        "id": "qingshui_town_start",
        "name": "主角小院",
        "description": "你醒来时躺在一间简陋的民居小院里。院子里有口水井，几株竹子在微风中摇曰。东南方向是镇子中心，西北通往后山小路。这里是你的起点，也是避风港。",
        "exits": {"东": "qingshui_street", "北": "qingshui_backyard", "南": "qingshui_river"},
        "items": ["well", "bamboo"],
        "npcs": [],
        "shop": None,
        "building_type": "safe"
    },
    "qingshui_street": {
        "id": "qingshui_street",
        "name": "清水镇街",
        "description": "镇子主街，青石板路略显破旧。两旁有药铺、铁匠铺、杂货铺和武馆。街中心有块告示牌，上面贴着各种悬赏和告示。西边是你家小院，东边通往县城方向。",
        "exits": {"西": "qingshui_town_start", "东": "qingshui_east_gate", "北": "qingshui_wuguan", "南": "qingshui_yaopu"},
        "items": ["notice_board"],
        "npcs": ["town_crier"],
        "shop": None,
        "building_type": "street"
    },
    "qingshui_yaopu": {
        "id": "qingshui_yaopu",
        "name": "药铺",
        "description": "药铺里渲漫着草药香气。老郎中正忙着抓药，墙上挂满了各种药材和丹方。这里可以买到基础恢复药和草药种子。",
        "exits": {"北": "qingshui_street"},
        "items": ["herb_seed", "healing_pill_low"],
        "npcs": ["old_doctor"],
        "shop": {
            "name": "药铺",
            "items": [
                {"id": "healing_pill_low", "name": "低阶回血丹", "price": 10, "stock": 20},
                {"id": "herb_seed", "name": "草药种子", "price": 5, "stock": 50}
            ]
        },
        "building_type": "shop"
    },
    "qingshui_wuguan": {
        "id": "qingshui_wuguan",
        "name": "武馆",
        "description": "武馆内传出阵阵喓声和兵器碰撞声。馆主正指导弟子练习基础拳脚。这里可以学习基础武学和进行体魄训练。",
        "exits": {"南": "qingshui_street"},
        "items": [],
        "npcs": ["wuguan_master"],
        "shop": None,
        "building_type": "training"
    },
    "qingshui_river": {
        "id": "qingshui_river",
        "name": "河边竹林",
        "description": "清水河边竹林茂密，风吹过发出沙沙声。这里是青梅竹马常来玩耍的地方，也是采集竹笋和野果的好去处。远处可见后山轮廓。",
        "exits": {"北": "qingshui_town_start", "东": "qingshui_street"},
        "items": ["bamboo_shoot", "wild_fruit"],
        "npcs": ["qingmei"],
        "shop": None,
        "building_type": "wild"
    },
    "qingshui_neighbor": {
        "id": "qingshui_neighbor",
        "name": "隔壁院落",
        "description": "隔壁少妇的院子，院门虛掩着。院内有晞晒的衣服和菜地，空气中飘着饯菜香气。这里是早期可攻略女性之一的居所。",
        "exits": {"西": "qingshui_town_start"},
        "items": [],
        "npcs": ["shaofu"],
        "shop": None,
        "building_type": "npc_home"
    },
    "qingshui_backyard": {
        "id": "qingshui_backyard",
        "name": "后山小路入口",
        "description": "小路通往后山，路边长满野草和灌木。偶尔有野兔出没，是低阶玩家练手的好地方。继续深入可达后山洞穴。",
        "exits": {"南": "qingshui_town_start", "北": "qingshui_houshan"},
        "items": [],
        "npcs": [],
        "shop": None,
        "building_type": "wild"
    },
    "qingshui_houshan": {
        "id": "qingshui_houshan",
        "name": "后山",
        "description": "后山树木葱愈，山风阵阵。这里有低阶野兽出没（兔、狼、熊），也是采集药材和矿石的地方。山洞深处可能有隐藏秘密。",
        "exits": {"南": "qingshui_backyard"},
        "items": ["iron_ore", "herb_low"],
        "npcs": [],
        "shop": None,
        "building_type": "wild"
    }
}

# 物品定义
ITEMS = {
    "well": {"name": "水井", "desc": "一口古井，水清澈见底。", "type": "scenery"},
    "bamboo": {"name": "竹子", "desc": "青翠的竹子，可采集竹笋。", "type": "resource"},
    "notice_board": {"name": "告示牌", "desc": "镇子告示，上面有各种悬赏任务。", "type": "scenery"},
    "healing_pill_low": {"name": "低阶回血丹", "desc": "恢复少量生命值。", "type": "consumable", "effect": {"hp": 20}},
    "herb_seed": {"name": "草药种子", "desc": "可种植的草药种子。", "type": "seed"},
    "bamboo_shoot": {"name": "竹笋", "desc": "新鲜竹笋，可食用或出售。", "type": "resource"},
    "wild_fruit": {"name": "野果", "desc": "山间野果，甜美多汁。", "type": "consumable", "effect": {"hp": 5}},
    "iron_ore": {"name": "铁矿石", "desc": "粗糙的铁矿，可用于打造。", "type": "resource"},
    "herb_low": {"name": "低阶草药", "desc": "常见的药材。", "type": "resource"},
    "treasure_map": {"name": "藏宝图", "desc": "古老的藏宝图，标着后山某处宝藏。", "type": "quest"}
}

# NPC定义（基础）
NPCS = {
    "qingmei": {
        "name": "青梅竹马",
        "desc": "儿时玩伴，温柔体贴，对你有特殊感情。",
        "dialogue": {
            "default": "青梅微笑一笑：『又来找我玩了吗？』",
            "quest": "青梅：『后山最近有野狼出没，你要小心...』"
        },
        "relationship": "qingmei_bamboo_horse"
    },
    "shaofu": {
        "name": "隔壁少妇",
        "desc": "成熟美妇，丈夫长期外出，生活压力大。",
        "dialogue": {
            "default": "少妇叹息：『日子不好过啊...』",
            "flirt": "少妇脸红：『你这孩子...』"
        },
        "relationship": "married_neighbor"
    },
    "old_doctor": {
        "name": "老郎中",
        "desc": "药铺掌柜，医术高明。",
        "dialogue": {"default": "老郎中：『需要什么药？』"}
    },
    "wuguan_master": {
        "name": "武馆馆主",
        "desc": " retired武者，善长基础拳脚。",
        "dialogue": {"default": "馆主：『想练武吗？先从扎马步开始！』"}
    }
}