# -*- coding: utf-8 -*-
"""凡人界 MUD 服务器 - 基于 asyncio 的 Telnet MUD
静态房间 + 完整基建框架
"""

import asyncio
from player import Player
from commands import handle_command
from rooms import ROOMS

# 在线玩家
online_players = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"玩家连接: {addr}")
    
    # 新玩家创建
    writer.write(b"欢迎来到《凡人界》MUD！\n请输入你的名字: ")
    await writer.drain()
    
    data = await reader.readline()
    name = data.decode().strip() or "无名 adventurer"
    
    player = Player(name)
    online_players[addr] = player
    
    writer.write(f"\n欢迎，{name}！你已进入凡人界。\n".encode())
    writer.write(f"初始位置：{ROOMS[player.location]['name']}\n".encode())
    writer.write(b"输入 'help' 查看命令。\n\n")
    await writer.drain()
    
    # 发送初始房间描述
    writer.write(handle_command(player, "look").encode() + b"\n> ")
    await writer.drain()
    
    while True:
        try:
            data = await reader.readline()
            if not data:
                break
            cmd_line = data.decode().strip()
            if not cmd_line:
                writer.write(b"> ")
                await writer.drain()
                continue
            
            # 解析命令
            parts = cmd_line.split(maxsplit=1)
            cmd = parts[0]
            args = parts[1] if len(parts) > 1 else ""
            
            response = handle_command(player, cmd, args)
            writer.write(response.encode() + b"\n> ")
            await writer.drain()
            
            # 特殊退出
            if cmd.lower() in ["quit", "exit", "退出"]:
                break
                
        except Exception as e:
            print(f"玩家 {name} 出错: {e}")
            break
    
    print(f"玩家 {name} 断开连接")
    del online_players[addr]
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 8888)
    addr = server.sockets[0].getsockname()
    print(f"《凡人界》MUD 服务器启动在 {addr}")
    print("使用 telnet localhost 8888 连接")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())