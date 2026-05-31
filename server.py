import asyncio
import logging

# Basic MUD server stub
async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'New connection from {addr}')
    writer.write(b'Welcome to FanRenJie MUD!\n> ')
    await writer.drain()
    while True:
        data = await reader.read(100)
        if not data:
            break
        message = data.decode().strip()
        if message.lower() == 'quit':
            break
        writer.write(f'You said: {message}\n> '.encode())
        await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
