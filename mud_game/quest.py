# -*- coding: utf-8 -*-
"""任务系统（基建版）- 凡人界 MUD
支持主线/支线、关系身份触发、静态任务
"""

QUESTS = {
    "main_qingshui_01": {
        "id": "main_qingshui_01",
        "name": "初入凡人界",
        "type": "main",
        "description": "在清水镇安顿下来，了解周围环境。",
        "steps": [
            {"id": "step1", "desc": "与青梅竹马对话", "target": "talk qingmei", "done": False},
            {"id": "step2", "desc": "去药铺购买低阶回血丹", "target": "buy 低阶回血丹", "done": False},
            {"id": "step3", "desc": "探索后山入口", "target": "go 北", "done": False}
        ],
        "reward": {"gold": 50, "exp": 100, "item": "treasure_map"},
        "next": "main_qingshui_02"
    },
    "side_shaofu_01": {
        "id": "side_shaofu_01",
        "name": "邻里互助",
        "type": "side",
        "description": "帮助隔壁少妇解决小麻烦。",
        "steps": [
            {"id": "step1", "desc": "与隔壁少妇对话", "target": "talk shaofu", "done": False},
            {"id": "step2", "desc": "从后山采集野果给她", "target": "give wild_fruit", "done": False}
        ],
        "reward": {"gold": 20, "favor": {"shaofu": 15}},
        "next": None
    }
}

class QuestManager:
    def __init__(self, player):
        self.player = player
        self.active_quests = player.flags.get("active_quests", {})
    
    def start_quest(self, quest_id):
        if quest_id not in QUESTS:
            return "任务不存在。"
        if quest_id in self.active_quests:
            return "你已经在做这个任务了。"
        self.active_quests[quest_id] = {"progress": 0, "steps_done": []}
        self.player.flags["active_quests"] = self.active_quests
        return f"接受任务：{QUESTS[quest_id]['name']}"
    
    def check_progress(self, command):
        updated = []
        for qid, progress in list(self.active_quests.items()):
            quest = QUESTS.get(qid)
            if not quest:
                continue
            step_idx = progress["progress"]
            if step_idx >= len(quest["steps"]):
                continue
            current_step = quest["steps"][step_idx]
            if command.lower() in current_step["target"].lower():
                progress["steps_done"].append(current_step["id"])
                progress["progress"] += 1
                updated.append(f"✓ {current_step['desc']}")
                if progress["progress"] >= len(quest["steps"]):
                    self.complete_quest(qid)
        return "\n".join(updated) if updated else ""
    
    def complete_quest(self, quest_id):
        quest = QUESTS[quest_id]
        # 发放奖励
        self.player.gold += quest["reward"].get("gold", 0)
        if "favor" in quest["reward"]:
            for npc, delta in quest["reward"]["favor"].items():
                self.player.change_favor(npc, delta)
        if "item" in quest["reward"]:
            self.player.add_item(quest["reward"]["item"])
        
        del self.active_quests[quest_id]
        next_q = quest.get("next")
        if next_q:
            self.start_quest(next_q)
        return f"任务完成：{quest['name']}！获得奖励。"

    def list_quests(self):
        if not self.active_quests:
            return "你当前没有进行中的任务。"
        result = "【进行中任务】\n"
        for qid in self.active_quests:
            q = QUESTS[qid]
            result += f"- {q['name']} ({q['type']})\n"
        return result