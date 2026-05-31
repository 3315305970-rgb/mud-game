# -*- coding: utf-8 -*-
"""
server.py
单一职责：服务器启动 + 单机玩家会话管理
"""

import asyncio
from core.player import Player
from systems.command_handler import handle_command

async def handle_client(reader, writer):
    writer.write(b"欢迎来到《凡人界》MUD（单机版）！\n请输入你的名字: ")
    await writer.drain()
    
    data = await reader.readline()
    name = data.decode().strip() or "穿越者"
    
    player = Player(name)
    
    writer.write(f"\n欢迎，{name}！你已穿越到凡人界。\n".encode())
    writer.write(b"输入 'help' 查看命令。\n\n")
    await writer.drain()
    
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
            
            parts = cmd_line.split(maxsplit=1)
            cmd = parts[0]
            args = parts[1] if len(parts) > 1 else ""
            
            response = handle_command(player, cmd, args)
            writer.write(response.encode() + b"\n> ")
            await writer.drain()
            
            if cmd.lower() in ["quit", "exit", "退出"]:
                break
        except Exception as e:
            print(f"玩家 {name} 出错: {e}")
            break
    
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 8888)
    print(f"《凡人界》单机MUD服务器启动在 8888 端口")
    print("使用 telnet localhost 8888 连接")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())