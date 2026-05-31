# -*- coding: utf-8 -*-
"""命令系统 - 凡人界 MUD
"""

from rooms import ROOMS, ITEMS, NPCS
from quest import QuestManager

def handle_command(player, command, args=""):
    cmd = command.lower().strip()
    qm = QuestManager(player)
    
    if cmd in ["look", "l", "查看"]:
        return look(player)
    elif cmd in ["go", "移动", "走"]:
        resp = move(player, args)
        # 检查任务进度
        progress = qm.check_progress(f"go {args}")
        return resp + ("\n" + progress if progress else "")
    elif cmd in ["inventory", "i", "背包", "物品"]:
        return show_inventory(player)
    elif cmd in ["status", "状态", "我"]:
        return player.get_status()
    elif cmd in ["talk", "对话", "说"]:
        resp = talk(player, args)
        progress = qm.check_progress(f"talk {args}")
        return resp + ("\n" + progress if progress else "")
    elif cmd in ["buy", "购买"]:
        resp = buy(player, args)
        progress = qm.check_progress(f"buy {args}")
        return resp + ("\n" + progress if progress else "")
    elif cmd in ["sell", "出售"]:
        return sell(player, args)
    elif cmd in ["dig", "挖宝"]:
        return dig(player)
    elif cmd in ["quest", "任务", "任务列表"]:
        return qm.list_quests()
    elif cmd in ["accept", "接受任务"]:
        return qm.start_quest(args)
    elif cmd in ["help", "帮助", "菜单"]:
        return show_help()
    else:
        return "未知命令。输入 'help' 查看可用命令。"

def look(player):
    room = ROOMS.get(player.location)
    if not room:
        return "当前位置不存在！"
    
    desc = f"【{room['name']}】\n{room['description']}\n"
    
    # 出口
    exits = ", ".join([f"{k}({v})" for k, v in room["exits"].items()])
    desc += f"\n出口：{exits}\n"
    
    # 物品
    if room["items"]:
        item_names = [ITEMS.get(iid, {}).get("name", iid) for iid in room["items"]]
        desc += f"可见物品：{', '.join(item_names)}\n"
    
    # NPC
    if room["npcs"]:
        npc_names = [NPCS.get(nid, {}).get("name", nid) for nid in room["npcs"]]
        desc += f"这里有：{', '.join(npc_names)}\n"
    
    # 商店
    if room.get("shop"):
        desc += f"\n【{room['shop']['name']}】可购买物品：\n"
        for item in room["shop"]["items"]:
            desc += f"  {item['name']} - {item['price']}铜钱\n"
    
    return desc

def move(player, direction):
    room = ROOMS.get(player.location)
    if not room:
        return "错误位置！"
    
    exits = room["exits"]
    if direction in exits:
        new_loc = exits[direction]
        player.location = new_loc
        return f"你向{direction}移动，来到 {ROOMS[new_loc]['name']}。"
    else:
        return f"没有通往 {direction} 的路。"

def show_inventory(player):
    if not player.inventory:
        return "你的背包空空如也。"
    inv = "【背包】\n"
    for iid, count in player.inventory.items():
        name = ITEMS.get(iid, {}).get("name", iid)
        inv += f"  {name} x{count}\n"
    return inv

def talk(player, target):
    room = ROOMS.get(player.location)
    if not room or not room["npcs"]:
        return "这里没有人可以对话。"
    
    # 简单匹配第一个NPC
    npc_id = room["npcs"][0]
    npc = NPCS.get(npc_id)
    if not npc:
        return "对话对象不存在。"
    
    # 检查关系
    rel = player.relationships.get(npc_id, {})
    if rel.get("type") == "qingmei_bamboo_horse":
        return npc["dialogue"].get("default", "青梅对你微笑了一下。")
    elif rel.get("type") == "married_neighbor":
        return npc["dialogue"].get("default", "少妇看了你一眼。")
    else:
        return npc["dialogue"].get("default", f"{npc['name']}：『你好。』")

def buy(player, item_name):
    room = ROOMS.get(player.location)
    if not room or not room.get("shop"):
        return "这里没有商店。"
    
    shop = room["shop"]
    for item in shop["items"]:
        if item["name"] == item_name or item["id"] == item_name:
            if player.gold >= item["price"]:
                player.gold -= item["price"]
                player.add_item(item["id"])
                return f"你购买了 {item['name']}。"
            else:
                return "铜钱不足！"
    return "没有这个物品。"

def sell(player, item_name):
    # 简化：只卖资源类
    for iid, count in list(player.inventory.items()):
        if ITEMS.get(iid, {}).get("name") == item_name:
            price = 2  # 基础售价
            player.gold += price * count
            player.remove_item(iid, count)
            return f"你出售了 {item_name}，获得 {price * count} 铜钱。"
    return "你没有这个物品。"

def dig(player):
    # 简化挖宝：需要藏宝图
    if player.has_item("treasure_map"):
        player.remove_item("treasure_map")
        player.add_item("iron_ore", 3)
        player.gold += 20
        return "你挖到了宝藏！获得铁矿石x3 和 20铜钱。"
    return "需要藏宝图才能挖宝。"

def show_help():
    return (
        "【可用命令】\n"
        "look/l/查看 - 查看当前位置\n"
        "go <方向> - 移动 (东/西/南/北)\n"
        "inventory/i/背包 - 查看背包\n"
        "status/状态 - 查看人物状态\n"
        "talk <目标> - 与NPC对话\n"
        "buy <物品> - 购买物品\n"
        "sell <物品> - 出售物品\n"
        "dig - 挖宝 (需藏宝图)\n"
        "quest/任务 - 查看进行中任务\n"
        "accept <任务ID> - 接受任务\n"
        "help - 显示此帮助"
    )