import asyncio


async def main(event_loop):
    await event_loop.run_until_complete()

if __name__ == '__main__':
    e = asyncio.get_event_loop()
    print("eeee")
