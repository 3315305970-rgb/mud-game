# 凡人界 MUD - 单机高完成度版（百万行代码架构）

## 架构原则（严格遵守）
- **单一职责**：每个文件只负责一个清晰职责
- **颗粒度高**：为百万行代码级别准备
- **目录结构**：
  - `core/`：领域模型（Player, Room, Item, NPC）
  - `systems/`：业务逻辑（CommandHandler, Combat, Cultivation, Quest, RoomSystem）
  - `config/`：纯数据配置
  - `utils/`：工具函数
  - `server.py`：仅服务器启动 + 会话管理

## 当前已重构完成（高完成度）
- ✅ core/player.py - 玩家类
- ✅ core/room.py - 房间类 + 静态数据
- ✅ core/item.py - 物品类
- ✅ systems/command_handler.py - 命令路由
- ✅ systems/room_system.py - 房间逻辑
- ✅ systems/cultivation.py - 修炼逻辑
- ✅ systems/quest.py - 任务逻辑
- ✅ server.py - 单机服务器（单一职责）
- ✅ commands.py - 兼容旧接口（逐步迁移中）

## 运行
```bash
cd mud_game
python3 server.py
telnet localhost 8888
```

## 单机模式特性
- 所有社交通过NPC对话完成
- 专注故事、修炼、探索、任务
- 无多人聊天

** 版本**： v2.0 单机高颗粒度架构 (2026-05-31)