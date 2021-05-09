import asyncio

import aiohttp


async def main():
    with aiohttp.ClientSession() as session:
        r = await session.get("https://google.com")
        html = await r.text()
        print(html)

if __name__ == '__main__':
    e = asyncio.get_event_loop()
    tasks = []
    for i in range(0, 10):
        tasks.append(main())
    t = asyncio.gather(*tasks)
    t.run_until_complite()

