import asyncio
import json
from datetime import datetime

class Player:
    def __init__(self, writer):
        self.writer = writer
        self.name = "冒险者"
        self.room = "大厅"

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.players = []

rooms = {
    "大厅": Room("大厅", "一个明亮的大厅，四周有几扇门。"),
    "森林": Room("森林", "茂密的森林，鸟鸣声不绝。"),
    "洞穴": Room("洞穴", "阴暗潮湿的洞穴。")
}

rooms["大厅"].exits = {"北": "森林", "东": "洞穴"}
rooms["森林"].exits = {"南": "大厅"}
rooms["洞穴"].exits = {"西": "大厅"}

players = []

async def broadcast(message, exclude=None):
    for player in players:
        if player != exclude:
            try:
                player.writer.write(f"{message}\n".encode())
                await player.writer.drain()
            except:
                pass

async def handle_client(writer, addr):
    player = Player(writer)
    players.append(player)
    
    writer.write("欢迎来到 MUD 世界！请输入你的名字: ".encode())
    await writer.drain()
    
    data = await writer.readline()
    name = data.decode().strip()
    if name:
        player.name = name
    
    await writer.write(f"\n{player.name} 加入了游戏！\n".encode())
    await broadcast(f"{player.name} 进入了游戏。", player)
    
    await show_room(player)
    
    while True:
        try:
            data = await writer.readline()
            if not data:
                break
            command = data.decode().strip().lower()
            
            if command in ["quit", "退出"]:
                break
            elif command == "look" or command == "l":
                await show_room(player)
            elif command.startswith("go ") or command.startswith("走 "):
                direction = command.split()[1]
                await move_player(player, direction)
            elif command.startswith("say "):
                message = command[4:]
                await broadcast(f"{player.name} 说: {message}", None)
            elif command == "help" or command == "帮助":
                await writer.write(b"\n可用命令: look, go <方向>, say <消息>, quit\n")
            else:
                await writer.write(b"未知命令。输入 help 查看帮助。\n")
        except:
            break
    
    players.remove(player)
    await broadcast(f"{player.name} 离开了游戏。", player)
    writer.close()

async def show_room(player):
    room = rooms.get(player.room)
    if not room:
        return
    msg = f"\n=== {room.name} ===\n{room.description}\n"
    if room.players:
        msg += "这里有: " + ", ".join([p.name for p in room.players if p != player]) + "\n"
    msg += "出口: " + ", ".join(room.exits.keys()) + "\n"
    player.writer.write(msg.encode())
    await player.writer.drain()

async def move_player(player, direction):
    room = rooms.get(player.room)
    if direction in room.exits:
        new_room = room.exits[direction]
        player.room = new_room
        await show_room(player)
        await broadcast(f"{player.name} 向 {direction} 走去了。", player)
    else:
        await player.writer.write(b"那个方向没有出口。\n")

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 8888)
    print(f"MUD 服务器启动在端口 8888")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
