# -*- coding: utf-8 -*-
"""
systems/command_handler.py
单一职责：命令解析 + 路由分发（不包含具体业务逻辑）
"""

from core.player import Player

from .cultivation import cultivate
from .quest import QuestManager


def handle_command(player: Player, command: str, args: str = "") -> str:
    cmd = command.lower().strip()
    
    if cmd in ["look", "l", "查看"]:
        from .room_system import look
        return look(player)
    elif cmd in ["go", "移动", "走"]:
        from .room_system import move
        return move(player, args)
    elif cmd in ["xiulian", "修炼"]:
        return cultivate(player)
    elif cmd in ["quest", "任务"]:
        qm = QuestManager(player)
        return qm.list_quests()
    elif cmd in ["accept", "接受任务"]:
        qm = QuestManager(player)
        return qm.start_quest(args)
    elif cmd in ["inventory", "i", "背包"]:
        from .inventory import show_inventory
        return show_inventory(player)
    elif cmd in ["fight", "战斗"]:
        from .combat import start_combat
        return start_combat(player)
    elif cmd in ["alchemy", "炼药"]:
        from .alchemy import refine_pill
        return refine_pill(player, args)
    elif cmd in ["forge", "打造"]:
        from .crafting import forge_equipment
        return forge_equipment(player, args)
    elif cmd in ["sex", "亲密"]:
        from .sex_system import start_sex_event
        return start_sex_event(player, args or "青梅竹马")
    elif cmd in ["catch", "抓宠"]:
        from .pet import catch_pet
        return catch_pet(player, args or "小狐妖")
    elif cmd in ["book", "打书"]:
        from .pet import book_pet
        return book_pet(player, args or "魅惑")
    elif cmd in ["fullfight", "完整战斗"]:
        from .full_combat import full_combat
        return full_combat(player, args or "后山狼王")
    elif cmd in ["train", "训练"]:
        from .building import train_at_wuguan
        return train_at_wuguan(player)
    elif cmd in ["rest", "休息"]:
        from .building import rest_at_inn
        return rest_at_inn(player)
    elif cmd in ["event", "随机事件"]:
        from .event import trigger_random_event
        return trigger_random_event(player)
    elif cmd in ["skill", "技能"]:
        from .skill import learn_skill
        return learn_skill(player, args or "基础拳法")
    elif cmd in ["title", "称号"]:
        from .title import show_titles
        return show_titles(player)
    elif cmd in ["buff", "状态"]:
        from .buff import apply_buff
        return apply_buff(player, args or "力量提升")
    elif cmd in ["harem", "后宫"]:
        from .harem import show_harem
        return show_harem(player)
    elif cmd in ["recruit", "收录"]:
        from .harem import recruit_to_harem
        return recruit_to_harem(player, args or "qingmei")
    elif cmd in ["summon", "召唤"]:
        from .harem import summon_harem
        parts = args.split() if args else ["qingmei", "亲密"]
        return summon_harem(player, parts[0], " ".join(parts[1:]) if len(parts) > 1 else "亲密")
    elif cmd in ["help", "帮助"]:
        return get_help_text()
    else:
        return "未知命令。输入 'help' 查看可用命令。"

def get_help_text():
    return (
        "【可用命令】\n"
        "look/l/查看 - 查看当前位置\n"
        "go <方向> - 移动\n"
        "xiulian/修炼 - 修炼提升\n"
        "inventory/i/背包 - 查看背包\n"
        "fight/战斗 - 普通战斗\n"
        "fullfight/完整战斗 - 完整战斗\n"
        "alchemy/炼药 - 炼制丹药\n"
        "forge/打造 - 打造装备\n"
        "sex/亲密 - 性爱互动（需好感度≥70 + 任务完成 + 性欲≥40）\n"
        "catch/抓宠 - 捕捉灵宠\n"
        "book/打书 - 宠物打书\n"
        "train/训练 - 武馆训练\n"
        "rest/休息 - 客栈休息\n"
        "event/随机事件 - 触发随机事件\n"
        "skill/技能 - 学习技能\n"
        "title/称号 - 查看称号\n"
        "buff/状态 - 获得状态效果\n"
        "harem/后宫 - 查看后宫成员\n"
        "recruit/收录 <ID> - 尝试收录女性进后宫\n"
        "summon/召唤 <ID> [动作] - 召唤后宫成员互动\n"
        "quest/任务 - 查看任务\n"
        "accept <ID> - 接受任务\n"
        "help - 此帮助\n\n"
        "单机模式：所有社交均通过NPC对话进行。"
    )