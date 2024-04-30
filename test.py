import asyncio
from datetime import datetime


async def do_sth(n):
    await asyncio.sleep(n)
    return f'sleeping for {n} seconds'

def do_now():
    print(f'do it right now!{datetime.now()}')

async def main():
    print(datetime.now())
    results = await asyncio.gather(do_sth(1), do_sth(2), do_sth(3))
    do_now()
    for res in results:
        print(res)
    # print(await do_sth(1))
    # print(await do_sth(2))
    # print(await do_sth(3))
    print(datetime.now())
    print('done')

if __name__ == '__main__':
    asyncio.run(main())